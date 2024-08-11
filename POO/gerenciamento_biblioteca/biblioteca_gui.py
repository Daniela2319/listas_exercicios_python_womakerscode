import tkinter as tk
from tkinter import messagebox
from models.biblioteca import Biblioteca
from models.usuario import Usuario
from models.livro import Livro
from models.exemplar import Exemplar
from models.emprestimo import Emprestimo

# Inicialização da Biblioteca
biblioteca = Biblioteca()


def adicionar_usuario():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    nacionalidade = entry_nacionalidade.get()
    if nome and telefone and nacionalidade:
        usuario = Usuario(nome, telefone, nacionalidade)
        biblioteca.adicionar_usuario(usuario)
        messagebox.showinfo("Sucesso", f"Usuário {nome} adicionado com sucesso!")
        entry_nome.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_nacionalidade.delete(0, tk.END)
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")


def adicionar_livro():
    id = entry_id_livro.get()
    titulo = entry_titulo.get()
    editora = entry_editora.get()
    generos = entry_generos.get().split(",")
    autores = entry_autores.get().split(",")
    if id and titulo and editora and generos and autores:
        livro = Livro(int(id), titulo, editora, generos, autores)
        exemplar = Exemplar(int(id))
        livro.adicionar_exemplar(exemplar)
        biblioteca.adicionar_livro(livro)
        messagebox.showinfo("Sucesso", f"Livro {titulo} adicionado com sucesso!")
        entry_id_livro.delete(0, tk.END)
        entry_titulo.delete(0, tk.END)
        entry_editora.delete(0, tk.END)
        entry_generos.delete(0, tk.END)
        entry_autores.delete(0, tk.END)
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")


def registrar_emprestimo():
    usuario_nome = entry_usuario_nome.get()
    livro_id = entry_livro_id.get()

    usuario = next((u for u in biblioteca.usuarios if u.nome == usuario_nome), None)
    livro = next((l for l in biblioteca.livros if l.id == int(livro_id)), None)

    if usuario and livro:
        exemplar = livro.exemplares[0]  # Assumindo que há um exemplar disponível
        emprestimo = Emprestimo(usuario, exemplar)
        biblioteca.registrar_emprestimo(emprestimo)
        messagebox.showinfo(
            "Sucesso", f"Empréstimo do livro {livro.titulo} realizado com sucesso!"
        )
    else:
        messagebox.showwarning("Erro", "Usuário ou Livro não encontrado.")


# Configuração da Janela Principal
root = tk.Tk()
root.title("Sistema de Biblioteca")
root.geometry("500x600")
root.configure(bg="#f0f0f0")

# Definindo fonte padrão maior
font_padrao = ("Arial", 14)

# Seção para Adicionar Usuário
frame_usuario = tk.Frame(root, bg="#f0f0f0")
frame_usuario.pack(pady=10, padx=20, fill="x")

tk.Label(frame_usuario, text="Nome:", font=font_padrao, bg="#f0f0f0").grid(
    row=0, column=0, sticky="w"
)
entry_nome = tk.Entry(frame_usuario, font=font_padrao)
entry_nome.grid(row=0, column=1, sticky="ew")

tk.Label(frame_usuario, text="Telefone:", font=font_padrao, bg="#f0f0f0").grid(
    row=1, column=0, sticky="w"
)
entry_telefone = tk.Entry(frame_usuario, font=font_padrao)
entry_telefone.grid(row=1, column=1, sticky="ew")

tk.Label(frame_usuario, text="Nacionalidade:", font=font_padrao, bg="#f0f0f0").grid(
    row=2, column=0, sticky="w"
)
entry_nacionalidade = tk.Entry(frame_usuario, font=font_padrao)
entry_nacionalidade.grid(row=2, column=1, sticky="ew")

btn_adicionar_usuario = tk.Button(
    frame_usuario,
    text="Adicionar Usuário",
    font=font_padrao,
    command=adicionar_usuario,
    bg="#4CAF50",
    fg="white",
)
btn_adicionar_usuario.grid(row=3, columnspan=2, pady=10, sticky="ew")

# Seção para Adicionar Livro
frame_livro = tk.Frame(root, bg="#f0f0f0")
frame_livro.pack(pady=10, padx=20, fill="x")

tk.Label(frame_livro, text="ID do Livro:", font=font_padrao, bg="#f0f0f0").grid(
    row=0, column=0, sticky="w"
)
entry_id_livro = tk.Entry(frame_livro, font=font_padrao)
entry_id_livro.grid(row=0, column=1, sticky="ew")

tk.Label(frame_livro, text="Título:", font=font_padrao, bg="#f0f0f0").grid(
    row=1, column=0, sticky="w"
)
entry_titulo = tk.Entry(frame_livro, font=font_padrao)
entry_titulo.grid(row=1, column=1, sticky="ew")

tk.Label(frame_livro, text="Editora:", font=font_padrao, bg="#f0f0f0").grid(
    row=2, column=0, sticky="w"
)
entry_editora = tk.Entry(frame_livro, font=font_padrao)
entry_editora.grid(row=2, column=1, sticky="ew")

tk.Label(
    frame_livro, text="Gêneros (separados por vírgula):", font=font_padrao, bg="#f0f0f0"
).grid(row=3, column=0, sticky="w")
entry_generos = tk.Entry(frame_livro, font=font_padrao)
entry_generos.grid(row=3, column=1, sticky="ew")

tk.Label(
    frame_livro, text="Autores (separados por vírgula):", font=font_padrao, bg="#f0f0f0"
).grid(row=4, column=0, sticky="w")
entry_autores = tk.Entry(frame_livro, font=font_padrao)
entry_autores.grid(row=4, column=1, sticky="ew")

btn_adicionar_livro = tk.Button(
    frame_livro,
    text="Adicionar Livro",
    font=font_padrao,
    command=adicionar_livro,
    bg="#4CAF50",
    fg="white",
)
btn_adicionar_livro.grid(row=5, columnspan=2, pady=10, sticky="ew")

# Seção para Registrar Empréstimo
frame_emprestimo = tk.Frame(root, bg="#f0f0f0")
frame_emprestimo.pack(pady=10, padx=20, fill="x")

tk.Label(
    frame_emprestimo, text="Nome do Usuário:", font=font_padrao, bg="#f0f0f0"
).grid(row=0, column=0, sticky="w")
entry_usuario_nome = tk.Entry(frame_emprestimo, font=font_padrao)
entry_usuario_nome.grid(row=0, column=1, sticky="ew")

tk.Label(frame_emprestimo, text="ID do Livro:", font=font_padrao, bg="#f0f0f0").grid(
    row=1, column=0, sticky="w"
)
entry_livro_id = tk.Entry(frame_emprestimo, font=font_padrao)
entry_livro_id.grid(row=1, column=1, sticky="ew")

btn_registrar_emprestimo = tk.Button(
    frame_emprestimo,
    text="Registrar Empréstimo",
    font=font_padrao,
    command=registrar_emprestimo,
    bg="#4CAF50",
    fg="white",
)
btn_registrar_emprestimo.grid(row=2, columnspan=2, pady=10, sticky="ew")

# Ajustar tamanhos das colunas para ocupar todo o espaço disponível
for frame in [frame_usuario, frame_livro, frame_emprestimo]:
    for i in range(2):
        frame.grid_columnconfigure(i, weight=1)

root.mainloop()
