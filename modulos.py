from random import randint
def ordenamientoBurbuja(unaLista):
    for numPasada in range(len(unaLista)):
        for i in range(len(unaLista)-1):
            if unaLista[i]>unaLista[i+1]:
                unaLista[i],unaLista[i+1] = unaLista[i+1],unaLista[i]
unaLista = [randint(10000,99999) for x in range(500)]
ordenamientoBurbuja(unaLista)
print(unaLista)