# Classe base Usuario
class Usuario:
    def __init__(self, nome: str, cpf: str, email: str, senha: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__senha = senha

    @property 
    def nome(self):
        return  self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def email(self):
        return self.__email
    
    @property
    def senha(self):
        return self.__senha
    
    def exibir_info(self):
        print(f"Nome: {self.nome}\nCPF: {self.cpf}\nEmail: {self.email}\nSenha: {self.senha}")