class Aluno:
    __nome = None
    __nasc = None

    def __init__(self, novoNome, novoNasc):
        self.__nome = novoNome
        self.__nasc = novoNasc

    def getNome(self):
        return self.__nome

    def setNome(self, novoNome):
        self.__nome = novoNome

    def getNasc (self):
        return self.__nasc
    
    def setNasc (self, novoNasc):
        self.__nasc = novoNasc

    def __str__(self):
        return self.__nome + " - " + self.__nasc
