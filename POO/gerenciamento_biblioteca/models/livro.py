from models.exemplar import Exemplar


class Livro:
    def __init__(self, id, titulo, editora, generos, autores, max_renovacoes=0):
        self.id = id
        self.titulo = titulo
        self.editora = editora
        self.generos = generos
        self.autores = autores
        self.max_renovacoes = max_renovacoes
        self.renovacoes = 0
        self.exemplares = []

    def adicionar_exemplar(self, exemplar):
        self.exemplares.append(exemplar)

    def remover_exemplar(self, exemplar):
        self.exemplares.remove(exemplar)
