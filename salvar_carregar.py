# Funções para salvar/carregar JSON
import json

def salvar_dados(arquivo, dados):
    """Salva os dados em um arquivo JSON."""
    with open(("Dados/" + arquivo), "w", encoding="utf-8") as arq:
        json.dump(dados, arq, indent=4, ensure_ascii=False)

def carregar_dados(arquivo):
    """Carrega os dados de um arquivo JSON e retorna o conteúdo."""
    try:
        with open(("Dados/" + arquivo), "r", encoding="utf-8") as arq:
            return json.load(arq)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}