import random

class Equipe:
    def __init__(self, nome, vitorias):
        self.nome =nome
        self.vitorias = vitorias

    
    def getEquipe(self):
        pass
    
class Competidor(Equipe):
    def __init__(self, nome, vitoriasPessoais):
        self.nome =nome
        self.vitoriasPessoais = vitoriasPessoais
    
#----------------------
# grupo1 = Equipe('Equipe 1', 0)

p1=Competidor('Alina', 0)
p2=Competidor('Pedro', 0)
p3=Competidor('Taina', 0)
grupo1=[p1,p2, p3]

#grupo2 = Equipe('Equipe 2', 0)

p4=Competidor('Max', 0)
p5=Competidor('Debota', 0)
p6=Competidor('Denise', 0)
grupo2=[p4,p5, p6]
#----------------------
pedra = 0
papel = 1 
tesoura = 2 
#----------------------
vitorio=0
Rodada = 0
loop=False

while loop == False:
    sorteioG1=random.randint(3)
    sorteioG1=random.randint(3)
    if sorteioG1 == 1:
        print(p1.nome, 'foi escolhida(o).')
        
    if sorteioG1 == 2:
        print(p2.nome, 'foi escolhida(o).')
        
    if sorteioG1 == 3:
        print(p3.nome, 'foi escolhida(o).')
    
