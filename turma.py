# Classe Turma
from curso import Curso

class Turma:
    def __init__(self, codigo: str, curso: Curso, alunos: list = None):
        if alunos is None:
            alunos = []
        self.__codigo = codigo
        self.__curso = curso
        self.__alunos = alunos

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def curso(self):
        return self.__curso

    @property
    def alunos(self):
        return self.__alunos        
    
    def exibir_info(self):
        print(f"Código: {self.codigo}\n Curso: {self.curso.nome}\n Alunos: ")
        if (self.alunos):
            for a in self.alunos:
                print(f" - {a.nome}")
        else:
            print("Não há alunos cadastrados!")

    