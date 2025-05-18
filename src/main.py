from simulacion import crear_grafo, propagacion_bfs, propagacion_dfs, detectar_zonas_criticas,detectar_zonas_criticas_peso

def main():
    grafo = crear_grafo()  #Creamos el grafo

    while True:
        print("\nMapa de la red de bosques:\n")
        for zona, conexiones in grafo.items():
            print(f"{zona}: {[f'{vecino} (peso: {peso})' for vecino, peso in conexiones]}")
        print("\n <--- Simulación de propagación de fuego --->")
        print("1. Propagación BFS")
        print("2. Propagación DFS")
        print("3. Detección de zonas críticas")
        print("4. Detección de zonas críticas (por ponderación)")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5):\n")

        if opcion == '1':
            inicio = input("Ingrese la zona de inicio para la propagación BFS:\n")
            if inicio in grafo:
                propagacion_bfs(grafo,inicio)
            else:
                print("Bosque no encontrado en la red. Intente de nuevo.")
        elif opcion == '2':
            inicio = input("Ingrese la zona de inicio para la propagación DFS: \n")
            if inicio in grafo:
                propagacion_dfs(grafo,inicio)
            else:
                print("Bosque no encontrado en la red. Intente de nuevo.")
        elif opcion == '3':
            detectar_zonas_criticas(grafo)
        elif opcion == '4':
            detectar_zonas_criticas_peso(grafo)
        elif opcion == '5':
            print("Saliendo de la simulación...")
            break
    
if __name__ == "__main__":
    main()
