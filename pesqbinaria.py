#arq = open ("palavras.txt", "r")
#lista = arq.readlines()
 #for i in range (len(lista)):
 #    lista [i] = lista[i].rstrip()
#arq.close()
def pesquisa_binaria (lst, palavra, inicio, final):
    if inicio > final:
        return -1
    meio = (inicio + final)//2
    #print(lst[meio])
    if lst[meio] == palavra:
        return meio
    elif lst[meio] > palavra:
        final = meio - 1
        return pesquisa_binaria (lst, palavra, inicio, final)
    else:
        inicio = meio + 1
        return pesquisa_binaria (lst, palavra, inicio, final)
        

lst = ['amor', 'baixinho', 'coracao', 'docinho', 'escola', 'feijao', 'gente', 'humano']
inicio = 0
final = len(lst)-1
palavra = 'docinho'
print (pesquisa_binaria(lst, palavra, inicio, final))
