import matplotlib.pyplot as plt
import networkx as nx
import heapq


# <---Función principal que crea el grafo con los bosques, estaciones de bomberos y conexiones ----->
"""Cada zona es un nodo y cada conexión representa una arista entre nodos. Esta arista tiene un peso que indica la 
   distancia entre los nodos(Distancia entres bosques y estaciones de bomberos).
   El grafo es un diccionario donde cada clave es un nodo y su valor es una lista de tuplas que representan los nodos vecinos y el peso de la arista.
   Las estaciones de bomberos están conectadas a los bosques y entre ellas, lo que permite simular la propagación del fuego y la respuesta de los bomberos."""

def crear_grafo():
    grafo = {
        #Bosques
        'Colomos': [('Primavera', 4), ('Huentitán', 3), ('Mirador', 2)],
        'Primavera': [('Colomos', 4), ('Huentitán', 8), ('Mirador', 7)],
        'Huentitán': [('Colomos', 3), ('Primavera', 8), ('Mirador', 2)],
        'Mirador': [('Colomos', 2), ('Primavera', 7), ('Huentitán', 2)],

        #Estaciones de bomberos conectadas a los bosques
        #Cuartel Central
        'Cuartel Central':[('Colomos',1),('Huentitán', 2),('Primavera', 4),('Mirador',2)],
        #Unidad Estatal de Protección Civil y Bomberos Jalisco 
        'UEPCBJ':[('Colomos',2),('Huentitán', 4),('Primavera', 4),('Mirador',2)],
        #Coordinación Municipal De Protección Civil Y Bomberos De Zapopan (Base 1) Oficinas Administrativas
        'Estacion1':[('Colomos',1),('Huentitán', 3),('Primavera', 5),('Mirador',2)],
        #Base 2 Protección Civil y Bomberos Zapopan, Los Molinos
        'Estacion2':[('Colomos',3),('Huentitán', 5),('Primavera', 7),('Mirador',4)],
        #Base 3 Protección Civil y Bomberos Zapopan, Auditorio
        'Estacion3':[('Colomos',1),('Huentitán', 2),('Primavera', 6),('Mirador',1)],
        #Coordinación Municipal De Protección Civil Y Bomberos De Zapopan (Base 4)
        'Estacion4':[('Colomos',2),('Huentitán', 5),('Primavera', 3),('Mirador',3)]
        
    }
    return grafo

# <--- Algoritmo BFS (anchura) --->
"""Simula cómo se propaga el fuego visitando primero los nodos mas cercanos.
   Utiliza una cola para recorrer los nodos en orden de aparición. 
   Se utiliza una lista de visitados para evitar visitar la misma zona más de una vez."""

def propagacion_bfs(grafo, inicio):
    bosques = ['Colomos', 'Primavera', 'Huentitán', 'Mirador']
    if inicio not in bosques:
        print(f"\nZona no válida. Debe ser una de las siguientes: {bosques}")
        return
    
    cola = [inicio]
    visitados = []   #Lista para guardar las zonas ya visitadas

    print("\n[Simulacion BFS] El fuego empieza en:", inicio)

    while cola:
        actual = cola.pop(0)  #Subimos el primer elemento de la cola
        if actual not in visitados:
            print("\nEl fuego ha llegado a: ", actual)
            visitados.append(actual)  #Marcamos la zona como visitada

            for vecino, peso in grafo[actual]:  #Conexiones de esa zona
                if vecino in bosques and vecino not in visitados and vecino not in cola:
                    print("\nSe propaga a: ", vecino, " , con peso: ", peso)
                    cola.append(vecino)  #Agregamos el vecino a la cola para despues

# <---Algoritmo DFS (profundidad)--->
"""Simula una propagación más profunda como si el fuego siguiera un solo camino primero.
   Utiliza recursión y una lista de visitados para no repetir zonas."""

def propagacion_dfs(grafo, inicio, visitados=None):
    bosques = ['Colomos', 'Primavera', 'Huentitán', 'Mirador']
    if inicio not in bosques:
        print(f"\nZona no válida. Debe ser una de las siguientes: {bosques}")
        return
    
    if visitados is None:
        visitados = []  #Lista de zonas visitadas

    if inicio not in visitados:
        print("\nEl fuego ha llegado a: ", inicio)  
        visitados.append(inicio)  #Marcamos como visitada

        for vecino, peso in grafo[inicio]:  #Recorremos los vecinos
            if vecino in bosques and vecino not in visitados:
                print("\nSe propaga a: ", vecino, " , con peso: ", peso) 
                propagacion_dfs(grafo, vecino, visitados)  #Llamada recursiva para seguir por ese camino


# <--- Detección de zonas críticas por ponderación entre conexiones --->
"""Detecta zonas criticas mediante las aristas de los nodos.
    Si el peso total de las conexiones de un bosque es menor a un umbral dado, se considera una zona crítica,
    ya que cuenta con una distancia corta a otras zonas aumentado la rapidez de la propagación.
    La zona crítica es aquella que tiene un alto riesgo de propagación de fuego."""

def detectar_zonas_criticas_peso(grafo, umbral=13):
    bosques = ['Colomos', 'Primavera', 'Huentitán', 'Mirador']
    print("\n <--- Deteccion de zonas criticas por ponderacion entre conexiones --->")
    for zona in bosques:
        conexiones = grafo.get(zona, [])
        peso_total = sum(peso for _, peso in conexiones)
        if peso_total < umbral:
            print(f"- {zona} es una zona critica (peso total de conexiones: {peso_total})")


# <--- Algoritmo de Dijkstra para encontrar la ruta más corta entre dos nodos --->
"""Busca la ruta más corta entre un bosque y una estación de bomberos.
   Utiliza una cola de prioridad para explorar los nodos más cercanos primero.
   Mantiene un registro de las distancias más cortas encontradas hasta el momento y reconstruye la ruta más corta al final.
   Además de mostrar la ruta, también visualiza el grafo con la ruta y las distancias."""

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

    #Reconstruir el camino
    camino = []
    actual = destino

    while actual and actual !=inicio:
        camino.insert(0, actual)
        actual=anteriores[actual]
    if actual==inicio:
        camino.insert(0, inicio)

        #Mostrar resultados
    if distancias[destino]==float("inf"):
        print(f"\nNo hay ruta posible de {inicio}a{destino}.")
    else:
        print(f"\nRuta más corta de {inicio} a {destino}: {' -> '.join(camino)}")
        print(f"Distancia total:{distancias[destino]}")
    
    #Vizualizar la ruta más corta
    G = nx.Graph()
    for nodo, conexiones in grafo.items():
        for vecino, peso in conexiones:
            G.add_edge(nodo, vecino, weight=peso)
    pos = nx.spring_layout(G)
   
   #Dibujar el grafo
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    ruta_edges = [(camino[i], camino[i + 1]) for i in range(len(camino) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=ruta_edges, edge_color='red', width=2)
   
    edge_labels_ruta = {(camino[i], camino[i + 1]): G[camino[i]][camino[i+1]]['weight'] for i in range(len(camino)-1)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels_ruta, font_color='green')
    plt.title(f"Ruta más corta de {inicio} a {destino}")
    plt.show()
