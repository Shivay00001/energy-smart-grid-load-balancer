import networkx as nx

class LoadBalancer:
    def __init__(self, grid):
        self.grid = grid
        self.graph = grid.get_topology()

    def distribute_load(self):
        """
        Simulates load flow from Plants -> Substations -> Consumers.
        Uses a BFS-like approach to push demand upstream.
        """
        # Reset flows
        for u, v in self.graph.edges:
            self.graph[u][v]['current_flow'] = 0
            
        # Calculate demand per substation (aggregating homes)
        # 1. Identify Consumers
        consumers = [n for n, attr in self.graph.nodes(data=True) if attr['type'] == 'CONSUMER']
        
        for consumer in consumers:
            demand = self.graph.nodes[consumer]['demand']
            # Find feeding substation (Predecessor)
            feeding_nodes = list(self.graph.predecessors(consumer))
            if not feeding_nodes:
                continue
                
            # Naive: Split demand equally among feeders
            split_load = demand / len(feeding_nodes)
            for feeder in feeding_nodes:
                self.graph[feeder][consumer]['current_flow'] += split_load
                self.graph.nodes[feeder]['load'] += split_load
                
        # Propagate Substation Load upstream to Plants
        substations = [n for n, attr in self.graph.nodes(data=True) if attr['type'] == 'SUBSTATION']
        
        for sub in substations:
            load = self.graph.nodes[sub]['load']
            feeders = list(self.graph.predecessors(sub))
            if not feeders:
                continue
                
            split_load = load / len(feeders)
            for plant in feeders:
                self.graph[plant][sub]['current_flow'] += split_load
                self.graph.nodes[plant]['load'] += split_load

    def check_overloads(self):
        """Checks for violations."""
        overloads = []
        for u, v, attr in self.graph.edges(data=True):
            if attr['current_flow'] > attr['capacity']:
                overloads.append(f"LINE {u}->{v} OVERLOADED: {attr['current_flow']:.2f}/{attr['capacity']:.2f} MW")
        
        for n, attr in self.graph.nodes(data=True):
            if attr.get('type') in ['PLANT', 'SUBSTATION']:
                if attr['load'] > attr['capacity']:
                    overloads.append(f"NODE {n} OVERLOADED: {attr['load']:.2f}/{attr['capacity']:.2f} MW")
                    
        return overloads
