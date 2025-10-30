# Menu principal do sistema
from sistema import Sistema
from time import sleep

sistema = Sistema()
sistema.carregar_disc()
sistema.carregar_curso()
sistema.carregar_turma()
sistema.carregar_usuario()

def menu_adm(adm):
    while (True):
        sleep(1)
        print(f"\n== MENU - ADM ({adm.nome}) ==\n")
        op = int(input("== Gerência Usuário ==\n1 - Adicionar Usuário\n2 - Remover Usuário\n3 - Exibir Usuário\n\n== Gerência Disciplina ==\n4 - Adicionar Disciplina\n5 - Remover Disciplina\n6 - Exibir Disciplina\n\n== Gerência Curso ==\n7 - Adicionar Curso\n8 - Remover Curso\n9 - Adicionar Disciplina ao Curso\n10 - Remover Disciplina do Curso\n11 - Exibir Curso\n\n== Gerência Turma ==\n12 - Adicionar Turma\n13 - Remover Turma\n14 - Adicionar Aluno à Turma\n15 - Remover Aluno da Turma\n16 - Exibir Turma\n\n17 - Sair\n\nO que deseja fazer? "))

        # Gerência Usuário
        if (op == 1):
            result_cadastro = cadastro()
            if (result_cadastro == None):
                continue
            elif (result_cadastro):
                print("\nUSUÁRIO CADASTRADO COM SUCESSO!")
                sistema.salvar_usuario()
            else:
                print("\nERRO AO CADASTRAR USUÁRIO")

        elif (op == 2):
            cpf_usuario = str(input("\nCPF do Usuário: "))
            if (not sistema.iscpf(cpf_usuario)):
                print("\nCPF INVÁLIDO")
                continue

            usuario = sistema.buscar_usuario(cpf_usuario)
            if (usuario):
                if (sistema.rem_usuario(usuario)):
                    print("\nUSUÁRIO REMOVIDO COM SUCESSO!")
                    sistema.salvar_usuario()
                    continue
                print("\nERRO AO REMOVER O USUÁRIO!")
                continue
            print("\nUSUÁRIO NÃO ENCONTRADO!")

        elif (op == 3):
            cpf_usuario = str(input("\nCPF do Usuário: "))
            if (not sistema.iscpf(cpf_usuario)):
                print("\nCPF INVÁLIDO")
                continue

            usuario = sistema.buscar_usuario(cpf_usuario)
            if (usuario):
                usuario.exibir_info()
                continue
            print("\nUSUÁRIO NÃO ENCONTRADO!")

        # Gerência Disciplina
        elif (op == 4):
            nome = str(input("\nNome: "))
            cod_disc = str(input("Código da Disciplina: "))
            if (sistema.buscar_disc(cod_disc)):
                print("\nDISCIPLINA JÁ CADASTRADA! (CÓDIGO)")
                continue

            carga_horaria = int(input("Carga Horária: "))
            if (sistema.add_disciplina(nome, cod_disc, carga_horaria)):
                print("\nDISCIPLINA ADICIONADA COM SUCESSO!")
                sistema.salvar_disc()
                continue
            print("\nERRO AO ADICIONAR DISCIPLINA!")
            
        elif (op == 5):
            cod_disc = str(input("\nCódigo da Disciplina: "))

            disc = sistema.buscar_disc(cod_disc)
            if (disc):
                if (sistema.rem_disciplina(disc)):
                    print("\nDISCIPLINA REMOVIDA COM SUCESSO!")
                    sistema.salvar_disc()
                    continue
                print("\nERRO AO REMOVER DISCIPLINA!")
                continue
            print("\nDISCIPLINA NÃO ENCONTRADA!")
        
        elif (op == 6):
            cod_disc = str(input("\nCódigo da Disciplina: "))

            disc = sistema.buscar_disc(cod_disc)
            if (disc):
                disc.exibir_info()
                continue
            print("\nDISCIPLINA NÃO ENCONTRADA!")

        # Gerência Curso
        elif (op == 7):
            nome = str(input("\nNome: "))
            cod_curso = str(input("Código do Curso: "))
            if (sistema.buscar_curso(cod_curso)):
                print("\nCURSO JÁ CADASTRADO! (CÓDIGO)")
                continue

            if (sistema.add_curso(nome, cod_curso)):
                print("\nCURSO ADICIONADO COM SUCESSO!")
                sistema.salvar_curso()
                continue
            print("\nERRO AO ADICIONAR CURSO!")

        elif (op == 8):
            cod_curso = str(input("\nCódigo do Curso: "))

            curso = sistema.buscar_curso(cod_curso)
            if (curso):
                if (sistema.rem_curso(curso)):
                    print("\nCURSO REMOVIDO COM SUCESSO!")
                    sistema.salvar_curso()
                    continue
                print("\nERRO AO REMOVER CURSO!")
                continue
            print("\nCURSO NÃO ENCONTRADO!")

        elif (op == 9):
            cod_disc = str(input("\nCódigo da Disciplina: "))
            disc = sistema.buscar_disc(cod_disc)
            if (disc is None):
                print("\nDISCIPLINA NÃO ENCONTRADA!")
                continue
            
            cod_curso = str(input("Código do Curso: "))
            curso = sistema.buscar_curso(cod_curso)
            if (curso is None):
                print("\nCURSO NÃO ENCONTRADO!")
                continue
            
            discincurso = False
            for d in curso.disciplinas:
                if (disc.codigo in d.codigo):
                    discincurso = True
                    break

            if (discincurso):
                print("\nDISCIPLINA JÁ ESTÁ NO CURSO!")
                continue

            if (sistema.add_disc_curso(disc, curso)):
                print("\nDISCIPLINA ADICIONADA AO CURSO COM SUCESSO!")
                sistema.salvar_curso()
                continue
            print("\nERRO AO ADICIONAR DISCIPLINA AO CURSO!")

        elif (op == 10):
            cod_disc = str(input("\nCódigo da Disciplina: "))
            
            cod_curso = str(input("Código do Curso: "))
            curso = sistema.buscar_curso(cod_curso)
            if (curso is None):
                print("\nCURSO NÃO ENCONTRADO!")
                continue
            
            disc = None
            for d in curso.disciplinas:
                if (cod_disc == d.codigo):
                    disc = d
                    break

            if (disc is None):
                print("\nDISCIPLINA NÃO ESTÁ NO CURSO!")
                continue

            if (sistema.rem_disc_curso(disc, curso)):
                print("\nDISCIPLINA REMOVIDA DO CURSO COM SUCESSO!")
                sistema.salvar_curso()
                continue
            print("\nERRO AO REMOVER DISCIPLINA DO CURSO!")

        elif (op == 11):
            cod_curso = str(input("\nCódigo do Curso: "))
            curso = sistema.buscar_curso(cod_curso)
            if (curso):
                curso.exibir_info()
                continue
            print("\nCURSO NÃO ENCONTRADO!")

        # Gerência Turma
        elif (op == 12):
            cod_turma = str(input("\nCódigo da Turma: "))
            if (sistema.buscar_turma(cod_turma)):
                print("\nTURMA JÁ CADASTRADA! (CÓDIGO)")
                continue
            
            cod_curso = str(input("Código do Curso: "))
            curso = sistema.buscar_curso(cod_curso)
            if (curso is None):
                print("\nCURSO NÃO ENCONTRADO!")
                continue

            if (sistema.add_turma(cod_turma, curso)):
                print("\nTURMA ADICIONADA COM SUCESSO!")
                sistema.salvar_turma()
                continue
            print("\nERRO AO ADICIONAR TURMA!")

        elif (op == 13):
            cod_turma = str(input("\nCódigo da Turma: "))

            turma = sistema.buscar_turma(cod_turma)
            if (turma):
                if (sistema.rem_turma(turma)):
                    print("\nTURMA REMOVIDA COM SUCESSO!")
                    sistema.salvar_turma()
                    continue
                print("\nERRO AO REMOVER A TURMA!")
                continue
            print("\nTURMA NÃO ENCONTRADA!")

        elif (op == 14):
            cpf_aluno = str(input("\nCPF do Aluno: "))
            if (not sistema.iscpf(cpf_aluno)):
                print("\nCPF INVÁLIDO!")
                continue

            from aluno import Aluno
            aluno = sistema.buscar_usuario(cpf_aluno)
            if (not isinstance(aluno, Aluno)):
                print("\nALUNO NÃO ENCONTRADO!")
                continue
            
            cod_turma = str(input("Código da Turma: "))
            turma = sistema.buscar_turma(cod_turma)
            if (turma is None):
                print("\nTURMA NÃO ENCONTRADA!")
                continue

            alunointurma = False
            for a in turma.alunos:
                if (aluno.cpf == a.cpf):
                    alunointurma = True
                    break

            if (alunointurma):
                print("\nALUNO JÁ ESTÁ NA TURMA!")
                continue

            if (sistema.add_aluno_turma(aluno, turma)):
                print("\nALUNO ADICIONADO À TURMA COM SUCESSO!")
                sistema.salvar_turma()
                continue
            print("\nERRO AO ADICIONAR ALUNO À TURMA!")

        elif (op == 15):
            cpf_aluno = str(input("\nCPF do Aluno: "))
            if (not sistema.iscpf(cpf_aluno)):
                print("\nCPF INVÁLIDO!")
                continue

            from aluno import Aluno
            aluno = sistema.buscar_usuario(cpf_aluno)
            if (not isinstance(aluno, Aluno)):
                print("\nALUNO NÃO ENCONTRADO!")
                continue
            
            cod_turma = str(input("Código da Turma: "))
            turma = sistema.buscar_turma(cod_turma)
            if (turma is None):
                print("\nTURMA NÃO ENCONTRADA!")
                continue

            alunointurma = None
            for a in turma.alunos:
                if (aluno.cpf == a.cpf):
                    alunointurma = a
                    break
            
            if (alunointurma is None):
                print("\nALUNO NÃO ESTÁ NA TURMA!")
                continue

            if (sistema.rem_aluno_turma(alunointurma, turma)):
                print("\nALUNO REMOVIDO DA TURMA COM SUCESSO!")
                sistema.salvar_turma()
                continue
            print("\nERRO AO REMOVER O ALUNO DA TURMA!")

        elif (op == 16):
            cod_turma = str(input("\nCódigo da Turma: "))
            turma = sistema.buscar_turma(cod_turma)
            if (turma):
                turma.exibir_info()
                continue
            print("\nTURMA NÃO ENCONTRADA!")

        # Voltar
        elif (op == 17):
            return None
        else:
            print("\nOPÇÃO INVÁLIDA!")

