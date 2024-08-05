# Modelagem de Dados de uma Biblioteca

+----------------+ +----------------+
| Usuario | | Livro |
+----------------+ +----------------+
| - nome | | - id |
| - telefone | | - titulo |
| - nacionalidade| | - editora |
+----------------+ | - generos |
| - autores |
| - maxRenovacoes|
| - renovacoes |
+----------------+
^
|
+----------------+ +------|---------+
| Emprestimo |------>| Exemplar |
+----------------+ +----------------+
| - usuario | | - id |
| - exemplar | | - emprestado |
| - dataEmprestimo| +----------------+
| - dataDevolucao|
| - estado |
+----------------+
^
|
+----------------+ +------|---------+
| Biblioteca |------>| Emprestimo |
+----------------+ +----------------+
| - usuarios |
| - livros |
| - emprestimos |
+----------------+

+----------------+
