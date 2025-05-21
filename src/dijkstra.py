import heapq
#función para encontrar la ruta más corta usando Dijkstra

def encontrar_ruta_mas_corta(grafo, inicio, destino):
    #inicializamos las distancias a infinito y el nodo de inicio a 0
    distancias ={nodo: float("inf")for nodo in grafo}
    distancias[inicio]=0
    anteriores ={nodo: None for nodo in grafo}
    cola=[(0, inicio)]

    while cola:
        distancia_actual, nodo_actual= heapq.heappop(cola)
        for vecino, peso in grafo[nodo_actual]:
            nueva_distancia=distancia_actual+peso
            if nueva_distancia<distancias[vecino]:
                distancias[vecino]=nueva_distancia
                anteriores[vecino]=nodo_actual
                heapq.heappush(cola, (nueva_distancia, vecino))

    #reconstruir el camino
    camino = []
    actual = destino

    while actual and actual !=inicio:
        camino.insert(0, actual)
        actual=anteriores[actual]
    if actual==inicio:
        camino.insert(0, inicio)

        #mostrar resultads
    if distancias[destino]==float("inf"):
        print(f"\nNo hay ruta posible de {inicio}a{destino}.")
    else:
        print(f"\nRuta más corta de {inicio} a {destino}: {' -> '.join(camino)}")
        print(f"Distancia total:{distancias[destino]}")