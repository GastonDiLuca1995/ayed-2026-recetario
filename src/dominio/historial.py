from src.tads.pila import Pila # Se importa la estructura genérica Pila que armamos en la carpeta tads

class Historial:
    def __init__(self): # Inicializamos el historial vacío
        self._acciones = Pila()

    def registrar_accion(self, accion): # Agrega una acción al historial
        self._acciones.apilar(accion)

    def deshacer_accion(self): # Deshace la última acción registrada y la devuelve. Si el historial está vacío, lanza una excepción.
        return self._acciones.desapilar()