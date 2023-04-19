''' Faça um programa que simule um "dado virtual". O dado deve ser modelado como uma classe,
possuindo apenas o número de faces e o método Rolar, que retorna o valor sorteado. O número
de faces deve ser definido na criação do objeto (construtor com parâmetro). Deve ser instanciado
um dado com 6, 8 e 12 faces no main(). Cada dado deve ser jogado 3 vezes e o resultado de cada
jogada deve ser impresso na tela. Não deve ser usado print dentro da classe.
'''
import random

class Dado:
    def __init__(self,faces):
        self.faces = faces

    def rolar(self):
        return random.randint(1,self.faces)


d6 = Dado(6)
d8 = Dado(8)
d12 = Dado(12)

for i in range (3):
    print(d6.rolar())

print()

for i in range (3):
    print(d8.rolar())

print()

for i in range (3):
    print(d12.rolar())
