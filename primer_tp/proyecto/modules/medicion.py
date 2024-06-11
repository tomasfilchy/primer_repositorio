import time 
import matplotlib.pyplot as plt
from burbuja import ordenamiento_burbuja
from quickSort import ordenamientoRapido
from radixSort import radix_sort 
import random

tamaños = list(range(1, 500))
tiempos_burbuja = []
tiempos_quicksort = []
tiempos_radix = []
fig, ax = plt.subplots()
for tamaño in tamaños:
    lista = [random.randint(10000, 99999) for _ in range(tamaño)]
    lista2 = [str(random.randint(10000, 99999)) for _ in range(tamaño)]
    inicio = time.time()
    ordenamiento_burbuja(lista.copy())
    tiempos_burbuja.append(time.time() - inicio)
    
    inicio = time.time()
    ordenamientoRapido(lista.copy())
    tiempos_quicksort.append(time.time() - inicio)
    
    inicio = time.time()
    radix_sort(lista2.copy())
    tiempos_radix.append(time.time() - inicio)

# Graficar los tiempos de ejecución
ax.plot(tamaños, tiempos_burbuja, label='Burbuja')
ax.plot(tamaños, tiempos_quicksort, label='Quicksort')
ax.plot(tamaños, tiempos_radix, label='Radix Sort')
ax.set_xlabel('Tamaño de la lista')
ax.set_ylabel('Tiempo de ejecución (segundos)')
ax.legend()
plt.show()