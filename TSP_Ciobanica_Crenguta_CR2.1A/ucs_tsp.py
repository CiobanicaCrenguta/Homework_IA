import heapq


def ucs_tsp(N, dist, home_city):
    min_cost = {}
    parent = {}
    start_mask = 1 << home_city
    min_cost[(home_city, start_mask)] = 0
    parent[(home_city, start_mask)] = (None, None)

    pq = [(0, home_city, start_mask)]
    heapq.heapify(pq)

    while pq:
        curr_max_dist, curr_city, visited_mask = heapq.heappop(pq)

        if visited_mask == (1 << N) - 1:
            final_max_dist = max(curr_max_dist, dist[curr_city][home_city])
            parent[(home_city, (1 << N) - 1)] = (curr_city, visited_mask)
            return final_max_dist, parent

        for next_city in range(N):
            if visited_mask & (1 << next_city) == 0:
                new_mask = visited_mask | (1 << next_city)
                new_dist = dist[curr_city][next_city]
                new_max_dist = max(curr_max_dist, new_dist)

                if (next_city, new_mask) not in min_cost or new_max_dist < min_cost[(next_city, new_mask)]:
                    min_cost[(next_city, new_mask)] = new_max_dist
                    parent[(next_city, new_mask)] = (curr_city, visited_mask)
                    heapq.heappush(pq, (new_max_dist, next_city, new_mask))

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
