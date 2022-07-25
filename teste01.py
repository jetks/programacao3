from matricula import Matricula
from aluno import Aluno
from materia import Materia

def aprovados(lista):
    total = 0
    for Matricula in lista:
        if Matricula.getSituacao() == "A":
            total = total + 1
    return total

a1 = Aluno ("Jéssica", "28/04/2004")
a2 = Aluno ("Lila", "26/03/2000")
a3 = Aluno ("Gumball", "07/02/2001")
a4 = Aluno ("Bela", "14/01/2006")
a5 = Aluno ("Snow", "31/04/2002")

m1 = Materia ("Programação III", 33)
m2 = Materia ("Portugues II", 45)
m3 = Materia ("Filosofia III", 21)
m4 = Materia ("Programação II", 33)

matr1 = Matricula(a1, m4, "A")
matr2 = Matricula(a2, m1, "A")
matr3 = Matricula(a3, m2, "R")
matr4 = Matricula(a4, m4, "R")
matr5 = Matricula(a5, m3, "A")

print (matr1.getAluno().getNome(), matr1.getMateria().getNome(), matr1.getSituacao())
print (matr2.getAluno().getNome(), matr2.getMateria().getNome(), matr2.getSituacao())
print (matr3.getAluno().getNome(), matr3.getMateria().getNome(), matr3.getSituacao())
print (matr4.getAluno().getNome(), matr4.getMateria().getNome(), matr4.getSituacao())
print (matr5.getAluno().getNome(), matr5.getMateria().getNome(), matr5.getSituacao())

matriculas = [matr1, matr2, matr3,matr4, matr5]
aprovados = aprovados(matriculas)
print ("%d estudantes foram aprovados" % (aprovados))
