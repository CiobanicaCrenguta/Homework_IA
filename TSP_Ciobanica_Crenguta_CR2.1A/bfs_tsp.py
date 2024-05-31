from collections import deque


def bfs_tsp(N, dist, home_city):
    min_max_dist = {}
    parent = {}
    start_mask = 1 << home_city
    min_max_dist[(home_city, start_mask)] = 0
    parent[(home_city, start_mask)] = (None, None)

    Q = deque([(home_city, start_mask, 0)])

    while Q:
        curr_city, visited_mask, curr_max_dist = Q.popleft()

        if visited_mask == (1 << N) - 1:
            final_max_dist = max(curr_max_dist, dist[curr_city][home_city])
            parent[(home_city, (1 << N) - 1)] = (curr_city, visited_mask)
            return final_max_dist, parent

        for next_city in range(N):
            if visited_mask & (1 << next_city) == 0:
                new_mask = visited_mask | (1 << next_city)
                new_dist = dist[curr_city][next_city]
                new_max_dist = max(curr_max_dist, new_dist)

                if (next_city, new_mask) not in min_max_dist or new_max_dist < min_max_dist[(next_city, new_mask)]:
                    min_max_dist[(next_city, new_mask)] = new_max_dist
                    parent[(next_city, new_mask)] = (curr_city, visited_mask)
                    Q.append((next_city, new_mask, new_max_dist))

    return -1, parent


def total_distance(path, dist):
    total_dist = 0
    N = len(path)
    for i in range(N - 1):
        total_dist += dist[path[i]][path[i + 1]]
    total_dist += dist[path[-1]][path[0]]  # Add the distance back to the starting city
    return total_dist


def reconstruct_path(parent, end_city, N):
    path = []
    mask = (1 << N) - 1
    current = end_city

    while current is not None:
        path.append(current)
        current, mask = parent.get((current, mask), (None, None))

    return path[::-1]



