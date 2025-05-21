# mapa-incendios-gdl
Simulación con grafos para modelar riesgo de incendios forestales en Guadalajara

Este proyecto utiliza grafos en Python para simular la propagación de incendios forestales en zonas naturales del Área Metropolitana de Guadalajara. Está orientado a apoyar a instituciones de protección civil para mejorar la prevención y respuesta ante incendios.

## Objetivo del Proyecto

Modelar zonas forestales como nodos en un grafo, simular la expansión del fuego con algoritmos de búsqueda (BFS y DFS), y proponer conexiones estratégicas con estaciones de bomberos o sistemas de monitoreo.

# Menú de simulación y funcionalidades

1. **Propagación BFS (Busqueda en anchura)**
   Simula como se propaga un incendio forestal, explorando todas las rutas posibles desde la zona de inicio hacia otras zonas conectadas. Nos ayuda a visualizar una propagación simultanea.

2. **Propagación DFS (Búsqueda en profundidad)**
   Simula la propagación del incendio siguiendo un solo camino a la vez, profundizando en cada ramificación antes de retroceder. Nos muestra una propagación más dirigida.

3. **Detención de zonas críticas**
   Analiza las conexiones entre bosques y detecta aquellas zonas con riesgo elevado de propagación basándose en la suma de los pesos. Identifica los puntos más vunerables.

4. **Ruta más corta (algoritmia de Dijkstra)**
   Calcula el camino más eficiente entre una estación de bomberos y una zona forestal. Esta función ayuda a planificar una respuesta rápida ante emergencias.
5. **Salir**
   Cierra la simulación.

Todas estas funciones permiten evaluar riesgos y planificar estrategias efectivas para actuar frente a incendios forestales.

## Equipo

- Ana Laura Gomez Melgoza (@AnaLauraGomez)
- Arambula Cruz Gabriela Jireh (@gabi055)
- Andres Hernandez Margarita (@usuarioGitHub)

## ¿Cómo ejecutar el proyecto?
Clona el repositorio:
Abre GitBash y escribe:

git clone https://github.com/tuUsuario/mapa-incendios-gdl.git
cd mapa-incendios-gdl
code .

