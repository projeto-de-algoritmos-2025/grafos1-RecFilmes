import networkx as nx

def criar_grafo(usuarios):
    G = nx.Graph()
    G.add_nodes_from(usuarios.keys(), bipartite=0)
    for user, vistos in usuarios.items():
        G.add_nodes_from(vistos, bipartite=1)
        for f in vistos:
            G.add_edge(user, f)
    return G