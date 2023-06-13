import csv

class Usuario:
    def __init__(self, nome=None, sobrenome=None, dataNasc=None, cpf=None,nomeussi=None, senha=None):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dataNasc = dataNasc
        self.cpf = cpf
        self.nomeussi = nomeussi
        self.senha = senha
        self.assinatura = []
        self.usuarios = []
        
        
        def adicionar_assinatura(self, assinatura): 
            ass = Assinaturas()
            self.assinatura.append(ass.tipo)
            
        def cancelar_assinatura(self, id_assinatura):
            pass
            
        def exibir_dados(self):
            print('Os dados do Usuario é:', self.nome)
            print('Os dados do Usuario é:', self.sobrenome)
            print('Os dados do Usuario é:', self.dataNasc)
            print('Os dados do Usuario é:', self.cpf)
            print('Os dados do Usuario é:', self.nomeussi)
            print('Os dados do Usuario é:', self.senha)
            
        def serializar(self): 
            return f'{self.nome} ; {self.sobrenome} ; {self.dataNasc} ; {self.cpf} ; {self.nomeussi} ; {self.senha}'
            
        def desserializar(dados):
            pass
        
class Assinaturas:
    def __init__(self, tipo=None, preco=None, idUsusi=None, status=None):
        self.tipo = tipo
        self.preco =preco
        self.idUsusi = idUsusi
        self.status = status
        
    def exibir_dados(self):
        print('O tipo da assinatura:', self.tipo)
        print('O valor da assinatura:', self.preco)
        print('O ID do usuário da assinatura:', self.idUsusi)
        print('O status da assinatura:', self.status)
    
    def serializar(self):
        return f'{self.tipo} ; {self.preco} ; {self.idUsusi} ; {self.status}'
    
    def desserializar(dados):
        pass
#-------------------------------------------------------------------------------------------
def criar_usuarios(arquivo_csv):
    usuarios = []

    with open(arquivo_csv, 'r') as file:
        reader = csv.reader(file, delimiter=';')

        for linha in reader:
            # Extrair dados relevantes da linha
            nome = linha[0]
            sobrenome = linha[1]
            dataNasc = linha[2]
            cpf = linha[3]
            nomeussi = linha[4]
            senha = linha[5]
            

            # Criar objeto de Usuário com os dados da linha
            usuario = Usuario(nome, sobrenome, dataNasc, cpf, nomeussi, senha)

            # Adicionar usuário à lista de usuários
            usuarios.append(usuario)

    return usuarios

def ler_dados_csv(arquivo_csv):
    dados = []

    with open(arquivo_csv, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for linha in reader:
            dados.append(linha)

    return dados

#Ler dados da tabela 1
arquivo_usi = ler_dados_csv("Usuarios.csv")

#Ler dados da tabela 2
arquivo_assi = ler_dados_csv("Assinaturas.csv")


loop = False

while loop == False:
    usuario = criar_usuarios("Usuarios.csv")
    usi = self.usuarios = usuario
    # usi=[Usuario(usuarios[4], usuarios[5])]
    # usi.self.Usuario
    
    login = input('adicione seu login:')
    senhaUsi = input('adicione sua senha:')
    
    if usi.nomeussi==login and usi.senha==senhaUsi:
        print('--- ENTROU ---')
        
    else:
        print('Senha ou login incoreto...')









