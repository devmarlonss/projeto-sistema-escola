# Classe Curso
from disciplina import Disciplina

class Curso:
    def __init__(self, nome: str, codigo: str, disciplinas: list = None):
        if disciplinas is None:
            disciplinas = []
        self.__nome = nome
        self.__codigo = codigo
        self.__disciplinas = disciplinas

    @property
    def nome(self):
        return self.__nome
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def disciplinas(self):
        return self.__disciplinas
    
    def exibir_info(self):
        """Exibe as informações do curso."""
        print(f"\nNome: {self.nome}\nCódigo: {self.codigo}\nDisciplinas: ")
        if (self.disciplinas):
            for d in self.disciplinas:
                print(f" - {d.nome}")
        else:
            print("Não há disciplinas cadastradas!")

    def adicionar_disc(self, disc):
        """Adiciona uma disciplina à lista de disciplinas do curso."""
        if (isinstance(disc, Disciplina) and disc not in self.disciplinas):
            self.disciplinas.append(disc)
            return True
        return False

    def remover_disc(self, disc):
        """Remove uma disciplina da lista de disciplinas do curso."""
        if (disc in self.disciplinas):
            self.disciplinas.remove(disc)
            return True
        return False

    def curso_dict(self):
        """Retorna o objeto da classe Curso em formato de dicionário."""
        disc_dict = []
        for d in self.disciplinas:
            disc_dict.append(Disciplina.disc_dict(d))

        return {
            "nome": self.nome,
            "codigo": self.codigo,
            "disciplinas": disc_dict
        }
    
    @staticmethod
    def dict_curso(curso):
        """Cria uma instância da classe Curso a partir de um dicionário."""
        disc = []
        for d in curso["disciplinas"]:
            disc.append(Disciplina.dict_disc(d))
        return Curso(curso["nome"], curso["codigo"], disc)
    
if __name__ == "__main__":
    disc1 = Disciplina("Matemática", "D001", 120)
    disc2 = Disciplina("Português", "D002", 120)

    curso1 = Curso("Informática", "C001")
    curso1.exibir_info()

    print()
    curso1.adicionar_disc(disc1)
    curso1.adicionar_disc(disc2)
    curso1.exibir_info()

    print()
    curso1.remover_disc(disc2)
    curso1.exibir_info()