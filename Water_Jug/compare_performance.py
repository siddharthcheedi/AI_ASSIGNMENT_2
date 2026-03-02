from search_algorithms import bfs, dfs, ids, dls
from water_jug import WaterJugProblem

def print_result(algo_name, result, time_taken, nodes, print_path=False):
    print(f"\n==========================================")
    print(f" {algo_name} ")
    print(f"==========================================")
    if result is None or result == 'cutoff':
        print(f"Result: No solution found ({result}).")
    else:
        path = result.path()
        print(f"Result: Solution found in {len(path)-1} steps.")
        if print_path:
            print("Path taken:")
            for n in path[1:]:
                print(f"  > {n.action}    => Current State: {n.state}")
    print(f"Nodes Explored: {nodes}")
    print(f"Time Taken:     {time_taken:.6f} seconds")

def main():
    print("Initializing Milk and Water Jug Problem")
    print("Jug 1 Capacity: 5L")
    print("Jug 2 Capacity: 3L")
    print("Target: 4L in either jug")
    
    problem = WaterJugProblem(5, 3, 4)
    
    print("\nStarting Performance Comparison...")
    
    # 1. BFS
    res_bfs, t_bfs, n_bfs = bfs(problem)
    print_result("Breadth-First Search (BFS)", res_bfs, t_bfs, n_bfs, print_path=True)
    
    # 2. DFS
    res_dfs, t_dfs, n_dfs = dfs(problem)
    # DFS might have a longer path, let's print it to see the difference from BFS
    print_result("Depth-First Search (DFS)", res_dfs, t_dfs, n_dfs, print_path=True)
    
    # 3. DLS (Limit=4, deliberately short to cause cutoff)
    res_dls, t_dls, n_dls = dls(problem, limit=4)
    print_result("Depth-Limited Search (DLS, limit=4)", res_dls, t_dls, n_dls)
    
    # 4. IDS
    res_ids, t_ids, n_ids = ids(problem)
    print_result("Iterative Deepening Search (IDS)", res_ids, t_ids, n_ids, print_path=True)

if __name__ == "__main__":
    main()
