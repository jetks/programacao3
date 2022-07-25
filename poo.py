class Cachorro:
    __nome = None
    __raça = None
    __latindo = None
    
    def __init__(self, nome, raça, latindo=False):
        self.__nome = nome
        self.__raça = raça
        self.__latindo = latindo

    def latir(self):
        print (str(self.__nome) + ' está latindo')
        self.latindo = True


    def parar_latir(self):
        if not self.latindo:
            print(str(self.__nome) +' não está latindo')
            return

        print (str(self.__nome) +' parou de latir')
        self.latindo = False


#gets e sets
    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        self.__nome = nome

    ''''''
    def getRaça(self):
        return self.__raça

    def setRaça(self, raça):
        self.__raça = raça
    
    ''''''
    def getLatindo(self):
        return self.__latindo
    
    def setLatindo(self, latindo):
        self.__latindo = latindo

