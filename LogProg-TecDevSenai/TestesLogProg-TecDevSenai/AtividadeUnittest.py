# Desenvolvimento de um ambiente de teste para a atividade lógica 08 utilizando unittest. 

# 1 - Utilizar o módulo padrão do python unittest para criar e rodar testes automatizados. 
# 2 - Utilizar o patch do unittest.mock para simular entradas e saídas sem interação manual.
# 3 - Importar as classes "Pessoas" e "Usuarios" do módulo principal (AtividadeLogica08).
# 4 - Criar uma classe de testes unitários herdando de unittest.TestCase.
# 5 - Utilizar mock_input e mock_print para verificar se as mensagens foram realmente impressas. 
# 6 - Utilizar @patch('builtins.input') para substituir a função input temporariamente retornando valores pré-definidos.

import unittest 
from unittest.mock import patch
from ..AtividadeLogica08 import Pessoa, Usuarios

class teste_pessoa(unittest.TestCase):
    
    def test_cadastro_valido(self):
        pessoa = Pessoa('João', 30)
        self.assertEqual(pessoa.nome, 'João')
        self.assertEqual(pessoa.idade, 30)

    def test_cadastro_vazio(self):
        with self.assertRaises(ValueError):
            Pessoa('', 25)

    def test_idade_invalida(self):
        with self.assertRaises(ValueError):
            Pessoa('Maria', 'abc')
        with self.assertRaises(ValueError):
            Pessoa('José', -5)

class teste_usuarios(unittest.TestCase):

    def setUp(self): # Garante que os testes comecem com uma lista vazia, ignorando os dados no usuarios.json. 
        self.usuarios = Usuarios()
        self.usuarios._Usuarios__lista_usuarios = []  

    @patch('builtins.input', side_effect=['Carlos', '22'])
    def test_cadastrar_usuario(self, mock_input):
        self.usuarios.cadastrar_usuarios()
        self.assertEqual(len(self.usuarios._Usuarios__lista_usuarios), 1)
        self.assertEqual(self.usuarios._Usuarios__lista_usuarios[0].nome, 'Carlos')

    @patch('builtins.input', return_value = 'Carlos')
    def test_remover_usuario(self, mock_input):
        self.usuarios._Usuarios__lista_usuarios = [Pessoa("Carlos", 22)]
        self.usuarios.remover_usuario()
        self.assertEqual(len(self.usuarios._Usuarios__lista_usuarios), 0, 'Carlos foi removido com sucesso!')

    def test_remover_usuario_pilha(self):
        self.usuarios._Usuarios__lista_usuarios = [Pessoa("Ana", 25)]
        self.usuarios.remover_usuario_pilha()
        self.assertEqual(len(self.usuarios._Usuarios__lista_usuarios), 0)

    def test_limpar_usuarios(self):
        self.usuarios._Usuarios__lista_usuarios = [Pessoa("João", 30), Pessoa("Maria", 28)]
        self.usuarios.limpar_usuarios()
        self.assertEqual(len(self.usuarios._Usuarios__lista_usuarios), 0)

    def test_ordenar_por_idade(self):
        self.usuarios._Usuarios__lista_usuarios = [
            Pessoa('Joana', 40),
            Pessoa('Bruno', 25),
            Pessoa('Ana', 30)
        ]
        self.usuarios.ordenar_por_idade()  
        nomes_ordenados = [p.nome for p in self.usuarios._Usuarios__lista_usuarios]
        self.assertEqual(nomes_ordenados, ['Bruno', 'Ana', 'Joana'])

    @patch('builtins.input', return_value = 'Bruno')
    def test_buscar_usuarios_encontrado(self, mock_input):
        self.usuarios._Usuarios__lista_usuarios = [Pessoa('Bruno', 25)]
        with patch('builtins.print') as mock_print:
            self.usuarios.buscar_usuarios()
            mock_print.assert_any_call('Posição: 1, Nome: Bruno, Idade: 25')

    @patch('builtins.input', return_value = 'inexistente')
    @patch('builtins.print')
    def test_buscar_usuarios_nao_encontrados(self, mock_print, mock_input):
        self.usuarios._Usuarios__lista_usuarios = [Pessoa('Carlos', 22)]
        self.usuarios.buscar_usuarios()
        mock_print.assert_any_call('\nUsuário não registrado')

if __name__ == '__main__': # Permite rodas os testes com: python -m unittest caminho/para/o/arquivo.py
    unittest.main()

    


        

