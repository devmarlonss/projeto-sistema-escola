from salvar_carregar import *
from disciplina import Disciplina
from curso import Curso
from turma import Turma
from usuario import Usuario
from aluno import Aluno
from professor import Professor
from adm import Adm

class Sistema:
    def __init__(self):
        self.__disciplinas = []
        self.__cursos = []
        self.__turmas = []
        self.__alunos = []
        self.__professores = []
        self.__adms = []

    @property
    def disciplinas(self):
        return self.__disciplinas
    
    @property
    def cursos(self):
        return self.__cursos
    
    @property
    def turmas(self):
        return self.__turmas
    
    @property
    def alunos(self):
        return self.__alunos
    
    @property
    def professores(self):
        return self.__professores
    
    @property
    def adms(self):
        return self.__adms

    # Seção Carregar/Salvar 
    def carregar_disc(self):
        disciplinas = carregar_dados("disciplina.json")
        self.__disciplinas = []
        for d in disciplinas:
            self.disciplinas.append(Disciplina.dict_disc(d))
        return self.disciplinas
    
    def salvar_disc(self):
        dados = []
        for d in self.disciplinas:
            dados.append(Disciplina.disc_dict(d))
        salvar_dados("disciplina.json", dados)
    
if __name__ == "__main__":
    sistema = Sistema()
    # disc1 = Disciplina("Matemática", "D001", 120)
    # sistema.disciplinas.append(disc1)
    # sistema.salvar_disc()
    print(sistema.carregar_disc())
    sistema.disciplinas[0].exibir_info()
