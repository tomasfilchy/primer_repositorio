from random import randint
def radixSort(lista):
    n = 0 
    for e in lista:
        if len(e) > n:
            n = len(e)
    
    for i in range(0, len(lista)):
        while len(lista[i]) < n:
            lista[i] = "0" + lista[i]

    for j in range(n -1, -1, -1):
        grupos = [[] for x in range(10)]
        for i in range(len(lista)):
            grupos[int(lista[i][j])].append(lista[i])
        lista= []
        for g in grupos:
            lista += g
            
    return [int(i) for i in lista]
            
    
lista = [str(randint(10000,99999)) for x in range(10)]
            
lista = radixSort(lista)
print(lista)