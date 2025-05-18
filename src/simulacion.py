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
    # Tardará moderadamente en llegar a Primavera (peso 3). 
    # Tardará más en llegar a Huentitán (peso 6).

   # | Peso | Significado                  
    #| 1    | Propagación muy fácil            
    #| 2–3  | Propagación fácil              
    #| 4–5  | Propagación media                 
    #| 6–7  | Propagación difícil               
    #| 8+   | Muy difícil o casi imposible      

#Función principal que crea el grafo con las zonas y conexiones
#Cada zona es un nodo y cada conexión representa una posible ruta de propagación de fuego
#Los numeros indican qué tan facil o dificil es que el fuego se propague por esa ruta
def crear_grafo():
    grafo = {
        'Colomos': [('Primavera', 3), ('Huentitán', 6), ('Mirador', 7), ('Bomberos_PabloNeruda', 2), ('Bomberos_Central', 5)],
        'Primavera': [('Colomos', 3), ('Huentitán', 5), ('Mirador', 4), ('Bomberos_Zapopan4', 3)],
        'Huentitán': [('Colomos', 6), ('Primavera', 5), ('Mirador', 8), ('Bomberos_Zapopan2', 4), ('Bomberos_Base2', 5)],
        'Mirador': [('Colomos', 7), ('Primavera', 4), ('Huentitán', 8), ('Bomberos_Central', 4)],

        #Estaciones de bomberos
        'Bomberos_Central': [('Colomos', 5), ('Mirador', 4)],
        'Bomberos_Base2': [('Huentitán', 5)],
        'Bomberos_PabloNeruda': [('Colomos', 2)],
        'Bomberos_Zapopan1': [('Primavera', 4)],
        'Bomberos_Zapopan2': [('Huentitán', 4)],
        'Bomberos_Zapopan3': [('Primavera', 5)],
        'Bomberos_Zapopan4': [('Primavera', 3)]
    }
    return grafo

#Algoritmo BFS (anchura)
#Simula cómo se propaga el fuego visitando primero los nodos mas cercanos
#Utiliza una cola para recorrer los nodos en orden de aparicion

def propagacion_bfs(grafo, inicio):
    cola = [inicio]
    visitados = []   #Lista para guardar las zonas ya visitadas

    print("\n[Simulacion BFS] El fuego empieza en:", inicio)

    while cola:
        actual = cola.pop(0)  #Subimos el primer elemento de la cola
        if actual not in visitados:
            print("\nEl fuego ha llegado a: ", actual)
            visitados.append(actual)  #Marcamos la zona como visitada

            for vecino, peso in grafo[actual]:  #Conexiones de esa zona
                if vecino not in visitados and vecino not in cola:
                    print("\nSe propaga a: ", vecino, " , con peso: ", peso)
                    cola.append(vecino)  #Agregamos el vecino a la cola para despues

#Algoritmo DFS (profundidad)
#Simula una propagacion mas profunda como si el fuego siguiera un solo camino primero
#Utiliza recursion y una lista de visitados para no repetir zonas

def propagacion_dfs(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = []  #Lista de zonas visitadas

    if inicio not in visitados:
        print("\nEl fuego ha llegado a: ", inicio)  
        visitados.append(inicio)  #Marcamos como visitada

        for vecino, peso in grafo[inicio]:  #Recorremos los vecinos
            if vecino not in visitados:
                print("\nSe propaga a: ", vecino, " , con peso: ", peso) 
                propagacion_dfs(grafo, vecino, visitados)  #Llamada recursiva para seguir por ese camino


#Funcion para detectar zonas criticas en el grafo
#Una zona critica es aquella que esta conectada a muchas otras con un alto riesgo de propagación

def detectar_zonas_criticas(grafo, umbral=3):
    print("\n[Detección de zonas criticas]")
    for zona in grafo:
        conexiones = len(grafo[zona])  #Numero de vecinos
        if conexiones >= umbral:
            print(f"- {zona} es una zona critica (conectada a {conexiones} zonas)")

"""Función que hace lo mismo que la función anterior solo que en lugar de basarse en las aristas de los nodos,
   se basa en la ponderacion de las aristas"""

def detectar_zonas_criticas_peso(grafo, umbral=17):
    print("\n <--- Deteccion de zonas criticas por ponderacion entre conexiones --->")
    for zona, conexiones in grafo.items():
        peso_total = sum(peso for _, peso in conexiones)
        if peso_total >= umbral:
            print(f"- {zona} es una zona critica (peso total de conexiones: {peso_total})")