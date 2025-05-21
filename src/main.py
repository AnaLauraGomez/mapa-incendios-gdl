from simulacion import crear_grafo, propagacion_bfs, propagacion_dfs,detectar_zonas_criticas_peso
from dijkstra import encontrar_ruta_mas_corta


def main():
    grafo = crear_grafo()  #Creamos el grafo
    bosques = ['Colomos', 'Primavera', 'Huentitán', 'Mirador']
    estaciones=['Cuartel Central', 'UEPCBJ','Estación1','Estación2','Estación3','Estación4']

    while True:
        print("\nMapa de la red de bosques:\n")
        for zona, conexiones in grafo.items():
            if zona in bosques:
                print(f"{zona}: {[f'{vecino} (peso: {peso})' for vecino, peso in conexiones]}")

        print("\n <--- Simulacion de propagacion de fuego --->")
        print("1. Propagacion BFS")
        print("2. Propagacion DFS")
        print("3. Deteccion de zonas criticas")
        print("4. Ruta más corta (Dijkstra)")
        print("5. Salir")

        opcion = input("Seleccione una opcion (1-5):\n")

        if opcion == '1':
            inicio = input("\nIngrese la zona de inicio para la propagacion BFS:\n")
            if inicio in bosques:
                propagacion_bfs(grafo,inicio)
            else:
                print("\nBosque no encontrado en la red. Intente de nuevo.")
        elif opcion == '2':
            inicio = input("\nIngrese la zona de inicio para la propagacion DFS: \n")
            if inicio in bosques:
                propagacion_dfs(grafo,inicio)
            else:
                print("\nBosque no encontrado en la red. Intente de nuevo.")
        elif opcion == '3':
            detectar_zonas_criticas_peso(grafo)
        elif opcion == '4':
            origen=input("\nIngrese la estación de bomberos de origen:\n")
            destino=input("Ingrese la zona forestal destino:\n")
            if origen in estaciones and destino in bosques:
                encontrar_ruta_mas_corta(grafo,origen,destino)
            else:
                print("\nNombre invalidos. Asegurate de escribirlo bien la estacion y el bosque.")
        elif opcion== '5':
            print("\nSaliendo de la simulacion...")
            break
        else:
            print("\nOpcion no valida. Intente de nuevo.")
    
if __name__ == "__main__":
    main()
