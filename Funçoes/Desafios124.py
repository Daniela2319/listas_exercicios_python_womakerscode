# 1 - Desafio: exercicio 2
"""2. Peça ao usuário para informar o ano de nascimento. Em seguida, calcule e imprima a idade atual."""
anoNascimento = int(input("Digite o ano de nascimento: "))
anoAtual = 2024

idadeAtual = anoAtual - anoNascimento
print(f"A idade atual é: {idadeAtual} anos.")

# 2 - Desafio: exercicio 1
# 1. Faça um Programa que peça dois números e imprima o maior deles.
numeroA = 5
numeroB = 8

if numeroA > numeroB:
    print("Numero A é maior que B")
else:
    print("numero A não é maior que B")

# 2 - Desafio: exercicio 10
# 10. Faça um programa que lê três números inteiros e os mostra em ordem crescente.

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))

numeros = [num1, num2, num3]
numeros_ordenados = sorted(numeros)
print("Os números em ordem crescente são:", numeros_ordenados)


# 4 - Desafio: exercicio 4
"""4. Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira. Considere a tabela de conversão abaixo:
 Dólar Americano: R$ 4,91
 Peso Argentino: R$ 0,02
 Dólar Australiano: R$ 3,18
 Dólar Canadense: R$ 3,64
 Franco Suiço: R$ 0,42
 Euro: R$ 5,36
 Libra esterlina: R$ 6,21"""

# Solicitar a quantidade de dinheiro em reais
dinheiro_reais = float(
    input("Digite a quantidade de dinheiro que você tem na carteira (em reais): ")
)

# Taxas de conversão
taxa_dolar_americano = 4.91
taxa_peso_argentino = 0.02
taxa_dolar_australiano = 3.18
taxa_dolar_canadense = 3.64
taxa_franco_suico = 0.42
taxa_euro = 5.36
taxa_libra_esterlina = 6.21

# Cálculo da quantidade de cada moeda estrangeira que pode ser comprada
quantidade_dolar_americano = dinheiro_reais / taxa_dolar_americano
quantidade_peso_argentino = dinheiro_reais / taxa_peso_argentino
quantidade_dolar_australiano = dinheiro_reais / taxa_dolar_australiano
quantidade_dolar_canadense = dinheiro_reais / taxa_dolar_canadense
quantidade_franco_suico = dinheiro_reais / taxa_franco_suico
quantidade_euro = dinheiro_reais / taxa_euro
quantidade_libra_esterlina = dinheiro_reais / taxa_libra_esterlina

# Mostrar os resultados
print(f"Com R${dinheiro_reais:.2f}, você pode comprar:")
print(f"{quantidade_dolar_americano:.2f} Dólares Americanos")
print(f"{quantidade_peso_argentino:.2f} Pesos Argentinos")
print(f"{quantidade_dolar_australiano:.2f} Dólares Australianos")
print(f"{quantidade_dolar_canadense:.2f} Dólares Canadenses")
print(f"{quantidade_franco_suico:.2f} Francos Suíços")
print(f"{quantidade_euro:.2f} Euros")
print(f"{quantidade_libra_esterlina:.2f} Libras Esterlinas")
