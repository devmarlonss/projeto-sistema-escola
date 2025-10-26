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

    # Seção Carregar/Salvar - Disciplinas
    def carregar_disc(self):
        disciplinas = carregar_dados("disciplinas.json")
        self.__disciplinas = []
        for d in disciplinas:
            self.disciplinas.append(Disciplina.dict_disc(d))
        return self.disciplinas
    
    def salvar_disc(self):
        dados = []
        for d in self.disciplinas:
            dados.append(Disciplina.disc_dict(d))
        salvar_dados("disciplinas.json", dados)
    
    # Seção Carregar/Salvar - Cursos
    def carregar_curso(self):
        cursos = carregar_dados("cursos.json")
        self.__cursos = []
        for c in cursos:
            self.cursos.append(Curso.dict_curso(c))
        return self.cursos
    
    def salvar_curso(self):
        dados = []
        for c in self.cursos:
            dados.append(Curso.curso_dict(c))
        salvar_dados("cursos.json", dados)

    # Seção Carregar/Salvar - Turmas
    def carregar_turma(self):
        turmas = carregar_dados("turmas.json")
        self.__turmas = []
        for t in turmas:
            self.turmas.append(Turma.dict_turma(t))
        return self.turmas

    def salvar_turma(self):
        dados = []
        for t in self.turmas:
            dados.append(Turma.turma_dict(t))
        salvar_dados("turmas.json", dados)

if __name__ == "__main__":
    sistema = Sistema()

    # disc1 = Disciplina("Matemática", "D001", 120)
    # sistema.disciplinas.append(disc1)
    # sistema.salvar_disc()
    # print(sistema.carregar_disc())
    # sistema.disciplinas[0].exibir_info()

    # disc1 = Disciplina("Matemática", "D001", 120)
    # disc2 = Disciplina("Português", "D002", 120)
    # curso1 = Curso("Informática", "C001")
    # curso1.adicionar_disc(disc1)
    # curso1.adicionar_disc(disc2)
    # sistema.cursos.append(curso1)
    # sistema.salvar_curso()
    # print(sistema.carregar_curso())
    # sistema.cursos[0].exibir_info()

    # disc1 = Disciplina("Matemática", "D001", 120)
    # disc2 = Disciplina("Português", "D002", 120)
    # curso1 = Curso("Informática", "C001")
    # curso1.adicionar_disc(disc1)
    # curso1.adicionar_disc(disc2)
    # aluno1 = Aluno("Pedro", "12312312312", "example@gmail.com", "senha123", curso1)
    # aluno2 = Aluno("Rian", "12312311211", "example@gmail.com", "senha123", curso1)
    # turma1 = Turma("T001", curso1)
    # turma1.adicionar_aluno(aluno1)
    # turma1.adicionar_aluno(aluno2)
    # sistema.turmas.append(turma1)
    # sistema.salvar_turma()
    print(sistema.carregar_turma())
    sistema.turmas[0].exibir_info()
    
