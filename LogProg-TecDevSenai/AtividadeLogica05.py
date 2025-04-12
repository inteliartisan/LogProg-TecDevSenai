# Atividade 05

# Promover a melhoria do código a partir do conceito de pilha (FILO).
# 1 - A estrutura deverá ter 20 posições
# 2 - O elemento adicionado deverá estar no topo da pilha. 
# 3 - Implementa a ação de remover o último elemento da pilha. 

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
        self.__lista_usuarios = []
        self.__carregar_usuarios()

# Função para cadastrar usuário já com os tratamentos devidos e a melhoria da atividade de haver uma limitação no número de usuários cadastrados. 
    def cadastrar_usuarios(self):
        maxUsuarios = 20
        if len(self.__lista_usuarios) < maxUsuarios:
            nome = input('\nDigite o nome do usuário: ')
            idade = input('Digite a idade do usuário: ')
            try:
                pessoa = Pessoa(nome, idade)
                self.__lista_usuarios.insert(0, pessoa)
                print('\nUsuário cadastrado com sucesso!')
                self.__salvar_usuarios()
            except ValueError as e:
                print(f'Erro ao cadastrar: {e}')
        else:
            print(f'Limite máximo de usuários atingido: {maxUsuarios}.')

# Função para listar usuários.
    def listar_usuarios(self):
        if not self.__lista_usuarios:
            print(f'\nNão há usuários cadastrados')
        else:
            print('\nOs usuários cadastrados são:\n')
            for i in self.__lista_usuarios:
                print(i)
    
# Função para buscar um usuário pelo nome evidenciando a posição, o nome e a idade e caso não encontrado, emitindo a mensagem "usuário não registrado".
    def buscar_usuarios(self):
        usuario = False
        buscaUsuario = input('\nDigite o nome do usuário que deseja buscar: ')
        for i, pessoa in enumerate(self.__lista_usuarios):
            if pessoa.nome == buscaUsuario:
                print(f'Posição: {1 + i}, Nome: {pessoa.nome}, Idade: {pessoa.idade}')
            usuario = True
            if not usuario:
                print('\nUsuário não registrado')

# Função para remover um usuário pelo nome da pessoa da estrutura homogênea.
    def remover_usuario(self):
        removeUsuario = input('\nInforme o nome do usuário que deseja remover: ')
        for i, pessoa in enumerate(self.__lista_usuarios):
            if pessoa.nome == removeUsuario:
                self.__lista_usuarios.pop(i)
                print(f'{removeUsuario} foi removido com sucesso!')
                self.__salvar_usuarios() #atualiza o arquivo "json".
                break
            else:
                print(f'Usuário não encontrado.')

# Função para remover o último usuário da pilha.
    def remover_usuario_pilha(self):
        usuarioRemovido = self.__lista_usuarios.pop()
        print(f'{usuarioRemovido.nome} foi removido com sucesso!')
        self.__salvar_usuarios() #atualiza o arquivo "json".
                
# Função para salvar usuários no formato "json".
    def __salvar_usuarios(self):
        with open('usuarios.json', 'w', encoding='utf-8') as arquivo:
            json.dump([p.to_dict() for p in self.__lista_usuarios], arquivo, ensure_ascii=False, indent=2)

# Função para carregar usuários no formato "json". 
    def __carregar_usuarios(self):
        if os.path.exists('usuarios.json'):
            with open('usuarios.json', 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                self.__lista_usuarios = [Pessoa.from_dict(p) for p in dados]

# Execução do looping.
    def executar(self):
        while True:
            print('''
Menu:\n
1. Para cadastrar usuário
2. Para listar os usuários cadastrados
3. Para buscar um usuário pelo nome
4. Para remover um usuário pelo nome
5. Para remover o último usuário na lista de cadastro
6. Para sair do sistema
                  ''')
            user = input('\nDigite a opção desejada: ')
            if user == '1':
                self.cadastrar_usuarios()
            elif user == '2':
                self.listar_usuarios()
            elif user == '3':
                self.buscar_usuarios()
            elif user == '4':
                self.remover_usuario()
            elif user == '5':
                self.remover_usuario_pilha()
            elif user == '6':
                break
            else:
                print('\nOpção Inválida')

if __name__ == "__main__":
    app = Usuarios()
    app.executar() 