def menu_prof(prof):
    while (True):
        sleep(1)
        print(f"\n== MENU - PROFESSOR ({prof.nome}) ==\n")
        op = int(input("1 - Lançar Nota\n2 - Exibir Curso\n3 - Exibir Disciplina\n4 - Exibir Informações\n5 - Sair\nO que deseja fazer? "))

        if (op == 1):
            cpf_aluno = str(input("\nCPF do Aluno: "))
            if (not sistema.iscpf(cpf_aluno)):
                print("\nCPF INVÁLIDO!")
                continue
            nota = float(input("Nota: "))

            aluno = sistema.buscar_usuario(cpf_aluno)
            if (aluno):
                if (sistema.lancar_nota(prof, aluno, nota)):
                    print(f"\nNOTA ADICIONADA AO ALUNO {aluno.nome}!")
                    sistema.salvar_usuario()
                    continue
                print("\nERRO AO ADICIONAR NOTA!")
                continue
            print("\nALUNO NÃO ENCONTRADO!")            
        elif (op == 2):
            cod_curso = str(input("\nCódigo do Curso: "))
            curso = sistema.buscar_curso(cod_curso)
            if (curso):
                curso.exibir_info()
                continue
            print("\nCURSO NÃO ENCONTRADO!")
        elif (op == 3):
            cod_disc = str(input("\nCódigo da Disciplina: "))
            disc = sistema.buscar_disc(cod_disc)
            if (disc):
                disc.exibir_info()
                continue
            print("\nDISCIPLINA NÃO ENCONTRADA!")
        elif (op == 4):
            prof.exibir_info()
        elif (op == 5):
            return None
        else:
            print("\nOPÇÃO INVÁLIDA!")

