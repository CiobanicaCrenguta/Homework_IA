

## Project Structure

Here’s a quick overview of the project files:

├── bfs_tsp.py         # BFS algorithm implementation
├── ucs_tsp.py         # UCS algorithm implementation
├── a_star_tsp.py      # A* algorithm implementation
├── graph_utils.py     # Utility functions for graph plotting
├── main.py            # Main script to run the TSP solvers
├── README.md          # This file

## Prerequisites

 Python 3.6+ installed. 

## How to Run

To see the TSP solvers in action, just run the main script:

This will execute all three algorithms and display the results.

## Example Usage

Here's an example of how to run the TSP solvers from the `main.py` script:
import random
from graph_utils import plot_graph, plot_matrix
from bfs_tsp import bfs_tsp, reconstruct_path as bfs_reconstruct_path
from ucs_tsp import ucs_tsp, reconstruct_path as ucs_reconstruct_path
from a_star_tsp import a_star_tsp, reconstruct_path as a_star_reconstruct_path

def generate_random_graph(N):
    return [[0 if i == j else random.randint(1, 100) for j in range(N)] for i in range(N)]

def main():
    N = 10
    home_city = 0
    dist = generate_random_graph(N)

    print("Running BFS TSP:")
    total_distance_bfs, parent_bfs = bfs_tsp(N, dist, home_city)
    path_bfs = bfs_reconstruct_path(parent_bfs, home_city, N)
    print("Total distance:", total_distance_bfs)
    print("Path:", path_bfs)
    plot_graph(N, dist, path_bfs, "BFS")

    print("\nRunning UCS TSP:")
    total_distance_ucs, parent_ucs = ucs_tsp(N, dist, home_city)
    path_ucs = ucs_reconstruct_path(parent_ucs, home_city, N)
    print("Total distance:", total_distance_ucs)
    print("Path:", path_ucs)
    plot_graph(N, dist, path_ucs, "UCS")

    print("\nRunning A* TSP:")
    total_distance_a_star, parent_a_star = a_star_tsp(N, dist, home_city)
    path_a_star = a_star_reconstruct_path(parent_a_star, home_city, N)
    print("Total distance:", total_distance_a_star)
    print("Path:", path_a_star)
    plot_graph(N, dist, path_a_star, "A*")

    plot_matrix(N, dist)

if __name__ == "__main__":
    main()
    
## Output
The main.py script will display the total distance and path for each algorithm, and plot the results.

## License

This project is licensed under the MIT License
