# Classe Disciplina
from salvar_carregar import *

class Disciplina:
    def __init__(self, nome: str, codigo: str, carga_horaria: int):
        self.__nome = nome
        self.__codigo = codigo
        self.__carga_horaria = carga_horaria

    @property
    def nome(self):
        return self.__nome
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def carga_horaria(self):
        return self.__carga_horaria

    def exibir_info(self):
        print(f"Nome: {self.nome}\nCódigo: {self.codigo}\nCarga Horária: {self.carga_horaria} horas")

    def disc_dict(self):
        return {
            "nome": self.nome,
            "codigo": self.codigo,
            "carga_horaria": self.carga_horaria
        }
    
    @staticmethod
    def dict_disc(disc):
        return Disciplina(disc["nome"], disc["codigo"], disc["carga_horaria"])

if __name__ == "__main__":
    disc = Disciplina("Matemática", "D002", 40)

    disc.exibir_info()