# Desenvolvimento de um ambiente de teste para a atividade lógica 08 utilizando pytest. 

# 1 - Instalar a biblioteca pytest como alternativa a unittest (nativa do python).
# 2 - Expor requirements.txt como boas práticas. 
# 3 - Utilizar o módulo padrão do python pytest para criar e rodar testes automatizados. 
# 2 - Importar as classes "Pessoas" e "Usuarios" do módulo principal (AtividadeLogica08).
# 3 - Utilizar monkeypatch para simular entradas.
# 4 - Utilizar capsys para verificar a saída (print).

import pytest
from LogProg_TecDevSenai.AtividadeLogica08 import Pessoa, Usuarios

def test_cadastro_valido():
    pessoa = Pessoa("João", 30)
    assert pessoa.nome == "João"
    assert pessoa.idade == 30

def test_cadastro_vazio():
    with pytest.raises(ValueError):
        Pessoa("", 25)

def test_idade_invalida():
    with pytest.raises(ValueError):
        Pessoa("Maria", "abc")
    with pytest.raises(ValueError):
        Pessoa("José", -5)

@pytest.fixture
def usuarios_vazios():
    usuarios = Usuarios()
    usuarios._Usuarios__lista_usuarios = []
    return usuarios

def test_cadastrar_usuario(monkeypatch, usuarios_vazios):
    inputs = iter(["Carlos", "22"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    usuarios_vazios.cadastrar_usuarios()
    assert len(usuarios_vazios._Usuarios__lista_usuarios) == 1
    assert usuarios_vazios._Usuarios__lista_usuarios[0].nome == "Carlos"
    assert usuarios_vazios._Usuarios__lista_usuarios[0].idade == 22

def test_remover_usuario(monkeypatch, usuarios_vazios):
    usuarios_vazios._Usuarios__lista_usuarios = [Pessoa("Carlos", 22)]
    monkeypatch.setattr("builtins.input", lambda _: "Carlos")
    usuarios_vazios.remover_usuario()
    assert len(usuarios_vazios._Usuarios__lista_usuarios) == 0

def test_remover_usuario_pilha(usuarios_vazios):
    usuarios_vazios._Usuarios__lista_usuarios = [Pessoa("Ana", 25)]
    usuarios_vazios.remover_usuario_pilha()
    assert len(usuarios_vazios._Usuarios__lista_usuarios) == 0

def test_limpar_usuarios(usuarios_vazios):
    usuarios_vazios._Usuarios__lista_usuarios = [Pessoa("João", 30), Pessoa("Maria", 28)]
    usuarios_vazios.limpar_usuarios()
    assert len(usuarios_vazios._Usuarios__lista_usuarios) == 0

def test_ordenar_por_idade(usuarios_vazios):
    usuarios_vazios._Usuarios__lista_usuarios = [
        Pessoa("Joana", 40),
        Pessoa("Bruno", 25),
        Pessoa("Ana", 30)
    ]
    usuarios_vazios.ordenar_por_idade()
    nomes_ordenados = [p.nome for p in usuarios_vazios._Usuarios__lista_usuarios]
    assert nomes_ordenados == ["Bruno", "Ana", "Joana"]

def test_buscar_usuarios_encontrado(monkeypatch, capsys, usuarios_vazios):
    usuarios_vazios._Usuarios__lista_usuarios = [Pessoa("Bruno", 25)]
    monkeypatch.setattr("builtins.input", lambda _: "Bruno")
    usuarios_vazios.buscar_usuarios()
    captured = capsys.readouterr()
    assert "Nome: Bruno" in captured.out

def test_buscar_usuarios_nao_encontrados(monkeypatch, capsys, usuarios_vazios):
    usuarios_vazios._Usuarios__lista_usuarios = [Pessoa("Carlos", 22)]
    monkeypatch.setattr("builtins.input", lambda _: "inexistente")
    usuarios_vazios.buscar_usuarios()
    captured = capsys.readouterr()
    assert "Usuário não registrado" in captured.out
