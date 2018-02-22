# encoding: utf-8
""" by: offsouza - Brasil - 2017"""


from scipy.stats import mode
import serial
import numpy as np
import csv
import sys
import time



class SENSOR():



    def __init__(self):
        ''' funçao que inicializa o programa '''

        self.arquivo = 'colorimetroteste1.csv' #definir banco a ser utilizado


        print ("0 --- Para criar novo banco")
        print ("1 --- Para atualizar banco de dados")
        print ("2 --- Para testar uma amostra")
        print ("3 --- Para verificar amostras do proprio banco de dados")
        print ("4 --- Para verificar numero de amostrar no banco de dados ")
        print ("5 --- Para sair do programa ")

        escolha = input(" Digite aqui -->  ")
        #print escolha

        if escolha==1 :
            print(" 0 - cor 0")

            print ("1 - cor 1 ")

            print ("2 - cor 2 ")

            print ("3 - cor 3")

            print ("4 - cor 4 ")

            print ("5 - cor 5")




            escolha2 = input(" Digite aqui -->  ")


            if escolha2 == 0:
                self.qualidade = np.array([0])
            if escolha2 == 1 :
                self.qualidade = np.array([1])
            if escolha2 == 2:
                self.qualidade = np.array([2])
            if escolha2 == 3:
                self.qualidade = np.array([3])
            if escolha2 == 4:
                self.qualidade = np.array([4])
            if escolha2 == 5:
                self.qualidade = np.array([5])




            self.ino()
            self.adicionar_amostra_banco()


        if escolha == 2:
             self.ino()
             self.treinar_amostra()

        if escolha == 0:
            print 'ola mundo'
            self.criar_banco()

        if escolha ==3:
            self.treinar_banco()

        if escolha == 4:
            self.amostrasCastradas()

        if escolha ==5:
            print ('****Programa finalizado****')
            sys.exit(0)

        #time.sleep(3)


    def criar_banco(self):


           bd = open(self.arquivo, 'w')

           print ("Banco de dados criado ou restaurado ")

           bd.close()




    def ino (self):
        ''' Ler  dados da serial do arduino  e chama algumas funcoes ==> moda e lux'''

      #try:1

        print("Aperte o botão da leitura ")

        self.arduino = serial.Serial('COM6', 9600, timeout=.1)

        #self.banco = []

        self.banco = []
        i = 0
        while (i < 300):
            ''' caso usar sensor comercial aumentar para 400 e desligar lux'''

            data = self.arduino.readline()[:-2]



            if data:
                #print data
                self.banco.append(int(data))
                self.dados = np.array(self.banco)
                i += 1
                #self.dados = self.dados.reshape(1,-1)
                #print self.dados
        self.arduino.close()
        #print (self.banco)
        print (self.dados)
        print (len(self.dados))

        self.moda()


        #self.lux()
    '''
      except serial.serialutil.SerialException:
          print (" Porta nao esta conectada")
          sys.exit(0)
    '''




    def treinar_banco(self):
        ''' Treina o proprio banco de dados, a fim de calcular porcetagem de acerto no proprio banco'''

        try:
            self.x = np.genfromtxt(self.arquivo, delimiter=',', usecols=(range(0,30)))
            self.y = np.genfromtxt(self.arquivo, delimiter=',', usecols=(30))

        except IOError:

            print(" Banco de dados ainda não foi criado ")
            print (" Por favor criar novo banco")


        from sklearn.model_selection import train_test_split

        x_treino, x_teste, y_treino, y_teste = train_test_split(self.x, self.y, test_size=0.3, random_state=42)

        from sklearn.neighbors import KNeighborsClassifier
        lista = []

        for i in range(1, 10):
            knn = KNeighborsClassifier(n_neighbors=i, p=2, weights='distance', algorithm='brute')
            knn.fit(x_treino, y_treino)
            labels = knn.predict(x_teste)

            acertos = (labels == y_teste).sum()

            print (labels)
            print (y_teste)

            total = float(len(x_teste))
            porcent = 100 * (acertos / total)
            porcent = int(porcent)

            lista.append(porcent)

            score = knn.score(x_teste, y_teste)
            score = float(score)

            print ('Porcentagem de acerto %f = %s %% ' %(score, porcent) )
        #print score
        #print porcent
        #print lista

    def treinar_amostra(self):
        ''' treina uma unica amostra externa baseada no banco de dados'''

        try:
            self.x = np.genfromtxt(self.arquivo, delimiter=',', usecols=(range(0, 30)))
            self.y = np.genfromtxt(self.arquivo, delimiter=',', usecols=(30))
            #print (self.x)


        except IOError:

            print(" Banco de dados ainda não foi criado ")
            print (" Por favor criar novo banco")



        from sklearn.neighbors import KNeighborsClassifier
        lista = []

        for i in range(1, 10):
            self.dadosok = self.dadosok.reshape(1, -1)
            knn = KNeighborsClassifier(n_neighbors=i, p=2, weights='distance', algorithm='brute')
            knn.fit(self.x, self.y)
            labels = knn.predict(self.dadosok)
            labels = int(labels)


            print ("labels")
            print (labels)

        if labels == 0 :
                 print(" cor 0 ")
        if labels == 1 :
            print ("cor 1")
        if labels == 2 :
            print ("cor 2 ")
        if labels == 3 :
            print ("cor 3")
        if labels == 4 :
            print ("cor 4 ")
        if labels == 5 :
           print ("cor 5")


    def adicionar_amostra_banco(self):
        ''' Adiciona amostra no banco de dados em CSV (excel) '''

        bd = open(self.arquivo, 'a')
        writer = csv.writer(bd)

        #self.dadosok = np.hstack((self.dados, self.listalux))
        self.dadosok = np.hstack((self.dadosok, self.qualidade))



        writer.writerow((self.dadosok))
        print (" Dados qualificado" ), (self.dadosok)

    def moda (self):
        ''' tira a moda de 10 em 10 amostras do sensor em guarda em um variavel'''
        self.dados = list(self.dados)

        i = 0               #numero de valores entre cada amostra
        j = 10               #numero de valores entre cada amostra
        self.listamoda = []
        for u in range(0,30):
            lista = []
            for z in range(i,j):
                lista.append(self.dados[z])
            i += 10
            j += 10
            moda1 = mode(lista)

            self.listamoda.append(moda1[0])

        self.listamoda = np.asarray(self.listamoda)
        self.dados = self.listamoda
        #self.dados = self.dados.astype(np.int64)
        #print "dados", self.listamoda
        self.dadosok = self.dados.flatten()     #transforma em um array de 1 dimensao
        print (" Moda "), (self.dadosok)

        #print " Moda " , self.listamoda

    def lux(self):

        ''' calcular o lux = sqrt (r^2 + g^2 + b^2) e adiciona no banco de dados   '''

        self.listaRGB = []
        self.listalux = []
        r = 0
        g = 10
        b = 20

        for i in range(0,10):
            self.listaRGB = []
            self.listaRGB.append(self.dados[r])
            self.listaRGB.append(self.dados[g])
            self.listaRGB.append(self.dados[b])

            ##print self.listaRGB
            self.lux = np.asarray(self.listaRGB)
            self.lux = np.power(self.lux,2)
            self.lux = np.sum(self.lux)
            self.lux = np.sqrt(self.lux)


            self.listalux.append(self.lux)

            r += 1
            g += 1
            b += 1
        #print self.listalux
        self.listalux = np.asarray(self.listalux)
        self.listalux = np.around(self.listalux)
        self.listalux = self.listalux.astype(np.int64)

        self.dadosok = np.hstack((self.dados, self.listalux))

        print ("listaluz") ,( self.listalux)
        print ("dados ok") , (self.dadosok)
        print ("  ")

    def amostrasCastradas (self):

        bd = open(self.arquivo, 'r')
        aa = csv.reader(bd)
        xx = 0

        for ii in aa:

            # x = x + 1
            if ii != []:
                xx = xx + 1


        print (" Amostras cadastradas %d" %xx)




#LDR()


while True:

    try:

        SENSOR()
        time.sleep(3)
        print ("\n*********************************************************** ")
        print ("\n********************* Selecione ************************ ")
        print ("\n*********************************************************** ")

    except  :
        print ("\nTente novamente ")


    #except'''
