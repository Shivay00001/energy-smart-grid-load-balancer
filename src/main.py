from src.grid_graph import PowerGrid
from src.balancer import LoadBalancer

def main():
    print("--- Energy Smart Grid Load Balancer ---")
    
    # 1. Build Grid
    grid = PowerGrid()
    
    # Plants
    grid.add_plant("Plant_A", capacity_mw=100) # 100 MW
    grid.add_plant("Plant_B", capacity_mw=50)  # 50 MW
    
    # Substations
    grid.add_substation("Sub_North", capacity_mw=80) 
    grid.add_substation("Sub_South", capacity_mw=60)
    
    # Lines Plant -> Sub
    grid.add_line("Plant_A", "Sub_North", max_capacity=90)
    grid.add_line("Plant_B", "Sub_South", max_capacity=45)
    
    # Homes
    for i in range(5):
        grid.add_home(f"Home_N{i}", demand_mw=10) # 50 MW Total
        grid.add_line("Sub_North", f"Home_N{i}", max_capacity=15)
        
    for i in range(4):
        grid.add_home(f"Home_S{i}", demand_mw=12) # 48 MW Total
        grid.add_line("Sub_South", f"Home_S{i}", max_capacity=15)

    # 2. Simulate
    print("\nRunning Load Flow Analysis...")
    balancer = LoadBalancer(grid)
    balancer.distribute_load()
    
    # 3. Report
    print("\n--- Grid Status ---")
    for n, attr in grid.graph.nodes(data=True):
        if attr['type'] in ['PLANT', 'SUBSTATION']:
            print(f"{n} ({attr['type']}): Load {attr['load']:.2f} / Cap {attr['capacity']:.2f} MW")
            
    print("\n--- Edge Flows ---")
    for u, v, attr in grid.graph.edges(data=True):
        print(f"{u} -> {v}: Flow {attr['current_flow']:.2f} / Cap {attr['capacity']:.2f} MW")

    # 4. Check Faults
    print("\n--- Alerts ---")
    alerts = balancer.check_overloads()
    if alerts:
        for alert in alerts:
            print(f"🚨 {alert}")
    else:
        print("✅ Grid Stable. No Overloads.")

if __name__ == "__main__":
    main()
