import json
import os

def carregar_dados(arquivo, padrao):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            return json.load(f)
    return padrao

def salvar_dados(arquivo, dados):
    with open(arquivo, "w") as f:
        json.dump(dados, f, indent=4)