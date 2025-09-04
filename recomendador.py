
from logica_grafo import criar_grafo

def recomendar(usuario, usuarios):
    G = criar_grafo(usuarios)
    vistos = set(usuarios[usuario])
    recomendados = set()

    for vizinho in G.neighbors(usuario):
        for outro in G.neighbors(vizinho):
            if outro in usuarios and outro != usuario:
                recomendados.update(set(usuarios[outro]) - vistos)
    return list(recomendados)