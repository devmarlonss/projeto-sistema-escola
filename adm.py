# Classe Adm
from usuario import Usuario

class Adm(Usuario):
    def __init__(self, nome, cpf, email, senha):
        super().__init__(nome, cpf, email, senha)

    def adm_dict(self):
        dados = super().usuario_dict()
        dados["tipo"] = "Adm"
        return dados
    
    @staticmethod
    def dict_adm(adm):
        return Adm(adm["nome"], adm["cpf"], adm["email"], adm["senha"])