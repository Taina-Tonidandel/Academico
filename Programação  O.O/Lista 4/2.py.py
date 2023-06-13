'''Crie uma classe base chamada Veiculo com os seguintes atributos:
• marca: marca do veículo (string)
• modelo: modelo do veículo (string)
• ano: ano de fabricação do veículo (int)
A classe Veiculo deve ter os seguintes métodos:
• acelerar(): exibe a mensagem "Acelerando o veículo!"
• frear(): exibe a mensagem "Freando o veículo!"
Crie três classes derivadas da classe Veiculo:
UNIVERSIDADE DO VALE DO RIO DOS SINOS
Graduação Tecnológica: Fundamentos de Programação
• Carro: com os atributos adicionais:
• cor: cor do carro (string) A classe Carro deve ter os seguintes métodos adicionais:
• ligar_radio(): exibe a mensagem "Ligando o rádio do carro!"
• abrir_porta(): exibe a mensagem "Abrindo a porta do carro!"
• Moto: com os atributos adicionais:
• cilindrada: cilindrada da moto (string) A classe Moto deve ter os seguintes métodos
adicionais:
• empinar(): exibe a mensagem "Empinando a moto!"
• buzinar(): exibe a mensagem "Buzinando a moto!"
• Caminhao: com os atributos adicionais:
• carga_maxima: capacidade máxima de carga do caminhão (string) A classe
Caminhao deve ter os seguintes métodos adicionais:
• carregar(): exibe a mensagem "Carregando o caminhão!"
• descarregar(): exibe a mensagem "Descarregando o caminhão!"
'''

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo =  modelo
        self.ano = ano
        
    def acelerar(self):
        print("Acelerando o veículo!")
        
    def frear(self):
        print("Freando o veículo!")
        
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor):
        super().__init__( marca, modelo, ano)
        self.cor =  cor
        
    def ligar_radio(self):
        print("Ligando o rádio do carro!")
        
    def abrir_porta(self):
        print("Abrindo a porta do carro!")

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindrada):
        super().__init__( marca, modelo, ano)
        self.cilindrada = cilindrada
        
    def empinar(self):
        print("Empinando a moto!")
        
    def buzinar(self):
        print("Buzinando a moto!")

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, carga_maxima):
        super().__init__( marca, modelo, ano)
        self.carga_maxima = carga_maxima
        
    def carregar(self):
        print("Carregando o caminhão!")
        
    def descarregar(self):
        print("Descarregando o caminhão!")
        
# Criando objetos
car = Carro("Ford", "Ka", 2007, "Branco")
print("------ Carro ------")
print('o Carro é da marca', car.marca, 'do modelo', car.modelo, 'é do ano',car.ano, 'e tem a cor:', car.cor)
car.ligar_radio()
car.acelerar()
car.frear()
car.abrir_porta()
print()

moto = Moto('Honda', 'Biz', 2012, "100I")
print("------ Moto ------")
print('A moto é da marca', moto.marca, 'do modelo', moto.modelo, 'é do ano',moto.ano, 'e tem', moto.cilindrada,'cilindrada.')
moto.acelerar()
moto.empinar()
moto.buzinar()
moto.frear()
print()

caminhao = Caminhao("Ford", ' F-MAX 500', 2022, '12,7 litros')
print("------ caminhão ------")
print('O caminhão é da marca', caminhao.marca, 'do modelo', caminhao.modelo, 'é do ano',caminhao.ano, 'e a carga maxima é de', caminhao.carga_maxima)
caminhao.acelerar()
caminhao.carregar()
caminhao.frear()
caminhao.descarregar()

