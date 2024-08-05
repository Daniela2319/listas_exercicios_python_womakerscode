class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, quantia):
        self.__saldo += quantia

    def sacar(self, quantia):
        if quantia <= self.__saldo:
            self.__saldo -= quantia
            print(f"Você está sacando R${quantia}")
        else:
            print(
                f" Você quer sacar R${quantia} o seu saldo é insuficiente R${self.__saldo}"
            )

    def mostrar_Saldo(self):
        print(f"Saldo: R${self.__saldo}")


# criando objeto classe conta bancaria
conta = ContaBancaria(1200)
conta.depositar(100)
conta.sacar(100)
conta.mostrar_Saldo()
