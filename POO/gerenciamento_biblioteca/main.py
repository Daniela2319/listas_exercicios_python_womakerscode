from models.biblioteca import Biblioteca
from models.usuario import Usuario
from models.livro import Livro
from models.exemplar import Exemplar
from models.emprestimo import Emprestimo


def titulo(txt):
    print("-=" * 30)
    print(txt)
    # print("-=" * 30)


# Criação de instâncias de exemplo
biblioteca = Biblioteca()

# Adicionar usuários
titulo("Adicionar usuário")
usuario1 = Usuario("Daniela", "9999-9999", "Brasileira")
biblioteca.adicionar_usuario(usuario1)
usuario2 = Usuario("Frank", "6666-6666", "EUA")
biblioteca.adicionar_usuario(usuario2)
usuario3 = Usuario("Valdemar", "9999-9999", "Chines")
biblioteca.adicionar_usuario(usuario3)
usuario1.obter_informacoes()

# Adicionar livros e exemplares

titulo("Adicionar livros e exemplares")
livro1 = Livro(
    1, "O Senhor dos Anéis", "HarperCollins", ["Fantasia"], ["J.R.R. Tolkien"], 2
)
livro2 = Livro(
    2,
    "Orientação a Objeto na Prática",
    "Ciência Moderna",
    ["Educação"],
    ["Caíque Cardoso"],
    0,
)


exemplar1 = Exemplar(1)
exemplar2 = Exemplar(2)


livro1.adicionar_exemplar(exemplar1)
livro2.adicionar_exemplar(exemplar2)
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)


# Realizar empréstimos
titulo("Realizar empréstimos")
emprestimo1 = Emprestimo(usuario1, exemplar1)
biblioteca.registrar_emprestimo(emprestimo1)
emprestimo2 = Emprestimo(usuario2, exemplar2)
biblioteca.registrar_emprestimo(emprestimo2)

print(
    f"Usuário {emprestimo1.usuario.nome} emprestou o exemplar {emprestimo1.exemplar.id} do livro {livro1.titulo}"
)
print(
    f"Usuário {emprestimo2.usuario.nome} emprestou o exemplar {emprestimo2.exemplar.id} do livro {livro2.titulo}"
)

# Devolver empréstimo
titulo("Devolver empréstimo")
biblioteca.devolver_emprestimo(emprestimo1)
print(
    f"Empréstimo do exemplar {emprestimo1.exemplar.id} foi devolvido em {emprestimo1.data_devolucao}"
)
