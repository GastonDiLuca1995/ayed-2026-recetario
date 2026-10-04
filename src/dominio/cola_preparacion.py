from src.tads.cola import Cola # Importamos la estructura genérica Cola que armamos en la carpeta tads

class ColaPreparacion:
    def __init__(self): # Inicializamos la cola de pedidos vacía
        self._pedidos = Cola()

    def agregar_pedido(self, plato): # Agrega un plato a la cola de preparación
        self._pedidos.encolar(plato)

    def cocinar_proximo(self): # Cocina el próximo plato en la cola de preparación y lo devuelve. Si la cola está vacía, lanza una excepción.
        return self._pedidos.desencolar()