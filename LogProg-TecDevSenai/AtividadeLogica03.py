# Atividade 03
# Implementar uma função que receba por parâmetro o nome de uma pessoa.
# 1 - Caso encontre deverá apresentar o nome e a idade da pessoa e retornar sua posição.
# 1.1 - Caso encontrário deverá retornar a mensagem de pessoa não registrada. 

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
    
# Função para buscar um usuário pelo nome evidenciando a posição, o nome e a idade e caso não encontrado, emitindo a mensagem "usuário não registrado".
    def buscarUsuarios(self):
        usuario = False
        buscaUsuario = input('\nDigite o nome do usuário que deseja buscar: ')
        for i, pessoa in enumerate(self.__listaUsuarios):
            if pessoa.nome == buscaUsuario:
                print(f'Posição: {1 + i}, Nome: {pessoa.nome}, Idade: {pessoa.idade}')
            usuario = True
            if not usuario:
                print('\nUsuário não registrado')

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