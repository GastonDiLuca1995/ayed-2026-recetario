from src.tads.lista_enlazada import ListaEnlazada # Se importa la clase ListaEnlazada desde el módulo lista_enlazada.py, que se encuentra en el paquete src.tads. Esto permite que la clase Pila utilice una lista enlazada para almacenar sus elementos.
from src.excepciones import PilaVaciaError # Se importa la excepción PilaVaciaError desde el módulo excepciones.py, que se encuentra en el paquete src. Esta excepción se utilizará para indicar que se ha intentado desapilar o ver el tope de una pila vacía.

class Pila:
    """TAD pila implementado sobre ListaEnlazada."""

    def __init__(self): # Inicializa la pila vacía, utilizando una instancia de ListaEnlazada para almacenar los elementos.
        self._items = ListaEnlazada()

    def apilar(self, dato): # Agrega un nuevo elemento a la pila. Este método crea un nuevo nodo con el dato proporcionado y lo inserta al inicio de la lista enlazada, que representa el tope de la pila.
        self._items.insertar_al_inicio(dato)

    def desapilar(self): # Elimina y devuelve el elemento en el tope de la pila. Si la pila está vacía, lanza una excepción PilaVaciaError.
        if self.esta_vacia(): # Si la pila está vacía, no hay elementos para desapilar, por lo que se lanza una excepción PilaVaciaError con un mensaje descriptivo.
            raise PilaVaciaError("No hay elementos para desapilar.")
        
        tope = self.ver_tope() # Se obtiene el elemento en el tope de la pila utilizando el método ver_tope(). Este método devuelve el dato del nodo que está en la cabeza de la lista enlazada, que representa el tope de la pila.
        self._items.eliminar(tope) # Se elimina el nodo que contiene el dato del tope de la pila utilizando el método eliminar() de la lista enlazada. Esto "desapila" el elemento de la pila.
        return tope

    def ver_tope(self): # Devuelve el elemento en el tope de la pila sin eliminarlo. Si la pila está vacía, lanza una excepción PilaVaciaError.

        if self.esta_vacia(): # Si la pila está vacía, no hay un elemento en el tope para devolver, por lo que se lanza una excepción PilaVaciaError con un mensaje descriptivo.
            raise PilaVaciaError("La pila está vacía.")
        return self._items._cabeza.dato

    def esta_vacia(self): # Devuelve True si la pila está vacía, es decir, si no hay elementos en ella. Si hay al menos un elemento, devuelve False.
        return self._items.esta_vacia()