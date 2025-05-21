import matplotlib.pyplot as plt
import networkx as nx

#Definir la estructura del grafo, representado como diccionario
"""
grafo = {
    'Colomos': [('Primavera', 3), ('Huentitán', 6), ('Mirador', 7)],
    'Primavera': [('Colomos', 3), ('Huentitán', 5), ('Mirador', 4)],
    'Huentitán': [('Colomos', 6), ('Primavera', 5), ('Mirador', 8)],
    'Mirador': [('Colomos', 7), ('Primavera', 4), ('Huentitán', 8)]
}
"""

#Solo puse 4 zonas y conexiones entre ellas

    #Ejemplo: 
    #Un incendio que inicia en Colomos: 
    # Tardará más en llegar a Primavera (peso 3). 
    # Tardará mucho menos en llegar a Huentitán (peso 5).

"""Para aplica ponderación, hicimos uso de la formula inversa  simple donde
   el peso de la arista es inversamente proporcional a la distancia entre los nodos.
   Por lo tanto, a mayor distancia entre los nodos, menor será el peso de la arista."""    

#Función principal que crea el grafo con las zonas y conexiones
#Cada zona es un nodo y cada conexión representa una posible ruta de propagación de fuego
#Los numeros indican qué tan facil o dificil es que el fuego se propague por esa ruta
def crear_grafo():
    grafo = {
        #Bosques
        'Colomos': [('Primavera', 3), ('Huentitán', 5), ('Mirador', 8)],
        'Primavera': [('Colomos', 3), ('Huentitán', 1), ('Mirador', 2)],
        'Huentitán': [('Colomos', 5), ('Primavera', 1), ('Mirador', 8)],
        'Mirador': [('Colomos', 8), ('Primavera', 2), ('Huentitán', 8)],

        #Estaciones de bomberos conectadas a los bosques
        #Cuartel Central
        'Cuartel Central':[('Colomos',11),('Huentitán', 6),('Primavera', 3),('Mirador',9)],
        #Unidad Estatal de Protección Civil y Bomberos Jalisco 
        'UEPCBJ':[('Colomos',7),('Huentitán', 4),('Primavera', 3),('Mirador',6)],
        #Coordinación Municipal De Protección Civil Y Bomberos De Zapopan (Base 1) Oficinas Administrativas
        'Estacion1':[('Colomos',19),('Huentitán', 5),('Primavera', 2),('Mirador',9)],
        #Base 2 Protección Civil y Bomberos Zapopan, Los Molinos
        'Estacion2':[('Colomos',4),('Huentitán', 3),('Primavera', 2),('Mirador',3)],
        #Base 3 Protección Civil y Bomberos Zapopan, Auditorio
        'Estacion3':[('Colomos',12),('Huentitán', 6),('Primavera', 2),('Mirador',14)],
        #Coordinación Municipal De Protección Civil Y Bomberos De Zapopan (Base 4)
        'Estacion4':[('Colomos',6),('Huentitán', 3),('Primavera', 4),('Mirador',4)]
        
    }
    return grafo

#Algoritmo BFS (anchura)
#Simula cómo se propaga el fuego visitando primero los nodos mas cercanos
#Utiliza una cola para recorrer los nodos en orden de aparicion

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

#Algoritmo DFS (profundidad)
#Simula una propagacion mas profunda como si el fuego siguiera un solo camino primero
#Utiliza recursion y una lista de visitados para no repetir zonas

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



"""Función que detecta zonas criticas mediante las aristas de los nodos,
   se basa en la ponderacion de las aristas. Una zona critica es aquella que tiene un peso total de conexiones menor a un umbral dado, la zona es
   aquella que tiene un alto riesgo de propagación de fuego."""

def detectar_zonas_criticas_peso(grafo, umbral=15):
    bosques = ['Colomos', 'Primavera', 'Huentitán', 'Mirador']
    print("\n <--- Deteccion de zonas criticas por ponderacion entre conexiones --->")
    for zona in bosques:
        conexiones = grafo.get(zona, [])
        peso_total = sum(peso for _, peso in conexiones)
        if peso_total > umbral:
            print(f"- {zona} es una zona critica (peso total de conexiones: {peso_total})")


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