def menu_aluno(aluno):
    while (True):
        sleep(1)
        print(f"\n== MENU - ALUNO ({aluno.nome}) ==\n")
        op = int(input("1 - Ver Boletim\n2 - Exibir Curso\n3 - Exibir Disciplina\n4 - Exibir Informações\n5 - Sair\nO que deseja fazer? "))

        if (op == 1):
            aluno.ver_boletim()
        elif (op == 2):
            cod_curso = str(input("\nCódigo do Curso: "))
            curso = sistema.buscar_curso(cod_curso)
            if (curso):
                curso.exibir_info()
                continue
            print("\nCURSO NÃO ENCONTRADO!")
        elif (op == 3):
            cod_disc = str(input("\nCódigo da Disciplina: "))
            disc = sistema.buscar_disc(cod_disc)
            if (disc):
                disc.exibir_info()
                continue
            print("\nDISCIPLINA NÃO ENCONTRADA!")
        elif (op == 4):
            aluno.exibir_info()
        elif (op == 5):
            return None
        else:
            print("\nOPÇÃO INVÁLIDA!")


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
            op = str(input("\nDeseja seguir para o cadastro? [s/n] "))
            if (op.lower() == "s"):
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
        op = int(input("1 - Aluno\n2 - Professor\n3 - Administrador\n\n4 - Voltar\n\nVocê é um: "))

        if (op == 4):
            return None
        elif (op not in [1, 2, 3]):
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

        if (op == 1):
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
        
        elif (op == 2):
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
        
        elif (op == 3):
            return sistema.add_usuario("Adm", nome, cpf, email, senha)        

def main():
    to_login = False
    while (True):
        sleep(1)
        print("\n== SISTEMA ESCOLAR ==\n")
        op = int(input("1 - Cadastrar-se\n2 - Fazer Login\n3 - Sair\nO que deseja fazer? "))

        if (op == 1):
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
        elif (op == 2):
            to_login = True
        elif (op == 3):
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