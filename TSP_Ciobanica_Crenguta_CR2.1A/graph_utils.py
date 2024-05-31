import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import seaborn as sns  # Added seaborn for better heatmap visualization


def plot_graph(N, dist, path, algorithm_name):
    G = nx.DiGraph()

    for i in range(N):
        for j in range(N):
            if i != j:
                G.add_edge(i, j, weight=dist[i][j])

    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 7))

    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=10)
    nx.draw_networkx_labels(G, pos)

    edge_labels = {(i, j): f'{dist[i][j]}' for i in range(N) for j in range(N) if i != j}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)] + [(path[-1], path[0])]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', arrows=True, arrowstyle='-|>', arrowsize=20, width=2)

    plt.title(f"TSP Path using {algorithm_name}")  # Include algorithm name in the title
    plt.show()


def plot_matrix(N, dist):
    df = pd.DataFrame(dist, index=range(N), columns=range(N))
    plt.figure(figsize=(10, 7))
    plt.title("Distance Matrix")
    sns.heatmap(df, annot=True, fmt="d", cmap="YlGnBu", cbar=False)
    plt.xlabel("Cities")
    plt.ylabel("Cities")
    plt.show()
