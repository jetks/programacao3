def pesquisa_linear(lst, palavra):
    for j in range(len(lst)):
        if lst [j] == palavra:
            return j
    return -1


lst = ['maçã', 'carro', 'roupa', 'cachorro', 'galinha', 'notebook', 'jujuba', 'cacau']
palavra = 'galinha'
print (pesquisa_linear(lst, palavra))
