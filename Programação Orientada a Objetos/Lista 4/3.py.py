'''
Desenvolva uma classe base chamada Criptografia que contenha os métodos cifrar e decifrar. Essa
classe servirá como base para as subclasses CifraCesar e CifraXor, que implementarão algoritmos
de criptografia específicos.
A classe Criptografia terá os seguintes métodos:
• Método cifrar(texto): Este método receberá um texto como entrada e retornará o texto
cifrado de acordo com o algoritmo de criptografia. Cada subclasse irá implementar sua
própria lógica de cifragem.
• Método decifrar(texto_cifrado): Este método receberá um texto cifrado como entrada e
retornará o texto original decifrado de acordo com o algoritmo de criptografia
correspondente.
A classe CifraCesar herda da classe Criptografia e implementa o algoritmo de criptografia conhecido
como Cifra de César. A Cifra de César desloca cada letra do texto original um número fixo de posições
no alfabeto para cifrar e decifrar o texto.
A classe CifraXor herda da classe Criptografia e implementa o algoritmo de criptografia usando a
operação XOR (OU exclusivo). Nesse algoritmo, cada caractere do texto original é combinado com uma
chave usando a operação XOR para obter o texto cifrado. A operação XOR também é usada para decifrar
o texto cifrado, combinando-o novamente com a mesma chave.
Os métodos cifrar e decifrar de cada subclasse devem ser implementados de acordo com a lógica
específica de cada algoritmo de criptografia.

'''
class Criptografia:
    def cifrar(self, texto):
        pass

    def decifrar(self, texto_cifrado):
        pass


class CifraCesar(Criptografia):
    def __init__(self, deslocamento):
        self.deslocamento = deslocamento

    def cifrar(self, texto):
        texto_cifrado = ""
        for char in texto:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                char_index = ord(char) - ascii_offset
                char_index = (char_index + self.deslocamento) % 26
                texto_cifrado += chr(char_index + ascii_offset)
            else:
                texto_cifrado += char
        return texto_cifrado

    def decifrar(self, texto_cifrado):
        texto_decifrado = ""
        for char in texto_cifrado:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                char_index = ord(char) - ascii_offset
                char_index = (char_index - self.deslocamento) % 26
                texto_decifrado += chr(char_index + ascii_offset)
            else:
                texto_decifrado += char
        return texto_decifrado


class CifraXor(Criptografia):
    def __init__(self, chave):
        self.chave = chave

    def cifrar(self, texto):
        texto_cifrado = ""
        for char in texto:
            texto_cifrado += chr(ord(char) ^ self.chave)
        return texto_cifrado

    def decifrar(self, texto_cifrado):
        texto_decifrado = ""
        for char in texto_cifrado:
            texto_decifrado += chr(ord(char) ^ self.chave)
        return texto_decifrado


# Exemplo de uso das classes Criptografia, CifraCesar e CifraXor

# Cifra de César
cesar = CifraCesar(3)
texto = "Criptografia de César"
texto_cifrado = cesar.cifrar(texto)
texto_decifrado = cesar.decifrar(texto_cifrado)

print("Texto original:", texto)
print("Texto cifrado:", texto_cifrado)
print("Texto decifrado:", texto_decifrado)
print()
# Cifra XOR
xor = CifraXor(9)
texto = "Criptografia XOR"
texto_cifrado = xor.cifrar(texto)
texto_decifrado = xor.decifrar(texto_cifrado)

print("Texto original:", texto)
print("Texto cifrado:", texto_cifrado)
print("Texto decifrado:", texto_decifrado)

