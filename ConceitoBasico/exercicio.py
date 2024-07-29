#faça um programa que peça dois numeros, realize as principais operações +/-/*//
def titulo(txt):
    print('-=' * 30)
    print(txt)
    print('-=' * 30)

titulo('Exercício 01')

numeroA = int(input('Digite um número: '))
numeroB = int(input('Digite outro número: '))
operacao = input('Digite uma operação (+, -, * ou /): ')

match operacao:
    case '+':
        resultado = numeroA + numeroB
        print(f"A soma é igual a: {resultado}")
    case '-':
        resultado = numeroA - numeroB
        print(f"A subtração é igual a: {resultado}")
    case '*':
        resultado = numeroA * numeroB
        print(f"A multiplicação é igual a: {resultado}")
    case '/':
        if numeroB != 0:
            resultado = numeroA / numeroB
            print(f"A divisão é igual a: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    case _:
        print("Operação inválida. Por favor, escolha +, -, * ou /.")

titulo('Exercício 02')
anoNascimento = int(input('Digite o ano de nascimento: '))
anoAtual = 2024

idadeAtual = anoAtual - anoNascimento
print(f"A idade atual é: {idadeAtual} anos.")

titulo('Exercício 03')
quantKm = int(input('Digite quantidade de Km: '))

metro = quantKm * 10
centimetro = quantKm * 100
milimetro = quantKm * 1000

print(f"O metro é: {metro} m.")
print(f"O centimetro é: {centimetro} cm.")
print(f"O milimetro é: {milimetro} mm.")

titulo('Exercício 04')
quantLitros = int(input('Digite quantidade de litros de combustível: '))
disPercorrida = int(input('Digite a distância percorrida (em km): '))

# Calcula o consumo médio de combustível em km/l
consumoMedio = disPercorrida / quantLitros

# Calcula o custo total baseado no preço do combustível
custoConsumo = consumoMedio * 6.90

print(f'Custo do consumo médio: {custoConsumo:.2f}')

titulo('Exercício 08')
# Pergunta ao usuário o número de horas de exercício por semana
horas_por_semana = float(input('Digite o número de horas de exercício físico por semana: '))
# Calcula o número de minutos de exercício por semana
minutos_por_semana = horas_por_semana * 60
# Calcula o total de calorias queimadas por semana
calorias_por_semana = minutos_por_semana * 5
# Calcula o total de calorias queimadas em um mês (considerando 4 semanas em um mês)
calorias_por_mes = calorias_por_semana * 4
# Exibe o resultado
print(f'Total de calorias queimadas em um mês: {calorias_por_mes:.2f}')
print(f'Total de calorias queimadas por semana: {calorias_por_semana:.2f}')

titulo('Exercício 07')
usuarioPeso = float(input('Digite o seu peso: '))
usuarioAltura = float(input('Digite o seu altura: '))

imc = usuarioPeso / (2* usuarioAltura)
print(f"Seu IMC é: {imc:.2f}")

titulo('Exercício 09')
numero = -1
while numero < 0: #enquanto
  numero = int(input('Digite seu numero: '))


ano = int(input('Anos de serviço:'))
valor_por_ano = float(input('Valor por ano: '))
bonus = ano * valor_por_ano
print('Bonus de R$ %5.2f' % bonus)