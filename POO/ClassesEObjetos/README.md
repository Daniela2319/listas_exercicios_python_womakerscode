# Modelagem de Dados de uma Biblioteca

```mermaid
classDiagram
    class Pessoa {
        -nome: str
        -telefone: str
        -nacionalidade: str
        +obter_informacoes(): str
    }

    class Usuario {
        +obter_informacoes(): str
    }
    Pessoa <|-- Usuario

    class Item {
        -id: int
        -emprestado: bool
        +emprestar(): void
        +devolver(): void
    }

    class Exemplar {
    }
    Item <|-- Exemplar

    class Livro {
        -id: int
        -titulo: str
        -editora: str
        -generos: list~str~
        -autores: list~str~
        -maxRenovacoes: int
        -renovacoes: int
        -exemplares: list~Exemplar~
        +adicionar_exemplar(exemplar: Exemplar): void
        +remover_exemplar(exemplar: Exemplar): void
    }

    class Emprestimo {
        -usuario: Usuario
        -exemplar: Exemplar
        -data_emprestimo: datetime
        -data_devolucao: datetime
        -estado: str
        +devolver(): void
    }

    class Biblioteca {
        -usuarios: list~Usuario~
        -livros: list~Livro~
        -emprestimos: list~Emprestimo~
        +adicionar_usuario(usuario: Usuario): void
        +adicionar_livro(livro: Livro): void
        +registrar_emprestimo(emprestimo: Emprestimo): void
        +devolver_emprestimo(emprestimo: Emprestimo): void
    }

    Usuario --> Emprestimo : "realiza"
    Emprestimo --> Exemplar : "refere-se a"
    Exemplar --> Livro : "pertence a"
    Biblioteca --> Usuario : "gerencia"
    Biblioteca --> Livro : "gerencia"
    Biblioteca --> Emprestimo : "gerencia"

```
