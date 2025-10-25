# Funções para salvar/carregar JSON
import json

def salvar_dados(arquivo, dados):
    with open(("Dados/" + arquivo), "w", encoding="utf-8") as arq:
        json.dump(dados, arq, indent=4, ensure_ascii=False)

def carregar_dados(arquivo):
    try:
        with open(("Dados/" + arquivo), "r", encoding="utf-8") as arq:
            return json.load(arq)
    except FileNotFoundError:
        return {}