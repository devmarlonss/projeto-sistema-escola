# Classe Professor
from usuario import Usuario
from disciplina import Disciplina

class Professor(Usuario):
    def __init__(self, nome, cpf, email, senha, disciplina: Disciplina, salario: float):
        super().__init__(nome, cpf, email, senha)
        self.__disciplina = disciplina
        self.__salario = salario

    @property 
    def disciplina(self):
        return self.__disciplina
    
    @property
    def salario(self):
        return self.__salario
    
    def exibir_info(self):
        super().exibir_info()
        print(f"Disciplina: {self.disciplina.nome}\nSalário: {self.salario:.2f}")
    