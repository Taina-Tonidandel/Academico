
class CorpoCeleste:
    def __init__(self, nome = None, diametro = float, composicao=''):
        self.nome = nome
        self.diametro = diametro
        self.composicao = composicao
        
    def exibirInformacoes(self):
        print(self.nome, self.diametro, self.composicao)
        
    
        
        
        
class Planeta(CorpoCeleste):
    def __init__(self, nome = None, diametro = None, composicao = None, nLua = None, atmosfera = None):
        super().__init__(nome, diametro, composicao)
        self.nLua = nLua
        self.atmosfera = atmosfera
        
    def exibirInformacoes(self):
        return super().exibirInformacoes()
        
    def getlua(self):
        print('Número de Luas: ', self.nLua)
        
    def getatmosfera(self):
        print('Tipo de Atmosfera: ', self.atmosfera)
        
class Satelite(CorpoCeleste):
    def __init__(self, nome= None, diametro= None, composicao= None, planetaOrb= None, tempoOrb= None):
        super().__init__(nome, diametro, composicao)
        self.planetaOrb = planetaOrb
        self.tempoOrb = tempoOrb
        
    def exibirInformacoes(self):
        return super().exibirInformacoes()
    

    def getplanetaOrb(self):
        print('Planeta de Órbita: ', self.planetaOrb)
        
    def gettempoOrb(self):
        print('Período de Órbita: ', self.tempoOrb)
        
class Estrela(CorpoCeleste):
    def __init__(self, nome= None, diametro= None, composicao= None, temperatura= None , espectral= None):
        super().__init__(nome, diametro, composicao)
        self.temperatura = temperatura
        self.espectral = espectral
        
    def exibirInformacoes(self):
        return super().exibirInformacoes()
        
    def gettemperatura(self):
        print('Temperatura : ', self.temperatura)
        
    def getespectral(self):
        print('Tipo Espectral : ', self.espectral)
        
terr = Planeta('Terra', 12.742, 'vulcão', 1, 'Atmosfera terrestre')
print('Terra')
terr.exibirInformacoes()
terr.getlua()
terr.getatmosfera()
print()

luna = Satelite('Luna', 5262.4, 'Metal', 'Saturno', 1095)   
print('Luna')
luna.exibirInformacoes()
luna.getplanetaOrb()
luna.gettempoOrb()
print()


sol = Estrela('Sol', 1392.700 , 'Hidrogênio e Hélio', 5.772, 'G2' )   
print('Sol')
sol.exibirInformacoes()
sol.gettemperatura()
sol.getespectral()
    
    
    
    
    
    
    







