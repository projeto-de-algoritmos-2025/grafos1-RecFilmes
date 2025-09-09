from collections import defaultdict
from logica_grafo import criar_grafo

def recomendar(usuario, usuarios):
    G = criar_grafo(usuarios)
    vistos = set(usuarios[usuario])
    
    similaridade = defaultdict(int)
    for filme_visto in G.neighbors(usuario):
        for outro_usuario in G.neighbors(filme_visto):
            if outro_usuario in usuarios and outro_usuario != usuario:
                similaridade[outro_usuario] += 1
    
    usuarios_similares_ordenados = sorted(similaridade.keys(), key=lambda u: similaridade[u], reverse=True)
    
    recomendados_ordenados = []
    filmes_ja_adicionados = set()

    for user_similar in usuarios_similares_ordenados:
        filmes_para_recomendar = set(usuarios[user_similar]) - vistos
        
        for filme in filmes_para_recomendar:
            if filme not in filmes_ja_adicionados:
                recomendados_ordenados.append(filme)
                filmes_ja_adicionados.add(filme)
                
    return recomendados_ordenados