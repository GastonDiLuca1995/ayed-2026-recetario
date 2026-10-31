def ordenar_seleccion(coleccion, obtener_clave):   # Ordena revisando todo para encontrar el más chico y pasarlo al frente.
    """
    Ordenamiento por selección (ascendente). 
    Busca el menor elemento del resto de la lista y lo intercambia.
    Complejidad: O(n^2). NO es estable.
    """
    n = len(coleccion)
    for i in range(n - 1):
        pos_min = i
        for j in range(i + 1, n):
            if obtener_clave(coleccion[j]) < obtener_clave(coleccion[pos_min]):
                pos_min = j
        
        coleccion[i], coleccion[pos_min] = coleccion[pos_min], coleccion[i]
        
    return coleccion


def ordenar_insercion(coleccion, obtener_clave):  # Ordena agarrando de a un elemento y corriéndolo hasta encontrar su hueco (funciona exactamente igual a como acomodas las cartas en tu mano).
    """
    Ordenamiento por inserción (ascendente).
    Inserta cada elemento en su posición correcta dentro de la parte ya ordenada.
    Complejidad: O(n^2) peor caso, O(n) mejor caso. SÍ es estable.
    """
    for i in range(1, len(coleccion)):
        actual = coleccion[i]
        j = i - 1
        
        while j >= 0 and obtener_clave(coleccion[j]) > obtener_clave(actual):
            coleccion[j + 1] = coleccion[j]
            j -= 1
            
        coleccion[j + 1] = actual
        
    return coleccion