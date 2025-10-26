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
    
    # Seção Gerência de Cursos
    def buscar_curso(self, codigo):
        for c in self.cursos:
            if (c.codigo == codigo):
                return c
        return None
    
    def add_curso(self, nome, codigo):
        self.cursos.append(Curso(nome, codigo))
        return True
    
    def rem_curso(self, curso):
        if (isinstance(curso, Curso)):
            self.cursos.remove(curso)
            return True
        return False
    
    def exibir_info_curso(self, curso):
        if (isinstance(curso, Curso)):
            curso.exibir_info()
            return True
        return False
    
    def add_disc_curso(self, disc, curso):
        if (isinstance(disc, Disciplina)):
            if (isinstance(curso, Curso)):
                curso.adicionar_disc(disc)
                return True
            return False
        return False
    
    def rem_disc_curso(self, disc, curso):
        if (isinstance(disc, Disciplina)):
            if (isinstance(curso, Curso)):
                curso.remover_disc(disc)
                return True
            return False
        return False

    
    # Seção Gerência de Disciplinas
    def buscar_disc(self, codigo):
        for d in self.disciplinas:
            if (d.codigo == codigo):
                return d
        return None
    
    def add_disciplina(self, nome, codigo, carga_horaria):
        self.disciplinas.append(Disciplina(nome, codigo, carga_horaria))
        return True
    
    def rem_disciplina(self, disc):
        if (isinstance(disc, Disciplina)):
            self.disciplinas.remove(disc)
            return True
        return False
    
    def exibir_info_disc(self, disc):
        if (isinstance(disc, Disciplina)):
            disc.exibir_info()
            return True
        return False

    
    # Seção Gerência de Usuários
    def buscar_usuario(self, cpf):
        for u in self.alunos:
            if (u.cpf == cpf):
                return u
        for u in self.professores:
            if (u.cpf == cpf):
                return u
        for u in self.adms:
            if (u.cpf == cpf):
                return u
        return None

    def add_usuario(self, tipo, nome, cpf, email, senha, curso = None, disciplina = None, salario = None):
        if (tipo == "Aluno"):
            if (isinstance(curso, Curso)):
                self.alunos.append(Aluno(nome, cpf, email, senha, curso))
                return True
            return False
        elif (tipo == "Professor"):
            if (isinstance(disciplina, Disciplina) and salario):
                self.professores.append(Professor(nome, cpf, email, senha, disciplina, salario))
                return True
            return False
        elif (tipo == "Adm"):
            self.adms.append(Adm(nome, cpf, email, senha))
            return True
        return False
    
    def rem_usuario(self, usuario):
        if (usuario):
            if (isinstance(usuario, Aluno)):
                self.alunos.remove(usuario)
                return True
            elif (isinstance(usuario, Professor)):
                self.professores.remove(usuario)
                return True
            elif (isinstance(usuario, Adm)):
                self.adms.remove(usuario)
                return True
            return False
        return False
    
    def exibir_info_usu(self, usuario):
        if (usuario):
            usuario.exibir_info()
            return True
        return False

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

    # Seção Carregar/Salvar - Usuários
    def carregar_usuario(self):
        usuarios = carregar_dados("usuarios.json")
        for u in usuarios:
            usu = Usuario.dict_usuario(u)
            if (isinstance(usu, Aluno)):
                self.alunos.append(usu)
            elif (isinstance(usu, Professor)):
                self.professores.append(usu)
            elif (isinstance(usu, Adm)):
                self.adms.append(usu)
        return (self.alunos, self.professores, self.adms)

    def salvar_usuario(self):
        dados = []
        for aluno in self.alunos:
            dados.append(Aluno.aluno_dict(aluno))
        for prof in self.professores:
            dados.append(Professor.prof_dict(prof))
        for adm in self.adms:
            dados.append(Adm.adm_dict(adm))
        salvar_dados("usuarios.json", dados)

if __name__ == "__main__":
    sistema = Sistema()

    # == Teste Disciplina ==
    # disc1 = Disciplina("Matemática", "D001", 120)
    # sistema.disciplinas.append(disc1)
    # sistema.salvar_disc()
    # print(sistema.carregar_disc())
    # sistema.disciplinas[0].exibir_info()

    # == Teste Curso ==
    # disc1 = Disciplina("Matemática", "D001", 120)
    # disc2 = Disciplina("Português", "D002", 120)
    # curso1 = Curso("Informática", "C001")
    # curso1.adicionar_disc(disc1)
    # curso1.adicionar_disc(disc2)
    # sistema.cursos.append(curso1)
    # sistema.salvar_curso()
    # print(sistema.carregar_curso())
    # sistema.cursos[0].exibir_info()

    # == Teste Turma ==
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
    # print(sistema.carregar_turma())
    # sistema.turmas[0].exibir_info()
    
    # == Teste Usuários ==
    # disc1 = Disciplina("Matemática", "D001", 120)
    # disc2 = Disciplina("Português", "D002", 120)
    # curso1 = Curso("Informática", "C001")
    # curso1.adicionar_disc(disc1)
    # curso1.adicionar_disc(disc2)
    # aluno1 = Aluno("Pedro", "12312312312", "example@gmail.com", "senha123", curso1)
    # aluno2 = Aluno("Rian", "12312311211", "example@gmail.com", "senha123", curso1)
    # prof1 = Professor("Prof1", "00000000001", "prof@gmail.com", "prof123", disc1, 5545.22)
    # adm1 = Adm("Administrator", "22222222211", "adm@gmail.com", "adm123")
    # prof1.lancar_nota(aluno1, 9.0)
    # sistema.alunos.append(aluno1)
    # sistema.alunos.append(aluno2)
    # sistema.professores.append(prof1)
    # sistema.adms.append(adm1)
    # sistema.salvar_usuario()
    # print(sistema.carregar_usuario())
    # sistema.alunos[0].exibir_info()
    # sistema.alunos[0].ver_boletim()
    # print()
    # sistema.professores[0].exibir_info()
    # print()
    # sistema.adms[0].exibir_info()
