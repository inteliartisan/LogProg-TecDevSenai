# Atividade 02
# 1 - Ao iniciar a execução do algoritmo, solicitar quantas pessoas serão cadastradas. 
# 2 - Ao escolher a opção 1, para cadastrar um novo usuário, sempre verificar se a estrutura homogênea possui alguma posição disponível para armazenar o novo usuário.
# 2.1 - Ainda na posição 1, após digitar os dados do usuário, adicioná-lo sempre a próxima posição disponível.

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

# Função para cadastrar usuário já com os tratamentos devidos e a melhoria da atividade de haver uma limitação no número de usuários cadastrados. 
    def cadastrarUsuarios(self):
        maxUsuarios = 3
        if len(self.__listaUsuarios) < maxUsuarios:
            nome = input('\nDigite o nome do usuário: ')
            idade = input('Digite a idade do usuário: ')
            try:
                pessoa = Pessoa(nome, idade)
                self.__listaUsuarios.append(pessoa)
                print('\nUsuário cadastrado com sucesso!')
                self.__salvarUsuarios()
            except ValueError as e:
                print(f'Erro ao cadastrar: {e}')
        else:
            print(f'Limite máximo de usuários atingido: {maxUsuarios}.')

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

# Execução do looping.
    def executar(self):
        while True:
            print('''
\nMenu:\n
1. Para cadastrar usuário
2. Para listar os usuários
3. Para buscar um usuário pelo nome
4. Para sair do sistema
                  ''')
            user = input('\nDigite a opção desejada: ')
            if user == '1':
                self.cadastrarUsuarios()
            elif user == '2':
                self.listarUsuarios()
            elif user == '3':
                self.buscarUsuarios()
            elif user == '4':
                break
            else:
                print('\nOpção Inválida')

if __name__ == "__main__":
    app = Usuarios()
    app.executar()