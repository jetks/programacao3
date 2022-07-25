from aluno import Aluno
from materia import Materia

class Matricula:
    __aluno = None
    __materia = None
    __situacao = None

    def __init__(self, novoAluno, novaMateria, novaSituacao):
        if not isinstance(novoAluno, Aluno):
            raise Exception("Você deve informar um Aluno")
        if not isinstance(novaMateria, Materia):
            raise Exception("Você deve informar uma Materia")

        self.__situacao = novaSituacao
        self.__aluno = novoAluno
        self.__materia = novaMateria


    def getAluno(self):
        return self.__aluno

    def setAluno(self, novoAluno):
        self.__aluno = novoAluno

    def getMateria(self):
        return self.__materia

    def setMateria(self, novaMateria):
        self.__materia = novaMateria

    def getSituacao(self):
        return self.__situacao
    
    def setSituacao(self, novaSituacao):
        self.__situacao = novaSituacao
    
