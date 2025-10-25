# Classe Aluno
from usuario import Usuario
from curso import Curso

class Aluno(Usuario):
    def __init__(self, nome, cpf, email, senha, curso: Curso, boletim: dir = None):
        super().__init__(nome, cpf, email, senha)
        if boletim is None:
            boletim = {}
        self.__curso = curso
        self.__boletim = boletim

    @property
    def curso(self):
        return self.__curso
    
    @property
    def boletim(self):
        return self.__boletim
    
    def exibir_info(self):
        super().exibir_info()
        print(f"Curso: {self.curso.nome}")
    

if __name__ == "__main__":
    curso1 = Curso("Informática", "C001")
    aluno1 = Aluno("Marlon", "12312312312", "example@gmail.com", "senha123", curso1)

    aluno1.exibir_info()