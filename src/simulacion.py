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
        'Estación1':[('Colomos',19),('Huentitán', 5),('Primavera', 2),('Mirador',9)],
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