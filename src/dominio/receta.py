class Receta: # Se crea la clase Receta
    def __init__(self, id_receta, nombre, tiempo_min, dificultad, categoria): # Constructor de la clase Receta
        # Atributos de la clase Receta con sus parametros
        self.id = id_receta
        self.nombre = nombre
        self.tiempo_min = tiempo_min
        self.dificultad = dificultad
        self.categoria = categoria

    def resumen(self): # Devuelve los datos formateados de la receta 
        return f"{self.id:>3}  {self.nombre} - {self.tiempo_min} min ({self.dificultad}) ({self.categoria})"