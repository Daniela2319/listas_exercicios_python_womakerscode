from models.pessoa import Pessoa


class Usuario(Pessoa):
    def __init__(self, nome, telefone, nacionalidade):
        super().__init__(nome, telefone, nacionalidade)

    def obter_informacoes(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Nacionalidade: {self.nacionalidade}"
