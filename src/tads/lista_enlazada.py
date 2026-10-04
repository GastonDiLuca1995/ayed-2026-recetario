from src.tads.nodo import Nodo

class ListaEnlazada:
    """TAD lista enlazada simple. No usar list de Python por debajo."""

    def __init__(self): # Inicializa la lista enlazada vacía, con cabeza None y tamaño 0.
        self._cabeza = None
        self._tamanio = 0 # Contador de elementos en la lista.

    def esta_vacia(self): # Devuelve True si la lista está vacía, False si tiene al menos un elemento.
        return self._cabeza is None

    def tamanio(self): # Devuelve la cantidad de elementos en la lista.
        return self._tamanio

    def insertar_al_inicio(self, dato): # Crea un nuevo nodo con el dato y lo engancha al principio de la lista.
        self._cabeza = Nodo(dato, self._cabeza)
        self._tamanio += 1 # Aumenta el contador porque agregamos uno.

    def insertar_al_final(self, dato): # Crea un nuevo nodo con el dato y lo engancha al final de la lista.
        nuevo = Nodo(dato)
        
        if self.esta_vacia(): # Si la lista está vacía, el nuevo nodo pasa a ser la cabeza.
            self._cabeza = nuevo
        else:
            cursor = self._cabeza # Empezamos desde la cabeza y vamos avanzando hasta llegar al último nodo.
            while cursor.siguiente is not None: # Mientras el nodo actual tenga un siguiente, avanzamos al siguiente.
                cursor = cursor.siguiente
            cursor.siguiente = nuevo # Cuando llegamos al último nodo, enganchamos el nuevo nodo al final.
            
        self._tamanio += 1 # Aumentamos el contador.

    def insertar_ordenado(self, dato, clave): 
        raise NotImplementedError

    def eliminar(self, dato): # Este método elimina el primer nodo que contenga el dato especificado.
        if self.esta_vacia(): # Si la lista está vacía, no hay nada que eliminar, así que simplemente retornamos.
            return
            
        if self._cabeza.dato == dato: # Caso 1: El dato está en la cabeza de la lista.
            self._cabeza = self._cabeza.siguiente # Hacemos que la cabeza apunte al siguiente nodo, "saltando" el nodo a eliminar.
            self._tamanio -= 1 # Disminuimos el contador.
            return
            
        cursor = self._cabeza # Caso 2: El dato no está en la cabeza, así que empezamos a recorrer la lista desde la cabeza.
        while cursor.siguiente is not None: # Mientras haya un siguiente nodo para revisar...
            if cursor.siguiente.dato == dato: # Si el siguiente nodo contiene el dato que queremos eliminar...
                cursor.siguiente = cursor.siguiente.siguiente # "Saltamos" el nodo a eliminar, haciendo que el nodo actual apunte al nodo después del siguiente.
                self._tamanio -= 1 # Disminuimos el contador.
                return

            cursor = cursor.siguiente # Si no encontramos el dato en el siguiente nodo, avanzamos al siguiente nodo y repetimos el proceso.

    def buscar(self, dato): # Este método busca un nodo que contenga el dato especificado y devuelve el nodo completo si lo encuentra, o None si no lo encuentra.
        cursor = self._cabeza # Empezamos a revisar desde la cabeza de la lista.
        while cursor is not None: # Mientras haya un nodo actual para revisar...
            if cursor.dato == dato: # Si encontramos el dato en el nodo actual, devolvemos el nodo completo.
                return cursor
            cursor = cursor.siguiente # Si no encontramos el dato en el nodo actual, avanzamos al siguiente nodo y repetimos el proceso.

        return None

    def __iter__(self): # Este método hace que la lista enlazada sea iterable, permitiendo usarla en bucles 'for' y otras construcciones que esperan un iterable.
        cursor = self._cabeza
        while cursor is not None: # Mientras haya un nodo actual para revisar...
            yield cursor.dato # Devolvemos el dato del nodo actual.
            cursor = cursor.siguiente # Avanzamos al siguiente nodo y repetimos el proceso.