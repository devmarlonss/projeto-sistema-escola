# Classe Adm
from usuario import Usuario
from aluno import Aluno
from professor import Professor
from disciplina import Disciplina
from curso import Curso
from turma import Turma

class Adm(Usuario):
    def __init__(self, nome, cpf, email, senha):
        super().__init__(nome, cpf, email, senha)

    # Gerência de Usuários
    def add_aluno(self, nome, cpf, email, senha, curso):
        return Aluno(nome, cpf, email, senha, curso)
    
    def add_prof(self, nome, cpf, email, senha, disciplina, salario):
        return Professor(nome, cpf, email, senha, disciplina, salario)
    
    @classmethod
    def add_adm(cls, nome, cpf, email, senha):
        return cls(nome, cpf, email, senha)
