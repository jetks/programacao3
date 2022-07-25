class Materia:
    __nome = None
    __CH = None

    def __init__(self, novoNome, novoCH):
        self.__nome = novoNome
        self.__nasc = novoCH

    def getNome(self):
        return self.__nome

    def getCH (self):
        return self.__CH
    
    def setNome(self, novoNome):
        self.__nome = novoNome

    def setCH (self, novoCH):
        self.__CH = novoCH
