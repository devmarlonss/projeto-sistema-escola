# Classe Adm
from usuario import Usuario

class Adm(Usuario):
    def __init__(self, nome, cpf, email, senha):
        super().__init__(nome, cpf, email, senha)

    