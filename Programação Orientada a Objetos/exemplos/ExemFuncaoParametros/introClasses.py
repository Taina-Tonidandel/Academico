# Definição das classe Magos

class Mago:
    def __init__(self, nome, idade, escola, ):
        # Atributos de instância
        self.nome = nome 
        self.idade = idade   
        self.escola = escola 
        
        
    def andar(self):
        print('Estou andando')
    
    def falar(self):
        print('Ola amigue! Meu nome é ',self.nome)
        
    def invocarMagia(self):
        print('Invocando magia!')
        
    def Voar(self):
        print('Haaaaa! Estou voando.')
    
    def comer(self):
        print('Estou com fome!')

    def imprimirData(Self):
        print(dia,'de',Mes,'de',ano,)
        
        
#Intanciação de um objeto da classe Mago
hp = Mago('Harry Potter', 17, 'Hogwarts')
hg = Mago('Hogolts', 2000, 'Magos cinza')
mi = Mago('Monica', 6, 'Escola de magias')
So = Mago('Sofia', 4, 'Unicornio')
ma = Mago('Maroa', 25, 'Casa de doces')
#---------------------
dia = input("Que Dia é Hoje? ")
Mes = input('Em que Mês estamos? ')
ano = input("Em que século? ")

print(hp.nome)
print(hp.idade)
print(hp.escola)



hp.andar()
hp.falar()
hp.invocarMagia()