from models.biblioteca import Biblioteca
from models.usuario import Usuario
from models.livro import Livro
from models.exemplar import Exemplar
from models.emprestimo import Emprestimo

# Criação de instâncias de exemplo
biblioteca = Biblioteca()

# Adicionar usuários
usuario1 = Usuario("Daniela", "9999-9999", "Brasileira")
usuario1.obter_informacoes()
biblioteca.adicionar_usuario(usuario1)

# Adicionar livros e exemplares
livro1 = Livro(
    1, "O Senhor dos Anéis", "HarperCollins", ["Fantasia"], ["J.R.R. Tolkien"], 2
)
exemplar1 = Exemplar(1)
exemplar2 = Exemplar(2)
livro1.adicionar_exemplar(exemplar1)
livro1.adicionar_exemplar(exemplar2)
biblioteca.adicionar_livro(livro1)

# Realizar empréstimos
emprestimo1 = Emprestimo(usuario1, exemplar1)
biblioteca.registrar_emprestimo(emprestimo1)

print(
    f"Usuário {emprestimo1.usuario.nome} emprestou o exemplar {emprestimo1.exemplar.id} do livro {livro1.titulo}"
)

# Devolver empréstimo
biblioteca.devolver_emprestimo(emprestimo1)
print(
    f"Empréstimo do exemplar {emprestimo1.exemplar.id} foi devolvido em {emprestimo1.data_devolucao}"
)
