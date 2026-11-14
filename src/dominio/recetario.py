from src.dominio.receta import Receta  # Se importa la clase Receta para instanciar cada plato del catálogo.
from src.tads.lista_enlazada import ListaEnlazada  # Se importa nuestra ListaEnlazada para guardar las recetas.
from src.excepciones import ArchivoInvalidoError, ItemNoEncontradoError  # Excepciones propias del TP.
from src.persistencia.texto import (  # Importamos la función de lectura y las rutas fijas a la carpeta data/.
    cargar_csv,
    RUTA_RECETAS,
    RUTA_INGREDIENTES,
    RUTA_SUBRECETAS,
)


class Recetario:  # Definimos la clase Recetario para gestionar el catálogo completo.
    def __init__(self):  # Constructor de la clase Recetario.
        self.recetas = ListaEnlazada()  # Catálogo principal guardado en nuestra ListaEnlazada.
        self.ingredientes = []  # Lista para almacenar los ingredientes de cada receta.
        self.subrecetas = []  # Lista para almacenar las dependencias entre recetas (recursión).

    def cargar_datos(
        self,
        ruta_recetas=RUTA_RECETAS,
        ruta_ingredientes=RUTA_INGREDIENTES,
        ruta_subrecetas=RUTA_SUBRECETAS,
    ):
        """Carga las recetas, ingredientes y subrecetas leyendo los archivos reales de la carpeta data/."""
        # 1. Cargamos el catálogo principal de recetas en la ListaEnlazada
        self.cargar_catalogo_desde_csv(ruta_recetas)

        # 2. Cargamos los ingredientes desde data/ingredientes.csv
        self.ingredientes = []
        for fila in cargar_csv(ruta_ingredientes):
            # En el CSV la columna es 'receta_id'; usamos .get() por compatibilidad
            id_rec = fila.get("receta_id", fila.get("id_receta"))
            self.ingredientes.append({
                "id_receta": int(id_rec),
                "nombre": fila["nombre"],
                "cantidad": fila["cantidad"],
                "unidad": fila["unidad"],
            })

        # 3. Cargamos las subrecetas desde data/subrecetas.csv
        self.subrecetas = []
        for fila in cargar_csv(ruta_subrecetas):
            id_rec = fila.get("receta_id", fila.get("id_receta"))
            id_sub = fila.get("subreceta_id", fila.get("id_subreceta"))
            self.subrecetas.append({
                "id_receta": int(id_rec),
                "id_subreceta": int(id_sub),
            })

    def cargar_catalogo_desde_csv(self, ruta_recetas=RUTA_RECETAS):
        """Lee el archivo CSV de recetas y arma la ListaEnlazada con objetos Receta."""
        nuevo_catalogo = ListaEnlazada()
        try:
            for fila in cargar_csv(ruta_recetas):
                nueva_receta = Receta(
                    id_receta=int(fila["id"]),          # Convertimos texto a entero
                    nombre=fila["nombre"],
                    tiempo_min=int(fila["tiempo_min"]), # Convertimos texto a entero
                    dificultad=fila["dificultad"],
                    categoria=fila["categoria"],
                )
                nuevo_catalogo.insertar_al_final(nueva_receta)
        except (ValueError, KeyError) as e:
            raise ArchivoInvalidoError(f"Error en los datos del archivo de recetas: {e}")

        self.recetas = nuevo_catalogo
        return self.recetas

    def filas_del_catalogo(self):
        """Convierte los objetos Receta de la ListaEnlazada en diccionarios para poder guardarlos en CSV."""
        filas = []
        for r in self.recetas:  # Recorre usando el iterador (__iter__) de ListaEnlazada
            filas.append({
                "id": r.id,
                "nombre": r.nombre,
                "tiempo_min": r.tiempo_min,
                "dificultad": r.dificultad,
                "categoria": r.categoria,
            })
        return filas

    def buscar_recetas(self):  # Devuelve la ListaEnlazada completa de recetas.
        return self.recetas

    def buscar_por_id(self, id_receta):
        """Busca y devuelve el objeto Receta según su ID. Si no existe, lanza ItemNoEncontradoError."""
        for receta in self.recetas:  # Usa el iterador de la ListaEnlazada
            if receta.id == id_receta:
                return receta
        raise ItemNoEncontradoError(f"No existe ninguna receta con el ID {id_receta}.")

    def buscar_subrecetas(self, id_receta):  # Devuelve la lista de IDs de subrecetas que necesita un plato.
        lista_id = []
        for t in self.subrecetas:
            if t["id_receta"] == id_receta:
                lista_id.append(t["id_subreceta"])
        return lista_id

    def buscar_ingredientes(self, id_receta):  # Devuelve los ingredientes formateados de una receta según su ID.
        lista_ing = []
        for ing in self.ingredientes:
            if ing["id_receta"] == id_receta:
                texto = f"{ing['cantidad']} {ing['unidad']} de {ing['nombre']}"
                lista_ing.append(texto)
        return lista_ing

    def descomponer_recetas(self, id_receta):  # Función recursiva que devuelve una receta y todas sus dependencias.
        sub = self.buscar_subrecetas(id_receta)
        if not sub:  # CASO BASE: No tiene sub-recetas previas.
            return [id_receta]

        resultado = [id_receta]  # CASO RECURSIVO: Agrega la receta actual y explora cada sub-receta.
        for s in sub:
            resultado += self.descomponer_recetas(s)
        return resultado