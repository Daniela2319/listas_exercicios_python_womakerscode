class Item:
    def __init__(self, id):
        self.id = id
        self.emprestado = False

    def emprestar(self):
        self.emprestado = True

    def devolver(self):
        self.emprestado = False
