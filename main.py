# Menu principal do sistema
from sistema import Sistema
from time import sleep

sistema = Sistema()
sistema.carregar_disc()
sistema.carregar_curso()
sistema.carregar_turma()
sistema.carregar_usuario()

def menu_adm(adm):
    pass

def menu_prof(prof):
    pass

def menu_aluno(aluno):
    while (True):
        sleep(1)
        print(f"\n== MENU - ALUNO ({aluno.nome}) ==\n")
        op4 = int(input("1 - Ver Boletim\n2 - Exibir Curso\n3 - Exibir Disciplina\n4 - Exibir Informações\n5 - Sair\nO que deseja fazer? "))

        if (op4 == 1):
            aluno.ver_boletim()
            continue
        elif (op4 == 2):
            cod_curso = str(input("\nCódigo do Curso: "))
            curso = sistema.buscar_curso(cod_curso)
            if (curso):
                curso.exibir_info()
                continue
            print("\nCURSO NÃO ENCONTRADO!")
            continue
        elif (op4 == 3):
            cod_disc = str(input("\nCódigo da Disciplina: "))
            disc = sistema.buscar_disc(cod_disc)
            if (disc):
                disc.exibir_info()
                continue
            print("\nDISCIPLINA NÃO ENCONTRADA!")
            continue
        elif (op4 == 4):
            aluno.exibir_info()
            continue
        elif (op4 == 5):
            return None
        else:
            print("\nOPÇÃO INVÁLIDA")


def login():
    while (True):
        sleep(1)
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
        return usuario


def cadastro():
    while (True):
        sleep(1)
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

def main():
    to_login = False
    while (True):
        sleep(1)
        print("\n== SISTEMA ESCOLAR ==\n")
        op1 = int(input("1 - Cadastrar-se\n2 - Fazer Login\n3 - Sair\nO que deseja fazer? "))

        if (op1 == 1):
            result_cadastro = cadastro()
            if (result_cadastro == None):
                continue
            elif (result_cadastro):
                print("\nUSUÁRIO CADASTRADO COM SUCESSO!")
                sistema.salvar_usuario()
                to_login = True
                sleep(1)
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
            result_login = login()
            if (result_login is None):
                continue
            else:
                print("\nLOGIN REALIZADO COM SUCESSO!")
                sleep(1)
                break

    from aluno import Aluno
    from professor import Professor
    from adm import Adm
    usuario = result_login
    print(f"\n== BEM - VINDO, {usuario.nome}! ==")
    sleep(1)
    if (isinstance(usuario, Aluno)):
        menu_aluno(usuario)
    elif (isinstance(usuario, Professor)):
        menu_prof(usuario)
    elif (isinstance(usuario, Adm)):
        menu_adm(usuario)
    else:
        print("\nERRO AO CARREGAR INTERFACE!")

main()