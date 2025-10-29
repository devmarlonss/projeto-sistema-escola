# Menu principal do sistema
from sistema import Sistema

sistema = Sistema()
sistema.carregar_disc()
sistema.carregar_curso()
sistema.carregar_turma()
sistema.carregar_usuario()

def login():
    while (True):
        print("\n== FAZER LOGIN ==\n")
        cpf = str(input("CPF: "))
        if (not sistema.iscpf(cpf)):
            print("\nCPF INVÁLIDO!")
            continue
        senha = str(input("Senha: "))

        usuario = sistema.buscar_usuario(cpf)
        if (usuario is None):
            print("\nUSUÁRIO NÃO CADASTRADO NO SISTEMA!")
            op3 = str(input("\nDeseja seguir para o cadastro? [s/n] "))
            if (op3.lower() == "s"):
                return None
            else:
                continue
            
        if (not sistema.verificar_senha(usuario, senha)):
            print("\nSENHA INCORRETA!")
            continue
        return True


def cadastro():
    while (True):
        print("\n== CADASTRAR-SE ==\n")
        op2 = int(input("1 - Aluno\n2 - Professor\n3 - Administrador\n\n4 - Voltar\n\nVocê é um: "))

        if (op2 == 4):
            return None
        elif (op2 not in [1, 2, 3]):
            print("\nOPÇÃO INVÁLIDA!")
            continue

        nome = str(input("\nNome: "))
        cpf = str(input("CPF: "))
        if (not sistema.iscpf(cpf)):
            print("\nCPF INVÁLIDO!")
            continue
        if (sistema.buscar_usuario(cpf)):
            print("\nUSUÁRIO JÁ CADASTRADO COM ESTE CPF!")
            continue

        email = str(input("Email: "))
        senha = str(input("Senha: "))

        if (op2 == 1):
            _curso = str(input("Curso: "))
            for c in sistema.cursos:
                if (c.nome == _curso):
                    _curso = c.codigo
                    break

            _curso = sistema.buscar_curso(_curso)
            if (_curso is None):
                print("\nCURSO NÃO ENCONTRADO!")
                continue
            
            return sistema.add_usuario("Aluno", nome, cpf, email, senha, curso = _curso)
        
        elif (op2 == 2):
            disciplina = str(input("Disciplina: "))
            for d in sistema.disciplinas:
                if (d.nome == disciplina):
                    disciplina = d.codigo
                    break

            disciplina = sistema.buscar_disc(disciplina)
            if (disciplina is None):
                print("\nDISCIPLINA NÃO ENCONTRADA!")        
                continue
            
            _salario = float(input("Salário: "))
            return sistema.add_usuario("Professor", nome, cpf, email, senha, disciplina=disciplina, salario=_salario)
        
        elif (op2 == 3):
            return sistema.add_usuario("Adm", nome, cpf, email, senha)        

def menu():
    to_login = False
    while (True):
        print("\n== SISTEMA ESCOLAR ==\n")
        op1 = int(input("1 - Cadastrar-se\n2 - Fazer Login\n3 - Sair\nO que deseja fazer? "))

        if (op1 == 1):
            result = cadastro()
            if (result == None):
                continue
            elif (result):
                print("\nUSUÁRIO CADASTRADO COM SUCESSO!")
                sistema.salvar_usuario()
                to_login = True
            else:
                print("\nERRO AO CADASTRAR USUÁRIO")
                continue
        elif (op1 == 2):
            to_login = True
        elif (op1 == 3):
            break
        else:
            print("\nOPÇÃO INVÁLIDA!")
            continue
        
        if (to_login):
            res = login()
            if (res is None):
                continue
            else:
                print("\nLOGIN REALIZADO COM SUCESSO!")
                break
menu()