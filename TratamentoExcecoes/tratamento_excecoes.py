def divisao(a, b):
    try:
        resultado = a / b
        print(resultado)

    except ZeroDivisionError:
        print("Erro: Impossível dividir um valor por zero!")


divisao(10, 2)

while True:
    try:
        categoria = int(input("Digite a categoria do produto de 1 a 5: "))
        if categoria == 1:
            preco = 10
        elif categoria == 2:
            preco = 18
        elif categoria == 3:
            preco = 23
        elif categoria == 4:
            preco = 26
        elif categoria == 5:
            preco = 31
        else:
            print("Categoria inválida, digite um valor entre 1 e 5!")
            preco = 0
            continue  # Volta para o início do loop se a categoria for inválida

        print("O preço do produto é: R$%6.2f" % preco)
        break  # Sai do loop se a categoria for válida
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
