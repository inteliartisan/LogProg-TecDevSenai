
# Atividade:

# 1 - Implementar uma repetição que solicite as informações do usuário até que seja informado a opção "c".
# 2 - A cada repetição, apresentar o menu com as seguintes opções:
# a) Cadastrar novo usuário: Nome e Idade
# b) Listar todos os usuários cadastrados
# c) Sair do sistema

# Melhorias:

# O código importa a biblioteca "json" e "os" para possibilitar a emissão de relatório.
import json
import os

# O código será desenvolvido com o paradigma de programação orientada a objetos já com os tratamentos devidos. 
class Pessoa:
    def __init__(self, nome, idade):
        if not nome:
            raise ValueError("Nome não pode ser Vazio")
        if not str(idade).isdigit() or int(idade)<0:
            raise ValueError("Idade deve ser um número inteiro não negativo.")
        
# Armazena o valor de "nome" como atributo privado __nome da instância da classe e no caso de idade também converte para inteiro.
        self.__nome = nome
        self.__idade = int(idade)

# Torna possível a leitura pelo programa do método (função) "def nome" como atributo "self.__nome", mantendo o encapsulamento. 
    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    
# Imprime a função através de string
    def __str__(self):
        return f'Nome: {self.__nome}, Idade: {self.__idade}'
    
# Antecipa o salvamento e carregamento dos dados de forma estruturada pensando no formato "json". O primeiro transforma o objeto "pessoa" em um dicionário (salva) e o segundo recebe o dicionário e retorna o objeto "pessoa" (carrega).
    def to_dict(self):
        return {'nome': self.__nome, 'idade': self.__idade}
    @staticmethod
    def from_dict(dados):
        return Pessoa(dados['nome'], dados['idade'])
    
class Usuarios: 
    def __init__(self):
        self.__listaUsuarios = []
        self.__carregarUsuarios()

# Função para cadastrar usuário já com os tratamentos devidos.
    def cadastrarUsuarios(self):
        nome = input('\nDigite o nome do usuário: ')
        idade = input('\nDigite a idade do usuário: ')
        try:
            pessoa = Pessoa(nome, idade)
            self.__listaUsuarios.append(pessoa)
            print('\nUsuário cadastrado com sucesso')
            self.__salvarUsuarios()
        except ValueError as e:
            print(f'Erro ao cadastrar: {e}')

# Função para listar usuários.
    def listarUsuarios(self):
        if not self.__listaUsuarios:
            print(f'\nNão há usuários cadastrados')
        else:
            print('\nOs usuários cadastrados são:\n')
            for i in self.__listaUsuarios:
                print(i)

# Função para salvar usuários no formato "json".
    def __salvarUsuarios(self):
        with open('usuarios.json', 'w', encoding='utf-8') as arquivo:
            json.dump([p.to_dict() for p in self.__listaUsuarios], arquivo, ensure_ascii=False, indent=2)

# Função para carregar usuários no formato "json". 
    def __carregarUsuarios(self):
        if os.path.exists('usuarios.json'):
            with open('usuarios.json', 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                self.__listaUsuarios = [Pessoa.from_dict(p) for p in dados]

# Execução do código
    def executar(self):
        while True:
            print('''\n Menu:\n
          1. Para cadastrar usuário
          2. Para listar os usuários
          3. Para sair do sistema''')
            
            opcao = input('\nDigite a opção desejada: ')
            if opcao == '1':
                self.cadastrarUsuarios()
            elif opcao == '2':
                self.listarUsuarios()
            elif opcao == '3':
                break
            else:
                print('\nOpção Inválida')

if __name__ == "__main__":
    app = Usuarios()
    app.executar()









        
            


    









          
          
          
          
          
          





    


