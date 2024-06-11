class Vertice:
    def __init__(self, clave):
        self.id = clave.strip()  # Eliminar espacios adicionales
        self.conectadoA = {}
        self.mensaje_recibido = False

    def agregarVecino(self, vecino, ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        return str(self.id)

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self, vecino):
        return self.conectadoA[vecino]


class Grafos:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self, clave):
        clave = clave.strip()  # Eliminar espacios adicionales
        if clave not in self.listaVertices:
            self.numVertices += 1
            nuevoVertice = Vertice(clave)
            self.listaVertices[clave] = nuevoVertice
        return self.listaVertices[clave]

    def obtenerVertice(self, n):
        return self.listaVertices.get(n.strip(), None)

    def __contains__(self, n):
        return n.strip() in self.listaVertices

    def agregarArista(self, de, a, costo=0):
        de = de.strip()  # Eliminar espacios adicionales
        a = a.strip()    # Eliminar espacios adicionales
        if de not in self.listaVertices:
            self.agregarVertice(de)
        if a not in self.listaVertices:
            self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], int(costo))
        self.listaVertices[a].agregarVecino(self.listaVertices[de], int(costo))

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())

    def mostrarEnOrden(self):
        listaOrdenada = []
        for vertice in self.listaVertices:
            listaOrdenada.append(vertice)
        listaOrdenada.sort()
        return listaOrdenada
        
def prim(grafo, inicio):
    inicio = inicio.strip()  # Eliminar espacios adicionales
    visitados = set()
    aem = []
    min_heap = [(0, inicio, None)]  # (peso, nodo, nodo_origen)

    while min_heap:
        min_heap.sort(reverse=True)  # Ordenar para simular un min-heap
        peso, vertice_actual, desde = min_heap.pop()

        if vertice_actual in visitados:
            continue

        visitados.add(vertice_actual)
        if desde is not None:
            aem.append((desde, vertice_actual, peso))

        for vecino in grafo.listaVertices[vertice_actual].obtenerConexiones():
            vecino_id = vecino.obtenerId()
            if vecino_id not in visitados:
                peso = grafo.listaVertices[vertice_actual].obtenerPonderacion(vecino)
                min_heap.append((peso, vecino_id, vertice_actual))

    return aem


def mostrar_aem(aem):
    suma = 0 
    for edge in aem:
        suma += edge[2]
        print(f"Desde {edge[0]} hasta {edge[1]} con peso {edge[2]}")
    print(suma)


def main():
    grafo = Grafos()

    with open("segundo_tp\\palomas\\aldeas.txt", "r", encoding="utf-8") as archivo:
        aldeas_txt = [x.strip().split(",") for x in archivo.readlines()]
        for i in aldeas_txt:
            grafo.agregarArista(i[0], i[1], i[2])

    lista = grafo.mostrarEnOrden()
    for linea in lista: print(linea)
    
    aem = prim(grafo, 'Peligros')
    mostrar_aem(aem)
    suma = 0
    for peso in aem:
        suma += peso[2]
   
        
if __name__ == "__main__":
    main()