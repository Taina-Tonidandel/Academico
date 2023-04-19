class data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano



    def imprimirData(self):
        print(self.dia,'/',self.mes,'/',self.ano)

    def imprimirDataPorExtenso(self):

        if self.mes == 1:
            mese = 'janeiro'
        elif self.mes == 2:
             mese = 'fevereiro'
        elif self.mes == 3:
            mese = 'Março'
        elif self.mes ==4:
            mese = 'Abril'
        elif self.mes ==5:
            mese = 'Maio'
        elif self.mes ==6:
            mese = 'Junho'
        elif self.mes ==7:
            mese = 'Julho'
        elif self.mes ==8:
            mese = 'Agosto'
        elif self.mes ==9:
            mese = 'Setembro'
        elif self.mes ==10:
            mese = 'Outubro'
        elif self.mes ==11:
            mese = 'Novembro'
        elif self.mes ==12:
            mese = 'Dezembro'

        print(cidade, 'dia', self.dia, 'de', mese,'de', self.ano,'.')


hj = data(2, 8, 2002)
cidade = input('Adicione a sua cidade:')

hj.imprimirData()

hj.imprimirDataPorExtenso()





