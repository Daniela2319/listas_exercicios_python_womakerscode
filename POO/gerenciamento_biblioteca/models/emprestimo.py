from datetime import datetime


class Emprestimo:
    def __init__(self, usuario, exemplar):
        self.usuario = usuario
        self.exemplar = exemplar
        self.data_emprestimo = datetime.now()
        self.data_devolucao = datetime.now().hour
        self.estado = "emprestado"

    def devolver(self):
        self.exemplar.devolver()
        self.data_devolucao = datetime.now()
        self.data_devolucao.strftime("%H:%M:%S.%f")
        self.estado = "devolvido"
