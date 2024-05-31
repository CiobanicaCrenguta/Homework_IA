import heapq
import networkx as nx


def heuristic(curr_city, visited_mask, dist, N, home_city):
    unvisited = [i for i in range(N) if not (visited_mask & (1 << i))]
    if not unvisited:
        return 0

    G = nx.Graph()
    for i in unvisited:
        for j in unvisited:
            if i != j:
                G.add_edge(i, j, weight=dist[i][j])

    mst = nx.minimum_spanning_tree(G)
    if len(mst.edges) > 0:
        mst_total_weight = sum(edge[2]['weight'] for edge in mst.edges(data=True))
    else:
        mst_total_weight = 0

    min_to_unvisited = min(dist[curr_city][i] for i in unvisited) if unvisited else 0
    min_from_unvisited = min(dist[i][home_city] for i in unvisited) if unvisited else 0

    # Consider the distance between unvisited cities themselves
    min_between_unvisited = 0
    if len(unvisited) > 1:
        min_between_unvisited = min(dist[i][j] for i in unvisited for j in unvisited if i != j)

    # Dynamic adjustment based on the state of the search
    adjustment_factor = 1.0
    if len(unvisited) < N / 2:
        adjustment_factor = 0.5


    heuristic_value = adjustment_factor * (mst_total_weight + min_to_unvisited + min_from_unvisited + min_between_unvisited)

    return heuristic_value


def a_star_tsp(N, dist, home_city=0):
    min_cost = {}
    parent = {}
    start_mask = 1 << home_city
    min_cost[(home_city, start_mask)] = 0
    parent[(home_city, start_mask)] = (None, None)

    pq = [(heuristic(home_city, start_mask, dist, N, home_city), 0, home_city, start_mask)]
    heapq.heapify(pq)

    while pq:
        curr_f, curr_g, curr_city, visited_mask = heapq.heappop(pq)

        if visited_mask == (1 << N) - 1:
            final_cost = max(curr_g, dist[curr_city][home_city])
            parent[(home_city, (1 << N) - 1)] = (curr_city, visited_mask)
            return final_cost, parent

        for next_city in range(N):
            if visited_mask & (1 << next_city) == 0:
                new_mask = visited_mask | (1 << next_city)
                new_g = max(curr_g, dist[curr_city][next_city])
                new_f = max(new_g, heuristic(next_city, new_mask, dist, N, home_city))

                if (next_city, new_mask) not in min_cost or new_g < min_cost[(next_city, new_mask)]:
                    min_cost[(next_city, new_mask)] = new_g
                    parent[(next_city, new_mask)] = (curr_city, visited_mask)
                    heapq.heappush(pq, (new_f, new_g, next_city, new_mask))

    return -1, parent


def reconstruct_path(parent, end_city, N):
    path = []
    mask = (1 << N) - 1
    current = end_city

    while current is not None:
        path.append(current)
        current, mask = parent[(current, mask)]

    return path[::-1]


def total_distance(path, dist):
    total_dist = 0
    N = len(path)
    for i in range(N - 1):
        total_dist += dist[path[i]][path[i + 1]]
    total_dist += dist[path[-1]][path[0]]  # Add the distance back to the starting city
    return total_dist
