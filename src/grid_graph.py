import networkx as nx
import random

class PowerGrid:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_plant(self, name: str, capacity_mw: float):
        self.graph.add_node(name, type="PLANT", capacity=capacity_mw, load=0)

    def add_substation(self, name: str, capacity_mw: float):
        self.graph.add_node(name, type="SUBSTATION", capacity=capacity_mw, load=0)

    def add_home(self, name: str, demand_mw: float):
        self.graph.add_node(name, type="CONSUMER", demand=demand_mw)

    def add_line(self, u: str, v: str, max_capacity: float):
        self.graph.add_edge(u, v, capacity=max_capacity, current_flow=0)

    def get_topology(self):
        return self.graph
