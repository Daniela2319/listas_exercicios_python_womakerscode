def titulo(txt):
    print("-=" * 30)
    print(txt)
    print("-=" * 30)


""" 1. Faça um Programa que peça dois números, realize as principais operações soma, subtração, multiplicação, divisão"""
titulo("Exercício 01")

numeroA = int(input("Digite um número: "))
numeroB = int(input("Digite outro número: "))
operacao = input("Digite uma operação (+, -, * ou /): ")

match operacao:
    case "+":
        resultado = numeroA + numeroB
        print(f"A soma é igual a: {resultado}")
    case "-":
        resultado = numeroA - numeroB
        print(f"A subtração é igual a: {resultado}")
    case "*":
        resultado = numeroA * numeroB
        print(f"A multiplicação é igual a: {resultado}")
    case "/":
        if numeroB != 0:
            resultado = numeroA / numeroB
            print(f"A divisão é igual a: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    case _:
        print("Operação inválida. Por favor, escolha +, -, * ou /.")

"""2. Peça ao usuário para informar o ano de nascimento. Em seguida, calcule e imprima a idade atual."""
titulo("Exercício 02")
anoNascimento = int(input("Digite o ano de nascimento: "))
anoAtual = 2024

idadeAtual = anoAtual - anoNascimento
print(f"A idade atual é: {idadeAtual} anos.")

"""3. Faça um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros."""
titulo("Exercício 03")
quantKm = int(input("Digite quantidade de Km: "))

metro = quantKm * 10
centimetro = quantKm * 100
milimetro = quantKm * 1000

print(f"O metro é: {metro} m.")
print(f"O centimetro é: {centimetro} cm.")
print(f"O milimetro é: {milimetro} mm.")

"""4. Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprima o consumo médio em km/l."""
titulo("Exercício 04")
quantLitros = int(input("Digite quantidade de litros de combustível: "))
disPercorrida = int(input("Digite a distância percorrida (em km): "))

consumoMedio = disPercorrida / quantLitros

custoConsumo = consumoMedio * 6.90
print(f"Custo do consumo médio: {custoConsumo:.2f}")

"""5. Escreva um programa que calcule o salário líquido. Lembrando de declarar o salário bruto e o percentual de desconto do Imposto de Renda.
 ● Renda até R$ 1.903,98: isento de imposto de renda;
 ● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
 ● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
 ● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
 ● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%."""

salario_bruto = float(input("Digite o salário bruto: R$ "))
if salario_bruto <= 1903.98:
    aliquota = 0.0
elif salario_bruto <= 2826.65:
    aliquota = 0.075
elif salario_bruto <= 3751.05:
    aliquota = 0.15
elif salario_bruto <= 4664.68:
    aliquota = 0.225
else:
    aliquota = 0.275

desconto_ir = salario_bruto * aliquota
salario_liquido = salario_bruto - desconto_ir

# Exibir o resultado
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(
    f"Desconto de Imposto de Renda (alíquota de {aliquota * 100}%): R$ {desconto_ir:.2f}"
)
print(f"Salário Líquido: R$ {salario_liquido:.2f}")

"""6. Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de avião, carro e ônibus.
 Levando em consideração:
 ● avião = 600 km/h
 ● carro = 100 km/h
 ● ônibus = 80 km/h"""

distancia = 700

velocidade_aviao = 600
velocidade_carro = 100
velocidade_onibus = 80

tempo_aviao = distancia / velocidade_aviao
tempo_carro = distancia / velocidade_carro
tempo_onibus = distancia / velocidade_onibus

print(f"Para uma distância de {distancia} km:")
print(f"Tempo de viagem de avião: {tempo_aviao:.2f} horas")
print(f"Tempo de viagem de carro: {tempo_carro:.2f} horas")
print(f"Tempo de viagem de ônibus: {tempo_onibus:.2f} horas")

"""7. Solicite ao usuário o peso em kg e a altura em metros. Calcule e imprima o Índice de Massa Corporal (IMC) usando a fórmula:
 IMC = peso / (altura x altura)."""

titulo("Exercício 07")
usuarioPeso = float(input("Digite o seu peso: "))
usuarioAltura = float(input("Digite o seu altura: "))

imc = usuarioPeso / (2 * usuarioAltura)
print(f"Seu IMC é: {imc:.2f}")

"""8. Faça um Programa que pergunte quanto você ganha por hora e o
 número de horas trabalhadas no mês.Calcule e mostre o total do seu
 salário no referido mês."""
titulo("Exercício 08")


"""9. Solicite ao usuário o número de horas de exercício físico por semana. Calcule o total de calorias queimadas em um mês, considerando uma média de 5 calorias por minuto de exercício."""
horas_por_semana = float(
    input("Digite o número de horas de exercício físico por semana: ")
)
minutos_por_semana = horas_por_semana * 60
calorias_por_semana = minutos_por_semana * 5
calorias_por_mes = calorias_por_semana * 4

print(f"Total de calorias queimadas em um mês: {calorias_por_mes:.2f}")
print(f"Total de calorias queimadas por semana: {calorias_por_semana:.2f}")


"""10. Faça um Programa que utilize 4 variáveis como preferir e no final print
 uma mensagem amigável utilizando as variáveis criadas.
 Exemplos de variáveis: nome, idade, lugar, profissão ....
 Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo
 também e estou migrando de área."""

nome = "Camila"
idade = 40
cidade = "Curitiba"
profissacao = "Programado"

print(
    f"Olá meu nome é {nome}, tenho {idade} anos, eu moro em {cidade} estou trabalhando na area da {profissacao}"
)
