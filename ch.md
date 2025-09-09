# 🎬 Sistema de Recomendação de Filmes com Grafos

Este projeto foi desenvolvido como parte da disciplina **Projeto de Algoritmos**, com foco no estudo de **grafos** e suas aplicações.  
O sistema simula uma rede de **usuários e filmes** e utiliza conexões em grafo para gerar recomendações.

---

## 🚀 Funcionalidades
- Criar usuários e adicionar filmes assistidos
- Visualizar graficamente a rede de usuários e filmes (grafo bipartido)
- Obter recomendações de filmes com base nas conexões do grafo

---

## 🧩 Conceito de Grafo Utilizado
- O grafo é **bipartido**, conectando **usuários ↔ filmes**  
- As arestas representam que **um usuário assistiu a um filme**  
- As recomendações são feitas analisando **vizinhos comuns**:
  - Se o usuário A assistiu "Matrix"
  - E o usuário B também assistiu "Matrix", mas viu "Inception"
  - Então A pode receber "Inception" como recomendação

---

## 🛠️ Tecnologias
- **Python 3.13**
- **Streamlit** (interface gráfica)
- **NetworkX** (criação e manipulação de grafos)
- **Matplotlib** (visualização do grafo)

---

## 📂 Estrutura do Projeto