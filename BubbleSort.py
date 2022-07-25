arq = open("100PalavrasParaOrdenar.txt", "r")
lista = arq.readlines()
for i in range(len(lista)):
    lista[i] = lista [i].rstrip()
arq.close()

def Bubblesort(lista):
    plvr = len(lista)
    for i in range(plvr-1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

Bubblesort(lista)
print(lista)
