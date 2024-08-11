class Pao:  # classe pão é um molde ou uma receita define com criar um objeto
    def __init__(
        self, tipo, ingredientes, peso
    ):  # __init__ é um construtor onde se inicia esse atributos ou caracteristica para novo objeto da classe
        self.tipo = (
            tipo  # o self é usado para acessar os atributos da instância da classe
        )
        self.ingredientes = ingredientes
        self.peso = peso  # em gramas

    def descrever(self):  # método ou função da classe onde vai ocorre a ação do objeto
        print(
            f"Este é um pão do tipo {self.tipo} feito com {', '.join(self.ingredientes)}."
        )

    def calcular_preco(self, preco_por_grama):
        return self.peso * preco_por_grama


# Criando uma instância da classe Pao
# Criando o objetos da classe pão. Maneira de organiza os códigos em torno do objetos.
pao_frances = Pao("Francês", ["farinha", "água", "fermento", "sal"], 50)
pao_frances.descrever()
preco = pao_frances.calcular_preco(0.05)
print(f"O preço do pão é R${preco:.2f}")

pao_de_forma = Pao(
    "Pão de forma", ["farinha", "agua", "fermento", "sal", "gordura", "açúcar"], 45
)
pao_de_forma.descrever()
preco = pao_de_forma.calcular_preco(0.10)
print(f"o preço do pão é R$ {preco:.2f}")
