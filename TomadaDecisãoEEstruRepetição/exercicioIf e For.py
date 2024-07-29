def titulo(txt):
    print('-=' * 30)
    print(txt)
    print('-=' * 30)

titulo('Exercício 01 - condições')

numero = 0
while numero < 5: #enquanto
  numero = int(input('Digite seu numero: '))

print('numero positivo inserido com sucesso!')

frutas = ['maça', 'banana', 'uva'] #declarando uma lista
for fruta in frutas: #para cada
  print(fruta)

titulo('Exercício 02 - condições')
numeroA = 5
numeroB = 8

if numeroA > numeroB :
  print('Numero A é maior que B')
else :
  print("numero A não é maior que B")


titulo('Exercício 03 - condições')
turno = input('Digite uma seu turno (M-Matutino, V-Vespertino ou N-Noturno): ')

if turno == "M":
  print('Bom Dia!')
elif turno == 'V':
  print('Boa Tarde!')
elif turno == 'N':
  print("Boa Noite!")


titulo('Exercício 04 - condições')
while True:
  notaA = float(input('Digite uma nota entre 0 e 10: ')) #enquanto
  if 0 <= notaA <=10:
    print(f'Você digitou uma nota válida: {notaA}')
    break
  else :
      print('Valor inválido. A nota deve estar entre 0 a 10.')


while True:
    try:
        nota = float(input('Digite uma nota entre 0 e 10: '))
        if 0 <= nota <= 10:
            print(f'Você digitou uma nota válida: {nota}')
            break
        else:
            print('Valor inválido. A nota deve estar entre 0 e 10.')
    except ValueError:
        print('Entrada inválida. Por favor, insira um número.')


titulo('Exercício 05 - condições com tratamento exceções')
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
      print('Categoria inválida, digite um valor entre 1 e 5!')
      preco = 0
      continue  # Volta para o início do loop se a categoria for inválida
    
    print('O preço do produto é: R$%6.2f' % preco)
    break  # Sai do loop se a categoria for válida
  except ValueError:
    print('Entrada inválida. Por favor, insira um número.')


