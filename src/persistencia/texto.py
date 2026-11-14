from pathlib import Path
from src.excepciones import ArchivoInvalidoError

# Resoluciones de ruta estáticas absolutas con el objetivo de prevenir excepciones de directorios por variaciones en el punto de ejecución.
RAIZ = Path(__file__).resolve().parents[2]
DATA = RAIZ / "data"

RUTA_RECETAS = DATA / "recetas.csv"
RUTA_INGREDIENTES = DATA / "ingredientes.csv"
RUTA_SUBRECETAS = DATA / "subrecetas.csv"

ENCABEZADOS_RECETAS = ["id", "nombre", "tiempo_min", "dificultad", "categoria"]


def cargar_csv(ruta):
    """
    Gestiona el procedimiento de lectura secuencial de los documentos almacenados en texto plano devolviendo estructuras nativas del lenguaje.
    Si se presentan discrepancias estructurales, invoca el módulo de manejo de excepciones interrumpiendo el flujo.
    """
    ruta = Path(ruta)
    if not ruta.exists():
        raise ArchivoInvalidoError(f"Imposibilidad de acceso de lectura al recurso: {ruta}")

    filas = []
    try:
        with ruta.open("r", encoding="utf-8") as archivo:
            primera_linea = archivo.readline().strip()
            if not primera_linea:
                raise ArchivoInvalidoError(f"Se ha detectado un archivo carente de datos: {ruta}")

            # Define las claves del diccionario a partir del procesamiento de la cabecera.
            encabezado = primera_linea.split(",")

            for num_linea, linea in enumerate(archivo, start=2):
                linea = linea.strip()
                # Omite las filas compuestas por caracteres nulos para estabilizar el proceso final de lectura.
                if not linea:  
                    continue

                valores = linea.split(",")
                # Validación estricta que coteja que la cardinalidad de cada registro iguale al patrón de cabecera.
                if len(valores) != len(encabezado):
                    raise ArchivoInvalidoError(
                        f"Anomalía estructural en línea {num_linea}: Compuesta por {len(valores)} campos "
                        f"cuando la definición esperada estipulaba {len(encabezado)}: {linea}"
                    )

                fila = dict(zip(encabezado, valores))
                filas.append(fila)
    except UnicodeDecodeError as e:
        raise ArchivoInvalidoError(f"Conflicto de estandarización: Fallo en la decodificación de caracteres UTF-8 en el recurso: {e}")

    return filas


def guardar_csv(ruta, filas, encabezados):
    """
    Maneja el procedimiento de escritura secuencial transformando los objetos al formato regular estipulado (valores separados por coma).
    """
    ruta = Path(ruta)
    with ruta.open("w", encoding="utf-8", newline="") as archivo:
        archivo.write(",".join(encabezados) + "\n")
        for fila in filas:
            campos = [str(fila[clave]) for clave in encabezados]
            archivo.write(",".join(campos) + "\n")


# Se establecen alias nomenclaturales con el propósito de respetar la semántica impuesta por las guías del trabajo práctico.
cargar_texto = cargar_csv
guardar_texto = guardar_csv