from src.tads.lista_enlazada import ListaEnlazada # Se importa la estructura genérica Lista Enlazada que armamos en la carpeta tads
from src.excepciones import ColeccionLlenaError # Se importa la excepción personalizada que definimos para manejar el caso de colección llena

class MenuSemanal:
    def __init__(self, tope=7): # Inicializamos el menú semanal con una lista enlazada vacía y un límite de 7 recetas por defecto
        self._recetas = ListaEnlazada()
        self._tope = tope # El tope es la cantidad máxima de recetas que puede contener el menú semanal.

    def agregar(self, receta):
        """Agrega una receta al menú. Falla si ya hay 7.""" # Si la cantidad de recetas en el menú es mayor o igual al tope, se lanza una excepción.
        if self._recetas.tamanio() >= self._tope:
            raise ColeccionLlenaError(f"El menú semanal está lleno (máximo {self._tope} días).")
        
        self._recetas.insertar_al_final(receta) # Agrega la receta al final de la lista enlazada de recetas.

    def listar(self):
        """Muestra el menú usando el iterador de la lista.""" # Se recorre la lista enlazada de recetas y se imprime cada receta en el menú semanal.
        for r in self._recetas:
            print(f" - {r}")