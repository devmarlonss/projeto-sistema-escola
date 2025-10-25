# Classe Professor
from usuario import Usuario
from disciplina import Disciplina
from aluno import Aluno

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
        print(f"Disciplina: {self.disciplina.nome}\nSalário: R$ {self.salario:.2f}")

    def lancar_nota(self, aluno, nota):
        if (isinstance(aluno, Aluno)):
            if (aluno.adicionar_nota(self.disciplina.nome, nota)):
                return True
            return False
        return False    
    
if __name__ == "__main__":
    from curso import Curso
    curso1 = Curso("Informática", "C001")
    aluno1 = Aluno("Marlon", "12312312312", "example@gmail.com", "senha123", curso1)

    disc = Disciplina("Matemática", "D001", 120)
    prof = Professor("Prof1", "00000000001", "prof@gmail.com", "prof123", disc, 5545.22)

    prof.exibir_info()

    prof.lancar_nota(aluno1, 9.0)
    
    aluno1.ver_boletim()

    