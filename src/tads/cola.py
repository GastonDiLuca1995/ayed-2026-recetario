from src.tads.lista_enlazada import ListaEnlazada # Se importa la clase ListaEnlazada desde el módulo lista_enlazada.py, que se encuentra en el paquete src.tads. Esto permite que la clase Cola utilice una lista enlazada para almacenar sus elementos.
from src.excepciones import ColaVaciaError # Se importa la excepción ColaVaciaError desde el módulo excepciones.py, que se encuentra en el paquete src. Esta excepción se utilizará para indicar que se ha intentado desencolar o ver el frente de una cola vacía.

class Cola:
    """TAD cola implementado sobre ListaEnlazada."""

    def __init__(self): # Inicializa la cola vacía, utilizando una instancia de ListaEnlazada para almacenar los elementos.
        self._items = ListaEnlazada()

    def encolar(self, dato): # Agrega un nuevo elemento a la cola. Este método crea un nuevo nodo con el dato proporcionado y lo inserta al final de la lista enlazada, que representa el final de la cola.
        self._items.insertar_al_final(dato)

    def desencolar(self): # Elimina y devuelve el elemento en el frente de la cola. Si la cola está vacía, lanza una excepción ColaVaciaError.
        if self.esta_vacia():
            raise ColaVaciaError("No hay elementos en la cola.")
        
        frente = self.ver_frente() # Se obtiene el elemento en el frente de la cola utilizando el método ver_frente(). Este método devuelve el dato del nodo que está en la cabeza de la lista enlazada, que representa el frente de la cola.
        self._items.eliminar(frente) # Se elimina el nodo que contiene el dato del frente de la cola utilizando el método eliminar() de la lista enlazada. Esto "desencola" el elemento de la cola.
        return frente

    def ver_frente(self): # Devuelve el elemento en el frente de la cola sin eliminarlo. Si la cola está vacía, lanza una excepción ColaVaciaError.
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía.")
        return self._items._cabeza.dato

    def esta_vacia(self): # Devuelve True si la cola está vacía, es decir, si no hay elementos en ella. Si hay al menos un elemento, devuelve False.
        return self._items.esta_vacia()