from src.dominio.receta import Receta # Se importa la clase Receta desde nuestro otro archivo.
from src.tads.lista_enlazada import ListaEnlazada # Se importa la clase ListaEnlazada para poder usarla en nuestro recetario.

class Recetario: # Definimos la clase Recetario para crear nuestro catálogo completo.
    def __init__(self): # Este es el constructor de la clase Recetario.
        self.recetas = ListaEnlazada() # Se inicializa la lista de recetas como una lista enlazada vacía.
        self.ingredientes = [] # Se inicializa la lista de ingredientes como una lista vacía.
        self.subrecetas = [] # Se inicializa la lista de subrecetas como una lista vacía.

    def cargar_datos(self):  # Este método carga los datos de recetas, ingredientes y subrecetas en el recetario.
        # Creamos una lista de diccionarios, cada uno representando una receta con sus atributos.
        lista_recetas = [
            {"id": 1, "nombre": "Chimichurri", "tiempo_min": 15, "dificultad": "baja", "categoria": "salsa"},
            {"id": 2, "nombre": "Salsa criolla", "tiempo_min": 20, "dificultad": "baja", "categoria": "salsa"},
            {"id": 3, "nombre": "Sofrito", "tiempo_min": 25, "dificultad": "baja", "categoria": "base"},
            {"id": 4, "nombre": "Puré de papas", "tiempo_min": 30, "dificultad": "baja", "categoria": "acompañamiento"},
            {"id": 5, "nombre": "Masa de empanadas", "tiempo_min": 90, "dificultad": "media", "categoria": "base"},
            {"id": 6, "nombre": "Masa de pizza", "tiempo_min": 120, "dificultad": "media", "categoria": "base"},
            {"id": 7, "nombre": "Pesto", "tiempo_min": 15, "dificultad": "baja", "categoria": "salsa"},
            {"id": 8, "nombre": "Pico de gallo", "tiempo_min": 15, "dificultad": "baja", "categoria": "salsa"},
            {"id": 9, "nombre": "Asado", "tiempo_min": 180, "dificultad": "media", "categoria": "principal"},
            {"id": 10, "nombre": "Empanadas de carne", "tiempo_min": 150, "dificultad": "media", "categoria": "principal"},
            {"id": 11, "nombre": "Milanesa napolitana", "tiempo_min": 50, "dificultad": "media", "categoria": "principal"},
            {"id": 12, "nombre": "Locro", "tiempo_min": 150, "dificultad": "alta", "categoria": "principal"},
            {"id": 13, "nombre": "Pizza muzzarella", "tiempo_min": 140, "dificultad": "media", "categoria": "principal"},
            {"id": 14, "nombre": "Choripán", "tiempo_min": 25, "dificultad": "baja", "categoria": "principal"},
            {"id": 15, "nombre": "Flan casero", "tiempo_min": 70, "dificultad": "media", "categoria": "postre"},
            {"id": 16, "nombre": "Panqueques con dulce de leche", "tiempo_min": 40, "dificultad": "baja", "categoria": "postre"},
            {"id": 17, "nombre": "Tacos de carne", "tiempo_min": 40, "dificultad": "baja", "categoria": "principal"},
            {"id": 18, "nombre": "Guacamole", "tiempo_min": 15, "dificultad": "baja", "categoria": "entrada"},
            {"id": 19, "nombre": "Pasta con salsa fileto", "tiempo_min": 45, "dificultad": "baja", "categoria": "principal"},
            {"id": 20, "nombre": "Ñoquis con pesto", "tiempo_min": 50, "dificultad": "media", "categoria": "principal"},
            {"id": 21, "nombre": "Tortilla de papas", "tiempo_min": 40, "dificultad": "media", "categoria": "principal"},
            {"id": 22, "nombre": "Pollo al horno con papas", "tiempo_min": 70, "dificultad": "baja", "categoria": "principal"},
            {"id": 23, "nombre": "Sopa de calabaza", "tiempo_min": 40, "dificultad": "baja", "categoria": "entrada"},
            {"id": 24, "nombre": "Arroz con leche", "tiempo_min": 45, "dificultad": "baja", "categoria": "postre"},
            {"id": 25, "nombre": "Brownies", "tiempo_min": 50, "dificultad": "media", "categoria": "postre"},
            {"id": 26, "nombre": "Humita", "tiempo_min": 60, "dificultad": "media", "categoria": "principal"},
            {"id": 27, "nombre": "Hamburguesa casera", "tiempo_min": 35, "dificultad": "baja", "categoria": "principal"},
            {"id": 28, "nombre": "Ensalada rusa", "tiempo_min": 35, "dificultad": "baja", "categoria": "entrada"},
            {"id": 29, "nombre": "Curry de garbanzos", "tiempo_min": 40, "dificultad": "baja", "categoria": "principal"},
            {"id": 30, "nombre": "Risotto de hongos", "tiempo_min": 45, "dificultad": "alta", "categoria": "principal"}
        ]
        for i in lista_recetas: # Recorremos la lista de recetas y creamos un objeto Receta para cada diccionario, luego lo agregamos a la lista de recetas del recetario.
            # Creamos un objeto Receta usando los datos del diccionario y lo agregamos a la lista de recetas del recetario.
            nueva_receta = Receta(i["id"], i["nombre"], i["tiempo_min"], i["dificultad"], i["categoria"])

            self.recetas.insertar_al_final(nueva_receta) # Agregamos la nueva receta al final de la lista de recetas del recetario.

        # Listas de ingredientes
        self.ingredientes = [
            {"id_receta": 1, "nombre": "perejil", "cantidad": 50, "unidad": "g"},
            {"id_receta": 1, "nombre": "ajo", "cantidad": 4, "unidad": "dientes"},
            {"id_receta": 1, "nombre": "orégano", "cantidad": 5, "unidad": "g"},
            {"id_receta": 1, "nombre": "aceite de oliva", "cantidad": 80, "unidad": "ml"},
            {"id_receta": 1, "nombre": "vinagre", "cantidad": 30, "unidad": "ml"},
            {"id_receta": 1, "nombre": "ají molido", "cantidad": 5, "unidad": "g"},
            {"id_receta": 2, "nombre": "tomate", "cantidad": 3, "unidad": "u"},
            {"id_receta": 2, "nombre": "cebolla", "cantidad": 1, "unidad": "u"},
            {"id_receta": 2, "nombre": "morrón", "cantidad": 1, "unidad": "u"},
            {"id_receta": 2, "nombre": "aceite de oliva", "cantidad": 40, "unidad": "ml"},
            {"id_receta": 2, "nombre": "vinagre", "cantidad": 20, "unidad": "ml"},
            {"id_receta": 3, "nombre": "cebolla", "cantidad": 2, "unidad": "u"},
            {"id_receta": 3, "nombre": "zanahoria", "cantidad": 1, "unidad": "u"},
            {"id_receta": 3, "nombre": "ajo", "cantidad": 2, "unidad": "dientes"},
            {"id_receta": 3, "nombre": "aceite", "cantidad": 30, "unidad": "ml"},
            {"id_receta": 4, "nombre": "papa", "cantidad": 800, "unidad": "g"},
            {"id_receta": 4, "nombre": "leche", "cantidad": 100, "unidad": "ml"},
            {"id_receta": 4, "nombre": "manteca", "cantidad": 40, "unidad": "g"},
            {"id_receta": 4, "nombre": "sal", "cantidad": 5, "unidad": "g"},
            {"id_receta": 5, "nombre": "harina", "cantidad": 500, "unidad": "g"},
            {"id_receta": 5, "nombre": "grasa", "cantidad": 100, "unidad": "g"},
            {"id_receta": 5, "nombre": "agua", "cantidad": 150, "unidad": "ml"},
            {"id_receta": 5, "nombre": "sal", "cantidad": 8, "unidad": "g"},
            {"id_receta": 6, "nombre": "harina", "cantidad": 500, "unidad": "g"},
            {"id_receta": 6, "nombre": "agua", "cantidad": 300, "unidad": "ml"},
            {"id_receta": 6, "nombre": "levadura", "cantidad": 10, "unidad": "g"},
            {"id_receta": 6, "nombre": "aceite", "cantidad": 20, "unidad": "ml"},
            {"id_receta": 6, "nombre": "sal", "cantidad": 8, "unidad": "g"},
            {"id_receta": 7, "nombre": "albahaca", "cantidad": 80, "unidad": "g"},
            {"id_receta": 7, "nombre": "ajo", "cantidad": 1, "unidad": "dientes"},
            {"id_receta": 7, "nombre": "piñones", "cantidad": 30, "unidad": "g"},
            {"id_receta": 7, "nombre": "queso parmesano", "cantidad": 40, "unidad": "g"},
            {"id_receta": 7, "nombre": "aceite de oliva", "cantidad": 80, "unidad": "ml"},
            {"id_receta": 8, "nombre": "tomate", "cantidad": 3, "unidad": "u"},
            {"id_receta": 8, "nombre": "cebolla", "cantidad": 1, "unidad": "u"},
            {"id_receta": 8, "nombre": "cilantro", "cantidad": 20, "unidad": "g"},
            {"id_receta": 8, "nombre": "lima", "cantidad": 1, "unidad": "u"},
            {"id_receta": 8, "nombre": "sal", "cantidad": 3, "unidad": "g"},
            {"id_receta": 9, "nombre": "vacío", "cantidad": 1200, "unidad": "g"},
            {"id_receta": 9, "nombre": "chorizo", "cantidad": 4, "unidad": "u"},
            {"id_receta": 9, "nombre": "sal gruesa", "cantidad": 20, "unidad": "g"},
            {"id_receta": 10, "nombre": "carne picada", "cantidad": 500, "unidad": "g"},
            {"id_receta": 10, "nombre": "huevo", "cantidad": 1, "unidad": "u"},
            {"id_receta": 10, "nombre": "comino", "cantidad": 3, "unidad": "g"},
            {"id_receta": 11, "nombre": "milanesa de ternera", "cantidad": 4, "unidad": "u"},
            {"id_receta": 11, "nombre": "salsa de tomate", "cantidad": 200, "unidad": "ml"},
            {"id_receta": 11, "nombre": "muzzarella", "cantidad": 250, "unidad": "g"},
            {"id_receta": 11, "nombre": "jamón", "cantidad": 150, "unidad": "g"},
            {"id_receta": 12, "nombre": "maíz blanco", "cantidad": 300, "unidad": "g"},
            {"id_receta": 12, "nombre": "poroto", "cantidad": 200, "unidad": "g"},
            {"id_receta": 12, "nombre": "zapallo", "cantidad": 400, "unidad": "g"},
            {"id_receta": 12, "nombre": "chorizo colorado", "cantidad": 200, "unidad": "g"},
            {"id_receta": 13, "nombre": "muzzarella", "cantidad": 400, "unidad": "g"},
            {"id_receta": 13, "nombre": "salsa de tomate", "cantidad": 150, "unidad": "ml"},
            {"id_receta": 13, "nombre": "orégano", "cantidad": 5, "unidad": "g"},
            {"id_receta": 14, "nombre": "chorizo", "cantidad": 4, "unidad": "u"},
            {"id_receta": 14, "nombre": "pan", "cantidad": 4, "unidad": "u"},
            {"id_receta": 15, "nombre": "huevo", "cantidad": 4, "unidad": "u"},
            {"id_receta": 15, "nombre": "leche", "cantidad": 400, "unidad": "ml"},
            {"id_receta": 15, "nombre": "azúcar", "cantidad": 120, "unidad": "g"},
            {"id_receta": 15, "nombre": "esencia de vainilla", "cantidad": 5, "unidad": "ml"},
            {"id_receta": 16, "nombre": "harina", "cantidad": 150, "unidad": "g"},
            {"id_receta": 16, "nombre": "leche", "cantidad": 250, "unidad": "ml"},
            {"id_receta": 16, "nombre": "huevo", "cantidad": 2, "unidad": "u"},
            {"id_receta": 16, "nombre": "dulce de leche", "cantidad": 200, "unidad": "g"},
            {"id_receta": 17, "nombre": "carne", "cantidad": 400, "unidad": "g"},
            {"id_receta": 17, "nombre": "tortilla de maíz", "cantidad": 8, "unidad": "u"},
            {"id_receta": 18, "nombre": "palta", "cantidad": 3, "unidad": "u"},
            {"id_receta": 18, "nombre": "lima", "cantidad": 1, "unidad": "u"},
            {"id_receta": 18, "nombre": "sal", "cantidad": 3, "unidad": "g"},
            {"id_receta": 19, "nombre": "fideos", "cantidad": 400, "unidad": "g"},
            {"id_receta": 19, "nombre": "tomate", "cantidad": 400, "unidad": "g"},
            {"id_receta": 20, "nombre": "papa", "cantidad": 800, "unidad": "g"},
            {"id_receta": 20, "nombre": "harina", "cantidad": 200, "unidad": "g"},
            {"id_receta": 20, "nombre": "huevo", "cantidad": 1, "unidad": "u"},
            {"id_receta": 21, "nombre": "papa", "cantidad": 600, "unidad": "g"},
            {"id_receta": 21, "nombre": "huevo", "cantidad": 6, "unidad": "u"},
            {"id_receta": 21, "nombre": "cebolla", "cantidad": 1, "unidad": "u"},
            {"id_receta": 22, "nombre": "pollo", "cantidad": 1200, "unidad": "g"},
            {"id_receta": 22, "nombre": "papa", "cantidad": 800, "unidad": "g"},
            {"id_receta": 22, "nombre": "aceite", "cantidad": 30, "unidad": "ml"},
            {"id_receta": 22, "nombre": "provenzal", "cantidad": 10, "unidad": "g"},
            {"id_receta": 23, "nombre": "calabaza", "cantidad": 800, "unidad": "g"},
            {"id_receta": 23, "nombre": "cebolla", "cantidad": 1, "unidad": "u"},
            {"id_receta": 23, "nombre": "caldo", "cantidad": 500, "unidad": "ml"},
            {"id_receta": 24, "nombre": "arroz", "cantidad": 100, "unidad": "g"},
            {"id_receta": 24, "nombre": "leche", "cantidad": 800, "unidad": "ml"},
            {"id_receta": 24, "nombre": "azúcar", "cantidad": 80, "unidad": "g"},
            {"id_receta": 24, "nombre": "canela", "cantidad": 1, "unidad": "u"},
            {"id_receta": 25, "nombre": "chocolate", "cantidad": 200, "unidad": "g"},
            {"id_receta": 25, "nombre": "manteca", "cantidad": 150, "unidad": "g"},
            {"id_receta": 25, "nombre": "azúcar", "cantidad": 150, "unidad": "g"},
            {"id_receta": 25, "nombre": "huevo", "cantidad": 3, "unidad": "u"},
            {"id_receta": 25, "nombre": "harina", "cantidad": 80, "unidad": "g"},
            {"id_receta": 26, "nombre": "choclo", "cantidad": 6, "unidad": "u"},
            {"id_receta": 26, "nombre": "cebolla", "cantidad": 1, "unidad": "u"},
            {"id_receta": 26, "nombre": "leche", "cantidad": 100, "unidad": "ml"},
            {"id_receta": 26, "nombre": "manteca", "cantidad": 20, "unidad": "g"},
            {"id_receta": 27, "nombre": "carne picada", "cantidad": 500, "unidad": "g"},
            {"id_receta": 27, "nombre": "pan", "cantidad": 4, "unidad": "u"},
            {"id_receta": 27, "nombre": "lechuga", "cantidad": 4, "unidad": "hojas"},
            {"id_receta": 27, "nombre": "tomate", "cantidad": 1, "unidad": "u"},
            {"id_receta": 28, "nombre": "papa", "cantidad": 400, "unidad": "g"},
            {"id_receta": 28, "nombre": "zanahoria", "cantidad": 200, "unidad": "g"},
            {"id_receta": 28, "nombre": "arveja", "cantidad": 150, "unidad": "g"},
            {"id_receta": 28, "nombre": "mayonesa", "cantidad": 120, "unidad": "g"},
            {"id_receta": 29, "nombre": "garbanzo", "cantidad": 400, "unidad": "g"},
            {"id_receta": 29, "nombre": "leche de coco", "cantidad": 200, "unidad": "ml"},
            {"id_receta": 29, "nombre": "curry", "cantidad": 15, "unidad": "g"},
            {"id_receta": 29, "nombre": "cebolla", "cantidad": 1, "unidad": "u"},
            {"id_receta": 30, "nombre": "arroz arborio", "cantidad": 300, "unidad": "g"},
            {"id_receta": 30, "nombre": "hongo", "cantidad": 200, "unidad": "g"},
            {"id_receta": 30, "nombre": "caldo", "cantidad": 800, "unidad": "ml"},
            {"id_receta": 30, "nombre": "queso parmesano", "cantidad": 50, "unidad": "g"}
        ]
        # Listas de subrecetas
        self.subrecetas = [
            {"id_receta": 9, "id_subreceta": 1},
            {"id_receta": 9, "id_subreceta": 2},
            {"id_receta": 10, "id_subreceta": 3},
            {"id_receta": 10, "id_subreceta": 5},
            {"id_receta": 11, "id_subreceta": 4},
            {"id_receta": 12, "id_subreceta": 3},
            {"id_receta": 13, "id_subreceta": 6},
            {"id_receta": 14, "id_subreceta": 1},
            {"id_receta": 17, "id_subreceta": 8},
            {"id_receta": 18, "id_subreceta": 8},
            {"id_receta": 19, "id_subreceta": 3},
            {"id_receta": 20, "id_subreceta": 7},
            {"id_receta": 27, "id_subreceta": 8},
            {"id_receta": 30, "id_subreceta": 3}
        ]
    def buscar_recetas(self): # Este método devuelve la lista de recetas del recetario.
        return self.recetas

    def buscar_subrecetas(self, id_receta): # Este método devuelve la lista de subrecetas de una receta específica, dado su ID.
        lista_id = [] 
        for t in self.subrecetas: # Recorremos la lista de subrecetas y verificamos si el ID de la receta coincide con el ID proporcionado.
            if t["id_receta"] == id_receta: 
                lista_id.append(t["id_subreceta"]) # Agregamos el ID de la subreceta a la lista de subrecetas de la receta.
        return lista_id

    def buscar_ingredientes(self, id_receta): # Este método devuelve la lista de ingredientes de una receta específica, dado su ID.
        lista_ing = []
        for ing in self.ingredientes: # Recorremos la lista de ingredientes y verificamos si el ID de la receta coincide con el ID proporcionado.
            if ing["id_receta"] == id_receta:
                texto = f"{ing['cantidad']} {ing['unidad']} de {ing['nombre']}"
                lista_ing.append(texto) # Agregamos el ingrediente a la lista de ingredientes de la receta.
        return lista_ing

    def descomponer_recetas(self, id_receta): # Función recursiva que devuelve una receta y todas sus dependencias.
        sub = self.buscar_subrecetas(id_receta)
        if not sub: # CASO BASE: No tiene sub-recetas.
            return [id_receta]
        
        resultado = [id_receta] # CASO RECURSIVO: Agregamos la receta actual y exploramos sus dependencias.
        for s in sub:
            resultado += self.descomponer_recetas(s)       
        return resultado