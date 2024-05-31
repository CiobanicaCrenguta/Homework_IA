from collections import deque
import random
import time
from graph_utils import plot_graph, plot_matrix
from bfs_tsp import bfs_tsp, reconstruct_path as bfs_reconstruct_path, total_distance as bfs_total_distance
from ucs_tsp import ucs_tsp, reconstruct_path as ucs_reconstruct_path, total_distance as ucs_total_distance
from a_star_tsp import a_star_tsp, reconstruct_path as a_star_reconstruct_path, total_distance as a_star_total_distance


def generate_random_graph(N):
    # Generate random distances between cities
    return [[0 if i == j else random.randint(1, 100) for j in range(N)] for i in range(N)]


def main():
    N = 15
    home_city = 0
    dist = generate_random_graph(N)  # Generate the graph

    print("Distance Matrix:")
    for row in dist:
        print(row)

    print("\nRunning BFS TSP:")
    start_time = time.time()
    min_max_dist_bfs, parent_bfs = bfs_tsp(N, dist, home_city)
    end_time = time.time()
    if min_max_dist_bfs != -1:
        path_bfs = bfs_reconstruct_path(parent_bfs, home_city, N)
        total_dist_bfs = bfs_total_distance(path_bfs, dist)
        print("The minimum distance between consecutive cities is:", min_max_dist_bfs)
        print("The path is:", path_bfs)
        print("The total distance is:", total_dist_bfs)
        plot_graph(N, dist, path_bfs, "BFS")  # Pass algorithm name for plotting
        print("Time taken for BFS:", end_time - start_time, "seconds")
    else:
        print("No solution found with BFS.")

    print("\nRunning UCS TSP:")
    start_time = time.time()
    min_max_dist_ucs, parent_ucs = ucs_tsp(N, dist, home_city)
    end_time = time.time()
    if min_max_dist_ucs != -1:
        path_ucs = ucs_reconstruct_path(parent_ucs, home_city, N)
        total_dist_ucs = ucs_total_distance(path_ucs, dist)
        print("The minimum distance between consecutive cities is:", min_max_dist_ucs)
        print("The path is:", path_ucs)
        print("The total distance is:", total_dist_ucs)
        plot_graph(N, dist, path_ucs, "UCS")  # Pass algorithm name for plotting
        print("Time taken for UCS:", end_time - start_time, "seconds")
    else:
        print("No solution found with UCS.")

    print("\nRunning A* TSP:")
    start_time = time.time()
    min_max_dist_a_star, parent_a_star = a_star_tsp(N, dist, home_city)
    end_time = time.time()
    if min_max_dist_a_star != -1:
        path_a_star = a_star_reconstruct_path(parent_a_star, home_city, N)
        total_dist_a_star = a_star_total_distance(path_a_star, dist)
        print("The minimum distance between consecutive cities is:", min_max_dist_a_star)
        print("The path is:", path_a_star)
        print("The total distance is:", total_dist_a_star)
        plot_graph(N, dist, path_a_star, "A*")  # Pass algorithm name for plotting
        print("Time taken for A*:", end_time - start_time, "seconds")
    else:
        print("No solution found with A*.")

    # Display the distance matrix
    plot_matrix(N, dist)


if __name__ == "__main__":
    main()
