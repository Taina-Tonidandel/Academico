'''Hierarquia de Figuras Geométricas: considere as seguintes figuras geométricas: retângulo, triângulo
e círculo. Crie uma hierarquia de classes para representar essas figuras geométricas. Cada classe
deve ter os seguintes atributos:
• Retângulo:

• base: comprimento da base do retângulo.
• altura: altura do retângulo.
• Triângulo:

• base: comprimento da base do triângulo.
• altura: altura do triângulo.
• Círculo:

• raio: raio do círculo.
Cada classe deve implementar os seguintes métodos:
• calcularÁrea(): calcula a área da figura geométrica.
• calcularPerimetro(): calcula o perímetro (ou circunferência, no caso do círculo) da figura
geométrica.
Você deve criar as classes Retangulo, Triangulo e Circulo, que herdam de uma classe base
FiguraGeometrica. Cada classe deve implementar os métodos de cálculo de área e perímetro de
acordo com as fórmulas adequadas para cada figura geométrica.
Além disso, você deve criar objetos dessas classes e testar os métodos calcularÁrea e
calcularPerimetro, exibindo os resultados para cada figura geométrica criada.
Lembre-se de utilizar as fórmulas corretas para calcular a área e o perímetro de cada figura
geométrica.
'''
class FiguraGeometrica:
    def __init__(self, base=None, altura=None, raio=None):
        self.base = base
        self.altura = altura
        self.raio = raio
        
    def calcularArea(self):
        pass
    
    def calcularPerimetro(self):
        pass
    
class Retangulo(FiguraGeometrica):
        
    def calcularArea(self):
        return self.base * self.altura
    
    def calcularPerimetro(self):
        return 2 * (self.base + self.altura)
    
class Triangulo(FiguraGeometrica):
        
    def calcularArea(self):
        r = 2/(self.base* self.altura)
        return r
        
    def calcularPerimetro(self):
        r = self.base + self.base + self.base
        return r
    
class Circulo(FiguraGeometrica): # erro 

    def calcularArea(self):
        r = (self.raio * self.raio) * 3.14
        return r
    
    def calcularPerimetro(self):
        r = (3.14 * 2) * self.raio
        return r



retangulo = Retangulo(5, 3 ) # Criando objetos
# Chamando os métodos
print("Retângulo:")
print("Área:", retangulo.calcularArea())
print("Perímetro:", retangulo.calcularPerimetro())
print()

triangulo = Triangulo(4, 6) # Criando objetos
# Chamando os métodos
print("Triângulo:")
print("Área:", triangulo.calcularArea())
print("Perímetro:", triangulo.calcularPerimetro())
print()

circulo = Circulo(0,0,2) # Criando objetos
# Chamando os métodos
print("Círculo:")
print("Área:", circulo.calcularArea())
print("Perímetro:", circulo.calcularPerimetro())
