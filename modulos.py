#from random import randint
#def ordenamientoBurbuja(unaLista):
#    for numPasada in range(len(unaLista)):
#        for i in range(len(unaLista)-1):
#            if unaLista[i]>unaLista[i+1]:
#                unaLista[i],unaLista[i+1] = unaLista[i+1],unaLista[i]
#unaLista = [randint(1,20) for x in range(10)]
#print(unaLista)
##ordenamientoBurbuja(unaLista)
##print(unaLista)
#
#def ordenamientoRapido(unaLista):
#   ordenamientoRapidoAuxiliar(unaLista,0,len(unaLista)-1)
#
#def ordenamientoRapidoAuxiliar(unaLista,primero,ultimo):
#   if primero<ultimo:
#
#       puntoDivision = particion(unaLista,primero,ultimo)
#
#       ordenamientoRapidoAuxiliar(unaLista,primero,puntoDivision-1)
#       ordenamientoRapidoAuxiliar(unaLista,puntoDivision+1,ultimo)
#
#
#def particion(unaLista,primero,ultimo):
#   valorPivote = unaLista[primero]
#   marcaIzq = primero+1
#   marcaDer = ultimo
#
#   hecho = False
#   while not hecho:
#
#       while marcaIzq <= marcaDer and unaLista[marcaIzq] <= valorPivote:
#           marcaIzq = marcaIzq + 1
#
#
#       while unaLista[marcaDer] >= valorPivote and marcaDer >= marcaIzq:
#           marcaDer = marcaDer -1
#       if marcaDer < marcaIzq:
#           hecho = True
#       else:
#           unaLista[marcaDer],unaLista[marcaIzq]=unaLista[marcaIzq], unaLista[marcaDer]
#  
#   unaLista[primero], unaLista[marcaDer] = unaLista[marcaDer], valorPivote
#
#
#   return marcaDer
#
#ordenamientoRapido(unaLista)
#print(unaLista)
from random import randint 


def radixSort(lista):
    n = 0
    for e in lista:
        if len(e) > n :
            n = len(e)
            
    for i in range(0, len(lista)):
        while len(lista[i]) < n:
            lista [i] = "0" + lista[i]
            
    for j in range(n - 1, -1, -1):
        grupos = [[]for i in range(10)]
        
        for i in range(len(lista)):
            grupos[int(lista[i][j])].append(lista[i])
            
            
        lista = []
        for g in grupos:
            lista+=g
        
    return [int(i) for i in lista]
        
        
listaNumeros = [randint(1,99999) for x in range(12)]
listaCadenas = []
for n in listaNumeros:
    listaCadenas.append(str(n))

print(listaCadenas)
print(radixSort(listaCadenas))