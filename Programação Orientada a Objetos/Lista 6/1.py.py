'''
Você foi contratado para desenvolver um programa de simulação de batalhas medievais. Para isso,
você precisa implementar um sistema de unidades militares que possa se movimentar e atacar.
Você deve criar três classes de unidades: Soldado, Arqueiro e Cavaleiro. Todas as classes devem
herdar de uma classe base chamada UnidadeMilitar. A classe UnidadeMilitar deve ter os seguintes
métodos:
• mover(): exibe uma mensagem indicando que a unidade está se movendo.
• atacar(): exibe uma mensagem indicando que a unidade está atacando.
Cada uma das classes filhas deve implementar os métodos mover() e atacar() de forma específica,
de acordo com a especialidade da unidade.
Crie uma instância de cada uma das diferentes unidades (Soldado, Arqueiro e Cavaleiro), e adicione em
uma lista chamada unidades. Por fim, você deve percorrer o array unidades usando um loop e chamar os
métodos mover() e atacar() de cada unidade no array.

'''
class UnidadeMilitar():
    def __init__(self):
        
        def mover(self):
            print('Esta se movendo...')
    
        def atacar(self):
            print('Estamos atacando...')
            
class Soldado(UnidadeMilitar):
    
    def mover(self):
            print('O soldado está marchando.')
    
    def atacar(self):
        print('O soldado está atacando com sua espada.!')
        
class Arqueiro(UnidadeMilitar):
        
    def mover(self):
        print('O arqueiro está se rastejando!')
    
    def atacar(self):
        print('O arqueiro está disparando flechas.')
        
class Cavaleiro(UnidadeMilitar):
        
    def mover(self):
        print('O cavaleiro está galopando.')
    
    def atacar(self):
       print('O cavaleiro está atacando com sua lança.')
   
    
# Criando Objeto
soldado= Soldado()
arqueiro= Arqueiro()
cavaleiro= Cavaleiro()

#chamando metodo

soldado.mover()
soldado.atacar()
print()
arqueiro.mover()
arqueiro.atacar()
print()
cavaleiro.mover()
cavaleiro.atacar()
print('---------------------------------------------------')
#---------------------------------------------------

unidades=[soldado, arqueiro, cavaleiro]

for unidades in unidades:
    unidades.mover()
    unidades.atacar()
    print()


