import random

class Competidor:
    def __init__(self, nome):
        self.nome = nome
        self.pos = 0

    def atualizar(self):
        jogada = random.randint(1,6)
        self.pos += jogada

        if self.pos == 5:
            print('Vixe, Deve voltar 1 casa')
            self.pos-1
            print(self.pos-1)

        elif self.pos == 7 or self.pos == 17:
            print('Oba!, Deve avançar 2 casas')
            self.pos + 2
            print(self.pos+2)

        elif self.pos == 13:
            self.pos = 0
            print('OMG!, Você voltou a estaca 0 (ZERO)')

            print(self.pos)

        else:
            print(self.pos)


competidores = [Competidor("Alice"), Competidor("Bob"), Competidor("Charlie"), Competidor("Dave"), Competidor("Eve")]
vencedor = None
terminou = False

while not terminou:
    for competidor in competidores:
        competidor.atualizar()
        print(f"{competidor.nome} está na posição {competidor.pos}"'\n')
        if competidor.pos >= 20:
            vencedor = competidor
            terminou = True

print(f"{vencedor.nome} venceu a corrida!")
