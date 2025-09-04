import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

from data import carregar_dados, salvar_dados
from logica_grafo import criar_grafo
from recomendador import recomendar

# --- Carregar dados ---
usuarios = carregar_dados("usuarios.json", {})
filmes = carregar_dados("filmes.json", {})

# --- Interface ---
st.set_page_config(page_title="Recomendador de Filmes", page_icon="🎬", layout="wide")
st.title("🎬 Sistema de Recomendação de Filmes com Grafos")

# Criar novo usuário
st.sidebar.header("👤 Gerenciamento de Usuários")
novo_usuario = st.sidebar.text_input("Novo usuário")
if st.sidebar.button("Adicionar usuário"):
    if novo_usuario and novo_usuario not in usuarios:
        usuarios[novo_usuario] = []
        salvar_dados("usuarios.json", usuarios)
        st.sidebar.success(f"Usuário {novo_usuario} criado!")
    elif novo_usuario in usuarios:
        st.sidebar.warning("Usuário já existe!")

# Selecionar usuário
usuario_selecionado = st.selectbox("Escolha um usuário", list(usuarios.keys()) if usuarios else [])

if usuario_selecionado:
    st.subheader(f"📌 Filmes já assistidos por {usuario_selecionado}")
    st.write(", ".join(usuarios[usuario_selecionado]) if usuarios[usuario_selecionado] else "Nenhum filme assistido.")

    # Adicionar filme
    filme_add = st.selectbox("Adicionar filme", [f for f in filmes.keys() if f not in usuarios[usuario_selecionado]])
    if st.button("Adicionar filme ao usuário"):
        usuarios[usuario_selecionado].append(filme_add)
        salvar_dados("usuarios.json", usuarios)
        st.success(f"{filme_add} adicionado a {usuario_selecionado}")

    # Recomendações
    st.subheader("✨ Recomendações")
    recs = recomendar(usuario_selecionado, usuarios)

    if recs:
        cols = st.columns(len(recs))
        for i, r in enumerate(recs):
            if r in filmes:
                with cols[i]:
                    st.image(filmes[r]["capa"], width=150)
                    st.write(f"**{r}**")
                    st.caption(filmes[r]["sinopse"])
    else:
        st.warning("Nenhuma recomendação encontrada.")

    # Grafo
    st.subheader("🌐 Grafo de Usuários e Filmes")
    G = criar_grafo(usuarios)
    fig, ax = plt.subplots(figsize=(8, 6))
    pos = {}
    pos.update((user, (0, i)) for i, user in enumerate(usuarios.keys()))
    todos_filmes = set(f for lista in usuarios.values() for f in lista)
    pos.update((f, (1, i)) for i, f in enumerate(todos_filmes))

    nx.draw(
        G, pos, with_labels=True,
        node_size=1500, node_color=[
            "lightgreen" if n == usuario_selecionado else
            "lightblue" if n in usuarios else
            "lightcoral"
            for n in G.nodes()
        ],
        font_size=9, ax=ax
    )
    st.pyplot(fig)