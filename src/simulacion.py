#Definir la estructura del grafo, representado como diccionario
grafo = {
    'Colomos': [('Primavera', 3), ('Huentitán', 6), ('Mirador', 7)],
    'Primavera': [('Colomos', 3), ('Huentitán', 5), ('Mirador', 4)],
    'Huentitán': [('Colomos', 6), ('Primavera', 5), ('Mirador', 8)],
    'Mirador': [('Colomos', 7), ('Primavera', 4), ('Huentitán', 8)]
}

#Solo puse 4 zonas y conexiones entre ellas

#Cada conexión entre dos zonas (una arista del grafo) tiene un peso numérico que representa qué tan fácil o difícil es que el fuego se propague entre esas dos zonas.

    #Ejemplo: 
    #Un incendio que inicia en Colomos: 
    # Tardará moderadamente en llegar a Primavera (peso 4). 
    # Tardará más en llegar a Huentitán (peso 5).

   # | Peso | Significado                       | Ejemplo real                                    |
    #| 1    | Propagación muy fácil             | Vegetación seca, sin barreras, muy cerca        |
    #| 2–3  | Propagación fácil                 | Áreas densas de bosque, misma altitud           |
    #| 4–5  | Propagación media                 | Algo de separación, caminos sin pavimentar      |
    #| 6–7  | Propagación difícil               | Zona húmeda, con ríos, poca continuidad vegetal |
    #| 8+   | Muy difícil o casi imposible      | Autopistas, zonas urbanas, cortafuegos          |
