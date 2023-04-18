def cumprimentar(nome):
    print("Ola,", nome)


cumprimentar("Tainá")

nome= "Rafael"
nome2 ="Rafaela"

cumprimentar(nome)
cumprimentar(nome2)

nome3= input("Digite um nome:")

cumprimentar(nome3)

Nomes =["ana", "Pedro", "maria", "joao", "Eduardo"]

for i in Nomes:
    cumprimentar(i)

for i in range(len(Nomes)):
    cumprimentar(Nomes[i])