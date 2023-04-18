class calculadora:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def somar(self):
        return self.n1 + self.n2

    def dividir(self):
        return self.n1 / self.n2
        if n2 == 0:
            print("ERRO: divisão por zero!")
            return -1

    def subtrair(self):
        return self.n1 - self.n2

    def multiplicar(self):
        return self.n1 * self.n2


c = calculadora(2, 2)

print(c.somar())
print(c.subtrair())
print(c.dividir())
print(c.multiplicar())
