def busqueda_lineal(coleccion, clave, obtener_clave=None):  # Búsqueda lenta: mira hoja por hoja desde el principio al final.
    """Devuelve el ítem cuya clave coincide, o None."""
    for elemento in coleccion:
        valor_actual = obtener_clave(elemento) if obtener_clave else elemento
        
        if str(valor_actual).lower() == str(clave).lower():
            return elemento
            
    return None


def busqueda_binaria(coleccion_ordenada, clave, obtener_clave):    # Búsqueda súper rápida: parte el libro al medio descartando mitades.
    """La colección tiene que estar ordenada por obtener_clave y soportar índices."""
    izq = 0
    der = len(coleccion_ordenada) - 1
    
    clave_str = str(clave).lower()
    
    while izq <= der:
        medio = (izq + der) // 2
        valor_medio = str(obtener_clave(coleccion_ordenada[medio])).lower()
        
        if valor_medio == clave_str:
            return coleccion_ordenada[medio]
        elif valor_medio < clave_str:
            izq = medio + 1 
        else:
            der = medio - 1  
            
    return None
