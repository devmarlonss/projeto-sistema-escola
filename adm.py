# Classe Adm
from usuario import Usuario

class Adm(Usuario):
    def __init__(self, nome, cpf, email, senha):
        super().__init__(nome, cpf, email, senha)

    def adm_dict(self):
        return super().usuario_dict()
    
    @staticmethod
    def dict_adm(adm):
        return Adm(adm["nome"], adm["cpf"], adm["email"], adm["senha"])