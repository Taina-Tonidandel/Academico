class Bioma:
    def __init__(self, nome):
        self.nome = nome
        self.fauna = []
        self.flora = []


    def getNome(self):
        pass

    def adicionarAnimal(self,):
        self.fauna.append(Animal)

    def adicionarVegetal(self):
        self.flora.append(Vegetal)

    def exibir_Fauna(self):
        for fauna in self.fauna:
            print(fauna.nome)

    def exibir_Flora(self):
        for flora in self.flora:
            print(flora.nome)


class Animal:
    def __init__(self, nome):
        self.nome = ''
        self.nomeCientifico = ''
        self.filo = ''
        self.classe = ''
        self.familia = ''
        self.genero =''
        self.especie = ''
        self.estadoConservacao = ''

    def Animal(self):
        animal1= Animal('capivara', 'Hydrochoerus hydrochaeris', 'Mamifero', 'Caviidae', 'Hydrochoerus', 'Hydrochoerus hydrochaeris','Pouco preocupante')
    
    def getNome(self):
        pass


class Vegetal:
    def __init__(self, nome, nomeCientifico, filo, classe, familia, genero, especie, estadoConcervacao):
        self.nome = ''
        self.nomeCientifico = ''
        self.filo = ''
        self.classe = ''
        self.familia = ''
        self.genero =''
        self.especie = ''
        self.estadoConservacao = estadoConcervacao

    def Vegetal(self):
        pass
    
    def getNome(self):
        pass




faunaBR = [
# [Animal Amazônia Mata_Atlântica Cerrado Caatinga Pampa Pantanal]
['Capivara', True, True, True, True, True, True],
['Gralha azul', False, True, False, False, True, False],
['Tamanduá-bandeira', True, True, True, False, True, False],
['Onça pintada', True, True, False, True, False, True],
['Tatu-bola', False, False, False, True, False, False]
]
floraBR = [
# [Planta Amazônia Mata_Atlântica Cerrado Caatinga Pampa Pantanal]
['Ipê amarelo', True, True, True, True, True, True],
['Araucária', False, True, False, False, True, False],
['Mandacaru', False, False, True, True, False, False],
['Vitória-régia', True, False, False, False, False, True],
['Jatobá', True, True, True, False, False, True]
]
# Diquinha de como acessar a tabela ;)
for i in range(len(faunaBR)):
    for j in range(len(faunaBR[i])):
        print(faunaBR[i][j], end=' ')
    print('\n')
