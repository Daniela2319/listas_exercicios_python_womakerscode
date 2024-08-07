from models.usuario import Usuario
from models.livro import Livro
from models.emprestimo import Emprestimo


class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.livros = []
        self.emprestimos = []

    def adicionar_usuario(self, usuario):
        try:
            self.usuarios.append(usuario)
            print(f"Usuário {usuario.nome} adicionado com sucesso.")
        except Exception as e:
            print(f"Erro ao adicionar usuário: {e}")

    def adicionar_livro(self, livro):
        try:
            self.livros.append(livro)
            print(f"Livro {livro.titulo} adicionado com sucesso.")
        except Exception as e:
            print(f"Erro ao adicionar livro: {e}")

    def registrar_emprestimo(self, emprestimo):
        try:
            if emprestimo.exemplar.emprestado:
                raise Exception("Exemplar já está emprestado.")
            self.emprestimos.append(emprestimo)
            emprestimo.exemplar.emprestar()
            print(
                f"Empréstimo do exemplar {emprestimo.exemplar.id} registrado com sucesso."
            )
        except Exception as e:
            print(f"Erro ao registrar empréstimo: {e}")

    def devolver_emprestimo(self, emprestimo):
        try:
            if emprestimo.estado != "emprestado":
                raise Exception("Exemplar não está emprestado.")
            emprestimo.devolver()
            print(
                f"Empréstimo do exemplar {emprestimo.exemplar.id} devolvido com sucesso."
            )
        except Exception as e:
            print(f"Erro ao devolver empréstimo: {e}")
