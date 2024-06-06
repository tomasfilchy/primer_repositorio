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

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())


def dijkstra(grafo, inicio):
    inicio = inicio.strip()  # Eliminar espacios adicionales
    distancia = {vertice: float('inf') for vertice in grafo.listaVertices}
    distancia[inicio] = 0
    previo = {vertice: None for vertice in grafo.listaVertices}
    cola_prioridad = [(0, inicio)]
    procesados = set()  # Conjunto para rastrear vértices procesados

    while cola_prioridad:
        cola_prioridad.sort(reverse=True)  # Ordenar para simular un min-heap
        dist_actual, vertice_actual = cola_prioridad.pop()

        if vertice_actual in procesados:
            continue  # Saltar vértices ya procesados

        procesados.add(vertice_actual)

        for vecino in grafo.listaVertices[vertice_actual].obtenerConexiones():
            vecino_id = vecino.obtenerId()
            peso = grafo.listaVertices[vertice_actual].obtenerPonderacion(vecino)
            dist_nueva = dist_actual + peso

            if dist_nueva < distancia[vecino_id]:
                distancia[vecino_id] = dist_nueva
                previo[vecino_id] = vertice_actual
                cola_prioridad.append((dist_nueva, vecino_id))

    return distancia, previo


def mostrar_rutas(distancia, previo):
    for vertice in sorted(distancia.keys()):
        if vertice != 'Peligros':
            ruta = []
            actual = vertice
            while actual:
                ruta.append(actual)
                actual = previo[actual]
            ruta.reverse()
            print(f"Aldea: {vertice}, Distancia: {distancia[vertice]}, Ruta: {' -> '.join(ruta)}")


def main():
    grafo = Grafos()

    with open("segundo_tp\\palomas\\aldeas.txt", "r", encoding="utf-8") as archivo:
        aldeas_txt = [x.strip().split(",") for x in archivo.readlines()]
        for i in aldeas_txt:
            grafo.agregarArista(i[0], i[1], i[2])

    # Paso 1: Mostrar la lista de aldeas en orden alfabético
    aldeas_ordenadas = sorted(grafo.obtenerVertices())
    print("Lista de aldeas en orden alfabético:")
    for aldea in aldeas_ordenadas:
        print(aldea)

    # Paso 2: Encontrar la ruta más corta desde "Peligros"
    distancia, previo = dijkstra(grafo, 'Peligros')

    # Paso 3: Mostrar rutas y calcular la suma de todas las distancias
    print("\nRutas más cortas desde 'Peligros':")
    mostrar_rutas(distancia, previo)

    suma_distancias = sum(distancia.values())
    print(f"\nSuma total de todas las distancias: {suma_distancias}")


if __name__ == "__main__":
    main()