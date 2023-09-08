import pytest
from _pytest.main import Failed

from livro import Livro, Exemplar
from exceptions import *

def test_criar_novo_livro():
    novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1976)

    assert novo_livro.titulo == "The Art of Software Testing"
    assert novo_livro.autores == ["John Glenford Myers", "Corey Sandler", "Tom Badget"]
    assert novo_livro.ano_publicacao == 1976

def test_criar_Exemplar_com_tipo_incorreto():
    with pytest.raises(TipoIncorretoException):
        exemplar = Exemplar(1, 10, 1, 2023, "Editora")
        exemplar.livro = 2

def teste_criar_exemplar_com_livro_string():
    exemplar = Exemplar(" ", 15, 1, 2023, "nova editora")
    with pytest.raises(TipoIncorretoException):
        exemplar.livro = " "

def test_livro_sem_ano_de_publicacao():
    novo_livro = Livro("meu novo livro", ["John Glenford Myers", "Corey Sandler", "Tom Badget"])
    assert novo_livro.titulo == "meu novo livro"
    assert novo_livro.autores == ["John Glenford Myers", "Corey Sandler", "Tom Badget"]
    assert novo_livro.autores != None

def test_criar_livro_com_autores_em_formato_de_dicionario():
    novo_livro = Livro("meu novo livro", {"John : Glenford Myers", "Corey : Sandler", "Tom : Badget"}, 1924)

    assert novo_livro.titulo == "meu novo livro"
    assert novo_livro.autores == ["John : Glenford Myers", "Corey : Sandler", "Tom : Badget"]
    assert novo_livro.ano_publicacao == 1924

def test_exemplar_com_edicao_em_float():
    exemplar = Exemplar(1, 10, 1.5, 2023, "Editora")
    assert exemplar.edicao != int

def test_remover_exemplar_inexistente():
    with pytest.raises(ValorInexistenteException):
        novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1976)
        exemplar = Exemplar(novo_livro, 10, 1, 2023, "Editora")
        with pytest.raises(ValorInexistenteException):
            exemplar.remover_exemplares(10, exemplar)
        '''
            o teste acima verifica se o exemplar existe. Ele lança a execessão mas falha, pois o exemplar existe
        '''

def test_remover_exemplar_existente():
    novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1976)
    exemplar = Exemplar(novo_livro, 10, 1, 2023, "Editora")
    assert exemplar.remover_exemplares(exemplar.quantidade, exemplar) != False


def test_adicionar_exemplar_com_quantidade_negativa():
    novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1976)
    exemplar = Exemplar(novo_livro, -3, 1, 2023, "Editora")
    with pytest.raises(QuantidadeInvalidaException):
        exemplar.adicionar_exemplares(-3,novo_livro)

def test_adicionar_exemplar_sem_livro():
    exemplar = Exemplar(None, 10, 1, 2023, "Editora")
    with pytest.raises(ValorInexistenteException):
        exemplar.adicionar_exemplares(10, exemplar.livro)
