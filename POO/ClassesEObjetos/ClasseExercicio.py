# Exercícios Classes - POO


class Carro:
    def __init__(self, cor, modelo, ligado=False, velocidade=0):
        self.cor = cor
        self.modelo = modelo
        self.ligado = ligado
        self.velocidade = velocidade

    def ligar(self):
        if self.ligado:
            print(f"{self.modelo} já está ligado!")
        else:
            self.ligado = True
            print(f"{self.modelo} está agora ligado!")

    def acelerar(self, acelera):
        if self.ligado:
            self.velocidade += acelera
            print(f"{self.modelo} acelerado para {self.velocidade} km/h!")
        else:
            print("Não pode acelerar, carro está desligado!")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            print(f"{self.modelo} está agora desligado!")
        else:
            print(f"{self.modelo} já está desligado!")


# Criação do objeto Carro
if __name__ == "__main__":
    carroA = Carro("preta", "fiat")
    carroB = Carro("Verde", "Corola")

    # Teste dos métodos
    carroA.ligar()
    carroA.acelerar(20)
    carroB.desligar()
