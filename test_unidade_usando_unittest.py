import unittest
from livro import Livro, Exemplar
from exceptions import *

'''
todo teste deve começar com Test ou Teste no nome da classe e dos métodos de teste (OBS :  unittest)
'''

class TesteLivro(unittest.TestCase):

    def test_criar_novo_livro(self):
        novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1976)
        # o primeiro parametro é o que eu envio como resposta, o segundo é o que é esperado como resposta
        self.assertEqual(novo_livro.titulo, "The Art of Software Testing")  # add assertion here
        self.assertEqual(novo_livro.autores, ["John Glenford Myers", "Corey Sandler", "Tom Badget"])
        self.assertEqual(novo_livro.ano_publicacao, 1976)

    def test_criar_exemplar_com_livro_incorreto(self):
        exemplar = Exemplar(1, 10, 1, 2023, "Editora")
        with self.assertRaises(TipoIncorretoException):
            exemplar.livro = 2

    def teste_criar_livro_com_titulo_errado(self):
        livro_com_titulo_errado = Livro(1,["jonatas", "fernandes"], 1998)
        with self.assertRaises(TipoIncorretoException):
            livro_com_titulo_errado.titulo = 4

    def teste_criar_exemplar_correto(self):
        novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1976)
        meu_novo_exemplar = Exemplar(novo_livro, 10, 2, 2024, "Editora nova")
        self.assertEqual(meu_novo_exemplar.livro, novo_livro)
        self.assertEqual(meu_novo_exemplar.quantidade, 10)
        self.assertEqual(meu_novo_exemplar.edicao, 2)
        self.assertEqual(meu_novo_exemplar.ano, 2024)
        self.assertEqual(meu_novo_exemplar.editora, "Editora nova")

    def teste_remocao_exemplar(self):
        livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1976)
        meu_novo_exemplar = Exemplar(livro, -1, 2, 2024, "Editora nova")
        with self.assertRaises(QuantidadeInvalidaException):
            meu_novo_exemplar.quantidade = -1


    def teste_tipo_dos_autores_do_livro(self):
        novo_livro = Livro("The Art of Software Testing",[], 1976)
        with self.assertRaises(ValorVazioException):
            novo_livro.autores = []

    def teste_ano_lancamento_errado_do_exemplar_(self):
        novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1990)
        meu_novo_exemplar = Exemplar(novo_livro, 10, 2, 1980, "Editora nova")
        with self.assertRaises(AnoInvalidoException):
            meu_novo_exemplar.ano = 1980

    def teste_edicao_do_exemplar_com_valor_errado(self):
        novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1990)
        meu_novo_exemplar = Exemplar(novo_livro, 10, 0, 1990, "Editora nova")
        with self.assertRaises(QuantidadeInvalidaException):
            meu_novo_exemplar.edicao = 0

    def teste_editora_exemplar_vazia(self):
        novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1990)
        meu_novo_exemplar = Exemplar(novo_livro, 10, 4, 1990, " ")
        with self.assertRaises(ValorVazioException):
            meu_novo_exemplar.editora = " "

    def teste_tipo_editora_exemplar(self):
        novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1990)
        meu_novo_exemplar = Exemplar(novo_livro, 10, 5, 1990, 1)
        with self.assertRaises(TipoIncorretoException):
            meu_novo_exemplar.editora = 1

    def teste_adicionar_quantidade_invalida_exemplar(self):
        novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], 1990)
        meu_novo_exemplar = Exemplar(novo_livro, -1, 6, 1990, "oi teste")
        with self.assertRaises(QuantidadeInvalidaException):
            meu_novo_exemplar.adicionar_exemplares(meu_novo_exemplar.quantidade)

    def teste_publicar_livro_com_data_errada(self):
        novo_livro = Livro("The Art of Software Testing", ["John Glenford Myers", "Corey Sandler", "Tom Badget"], -1)
        with self.assertRaises(AnoInvalidoException):
            novo_livro.ano_publicacao = -1

# if __name__ == '__main__':
#     unittest.main()
