class Musica:
    def __init__(self, NomedaMusica, artista, genero, ano, duracao):

        self.NomedaMusica = NomedaMusica
        self.artista = artista
        self.genero = genero
        self.ano = ano
        self.duracao = duracao

#Meus atributos

    def info(self): #exibe as informações (valores) dos atributos da música
        pass

    def retornarDuracao(self): #método de get da duração
        return self.duracao


#-----------------------------------------------

baseDeDados = []

# Criando um objeto da classe musica

musicas = Musica('Fa fe fi fo Funk', 'Anira', 'Funk', 2019, '3:05')

baseDeDados.append(musicas)

print(baseDeDados[0].NomedaMusica)