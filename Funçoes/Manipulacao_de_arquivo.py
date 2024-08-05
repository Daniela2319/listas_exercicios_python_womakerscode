# eeclarando uma função
def titulo(txt):
    print("-=" * 30)
    print(txt)
    print("-=" * 30)


titulo("Exercício 01")


def multiplicacao():
    mult = 10 * 2
    # abertura de arquivo
    file = "arquivo.txt"

    # abertura para escrita
    arquivo_escrito = open(file, "w")
    arquivo_escrito.write("Texto a ser escrito")
    arquivo_escrito.close()

    # abertura somente para leitura
    arquivo_leitura = open(file, "r")
    leitura = arquivo_leitura.read()
    print(leitura)
    arquivo_leitura.close()


# abertura de arquivo binário
# arquivo_binario = open(file, "wb")
# print(f'O Resultado da multiplicação é {mult}')

multiplicacao()  # chamada da função
# 4 - Desafio: exercicio 2


titulo("Exercício 03")


def epar(x):
    return x % 2 == 0


print(epar(5))
print(epar(2))
print(epar(1))
print(epar(10))

titulo("Exercício 04")


def par_ou_impar(x):
    if epar(x):
        return f"É par {x}"
    else:
        return f"É impar {x}"


print(par_ou_impar(4))
print(par_ou_impar(5))

titulo("Exercício 05")


def maximo(numA, numB):
    if numA > numB:
        return numA
    else:
        return numB


print(maximo(5, 6) == 6)
print(maximo(2, 1) == 2)
print(maximo(7, 7) == 7)
print(maximo(4, 8) == 5)

titulo("Exercício 06")


def calcular(n1, n2, n3):
    return n1 + n2 + n3


cliente1 = 7
cliente2 = 8
cliente3 = 12

resultado = calcular(cliente1, cliente2, cliente3)

print(f"A soma de {cliente1}, {cliente2} e {cliente3} é igual a {resultado}")

titulo("Exercício 06")


def numero_reverso(num):
    num_str = str(num)
    num_invertido = int(num_str[::-1])
    return num_invertido


numero = 523
resultado = numero_reverso(numero)
print(f"Numero reverso 523 é : {resultado}")

titulo("Exercício 07")


def temp_celsius_para_fahrenheir(celsius):
    return (celsius * 9 / 5) + 32


def temp_fahrenheir_para_celsius(fahrenheir):
    return (fahrenheir - 32) * 5 / 9


def menu():
    while True:
        op = int(
            input("1. Celsius para Fahrenheir: \n " + "2. Fahrenheir para Celsius: \n")
        )
        if op == 1:
            c = int(input("Graus Celsius: "))
            print("Convertido: ", temp_celsius_para_fahrenheir(c), "graus Fahrenheir\n")
            break
        elif op == 2:
            f = int(input("Graus Fahrenheir: "))
            print("Convertido: ", temp_celsius_para_fahrenheir(f), "graus Celsius")
            break
        else:
            print("Opa Opção inválida!")
            continue


menu()
