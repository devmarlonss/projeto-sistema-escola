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

    def ver_boletim(self):
        if (self.boletim):
            for k, v in self.boletim.items():
                print(f"\nDisciplina: {k}")
                print(f"Notas: {v}")
        else:
            print("Não há notas cadastradas!")

    def adicionar_nota(self, disciplina, nota):
        try:
            if (disciplina in self.boletim):
                self.boletim[disciplina].append(nota)
            else:
                self.boletim[disciplina] = [nota]
            return True
        except Exception:
            return False
    
    def aluno_dict(self):
        dados = super().usuario_dict()
        dados["tipo"] = "Aluno"
        dados["curso"] = Curso.curso_dict(self.curso)
        dados["boletim"] = self.boletim
        return dados
    
    @staticmethod
    def dict_aluno(aluno):
        curso = Curso.dict_curso(aluno["curso"])
        return Aluno(aluno["nome"], aluno["cpf"], aluno["email"], aluno["senha"], curso, aluno["boletim"])

if __name__ == "__main__":
    curso1 = Curso("Informática", "C001")
    aluno1 = Aluno("Marlon", "12312312312", "example@gmail.com", "senha123", curso1)

    aluno1.exibir_info()
    aluno1.ver_boletim()

    aluno1.adicionar_nota("Matemática", 8.5)
    aluno1.adicionar_nota("Matemática", 9.0)
    aluno1.adicionar_nota("Português", 10.0)

    aluno1.ver_boletim()
