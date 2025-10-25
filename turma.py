# Classe Turma
from curso import Curso
from aluno import Aluno

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
        print(f"Código: {self.codigo}\nCurso: {self.curso.nome}\nAlunos: ")
        if (self.alunos):
            for a in self.alunos:
                print(f" - {a.nome}")
        else:
            print("Não há alunos cadastrados!")

    def adicionar_aluno(self, aluno):
        if (isinstance(aluno, Aluno) and aluno not in self.alunos):
            self.alunos.append(aluno)
            return True
        return False

    def remover_aluno(self, aluno):
        if (aluno in self.alunos):
            self.alunos.remove(aluno)
            return True
        return False

if __name__ == "__main__":
    curso1 = Curso("Informática", "C001")
    aluno1 = Aluno("Marlon", "12312312312", "example@gmail.com", "senha123", curso1)
    aluno2 = Aluno("Rian", "12312311211", "example@gmail.com", "senha123", curso1)

    turma1 = Turma("T001", curso1)
    turma1.exibir_info()
    print()
    turma1.adicionar_aluno(aluno1)
    turma1.adicionar_aluno(aluno2)
    turma1.exibir_info()
    print()
    turma1.remover_aluno(aluno2)
    turma1.exibir_info()