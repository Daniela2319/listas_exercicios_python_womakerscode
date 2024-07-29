class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        pass

    def cumprimentar(self):
        print(f"Ola meu nome é {self.nome} e tenho {self.idade}")


pessoa1 = Pessoa("Daniela", 40)
pessoa1.cumprimentar()

pessoa2 = Pessoa("Valdemar", 39)
pessoa2.cumprimentar()

pessoa2 = Pessoa("Frank João", 7)
pessoa2.cumprimentar()

valor_casa_compra = float(input("Digite o valor da casa a compra: "))
valor_salario = float(input("Digite o valor do seu salario: "))
quantidade_paga_ano = float(input("Digite o valor da prestação anual: "))

# Calcula o valor da prestação mensal
meses_a_pagar = quantidade_paga_ano * 12
prestacao_mensal = valor_casa_compra / meses_a_pagar
# Verifica se a prestação não excede 30% do salário
limite_prestacao = valor_salario * 0.3
if prestacao_mensal <= limite_prestacao:
    print(f"A prestação mensal é de R$ {prestacao_mensal:.2f}. Empréstimo aprovado!")
else:
    print(f"A prestação mensal excede 30% do salário. Empréstimo não aprovado.")
