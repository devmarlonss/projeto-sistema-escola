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
        """Exibe as informações do professor."""
        super().exibir_info()
        print(f"Disciplina: {self.disciplina.nome}\nSalário: R$ {self.salario:.2f}")
    
    def prof_dict(self):
        """Retorna o objeto da classe Professor em formato de dicionário."""
        dados = super().usuario_dict()
        dados["tipo"] = "Professor"
        dados["disciplina"] = Disciplina.disc_dict(self.disciplina)
        dados["salario"] = self.salario
        return dados
    
    @staticmethod
    def dict_prof(prof):
        """Cria uma instância da classe Professor a partir de um dicionário"""
        disc = Disciplina.dict_disc(prof["disciplina"])
        return Professor(prof["nome"], prof["cpf"], prof["email"], prof["senha"], disc, prof["salario"])
    
if __name__ == "__main__":
    from curso import Curso
    curso1 = Curso("Informática", "C001")
    aluno1 = Aluno("Marlon", "12312312312", "example@gmail.com", "senha123", curso1)

    disc = Disciplina("Matemática", "D001", 120)
    prof = Professor("Prof1", "00000000001", "prof@gmail.com", "prof123", disc, 5545.22)

    prof.exibir_info()

    prof.lancar_nota(aluno1, 9.0)
    
    aluno1.ver_boletim()

    