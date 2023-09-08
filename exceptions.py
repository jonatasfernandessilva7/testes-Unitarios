class TipoIncorretoException(BaseException):

    def __int__(self, mensagem):
        self._mensagem = mensagem

    def __str__(self):
        return self._mensagem


class AnoInvalidoException(BaseException):

    def __int__(self, mensagem):
        self._mensagem = mensagem

    def __str__(self):
        return self._mensagem


class QuantidadeInvalidaException(BaseException):

    def __int__(self, mensagem):
        self._mensagem = mensagem

    def __str__(self):
        return self._mensagem


class ValorVazioException(BaseException):

    def __init__(self, mensagem):
        self._mensagem = mensagem

    def __str__(self):
        return self._mensagem


class ValorInexistenteException(BaseException):

    def __init__(self, mensagem):
        self._mensagem = mensagem

    def __str__(self):
        return self._mensagem