"""Registros de longitud fija con struct para la representación del modelo de Recetario.

Estructura de Cabecera (9 bytes): "<4s 1s I"
  magia     4s   Firma validatoria (b'AYED')
  tema      1s   Identificador del dominio (b'R')
  cantidad  I    Contador de registros, entero sin signo (4 bytes)

Estructura de Entidad Receta (61 bytes): "<I 30s H 10s 15s"
  id          I    Clave primaria, entero sin signo (4 bytes)
  nombre     30s   Cadena codificada en UTF-8 con alineación nula \\x00 (30 bytes)
  tiempo_min  H    Unidad temporal, entero corto sin signo (2 bytes)
  dificultad 10s   Cadena codificada en UTF-8 con alineación nula \\x00 (10 bytes)
  categoria  15s   Cadena codificada en UTF-8 con alineación nula \\x00 (15 bytes)
"""

import struct
from pathlib import Path
from src.dominio.receta import Receta
from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ArchivoInvalidoError, ItemNoEncontradoError

# Configuración de referencias espaciales relativas al repositorio.
RAIZ = Path(__file__).resolve().parents[2]
DATA = RAIZ / "data"
RUTA_BIN = DATA / "recetas.bin"

# Definición inmutable de los formatos de lectura y escritura a nivel de byte.
HEADER = struct.Struct("<4s 1s I")             
FORMATO = struct.Struct("<I 30s H 10s 15s")    
TEMA_BIN = b"R"


def _a_bytes(texto, ancho):
    """Realiza la conversión de un tipo cadena hacia su equivalente en bytes UTF-8, garantizando el espacio posicional estricto mediante relleno con caracteres nulos."""
    return str(texto).encode("utf-8")[:ancho].ljust(ancho, b"\x00")


def _a_texto(datos):
    """Revierte la conversión binaria de caracteres descartando la sección de padding aplicada para homogeneizar longitudes."""
    try:
        return datos.rstrip(b"\x00").decode("utf-8")
    except UnicodeDecodeError as e:
        raise ArchivoInvalidoError(f"Se detectó un segmento de texto ilegible por corrupción en el decodificador: {e}")


def _item_a_tupla(receta):
    """Prepara las propiedades del objeto de dominio conformándolas en una tupla posicional requerida por la librería struct."""
    return (
        int(receta.id),
        _a_bytes(receta.nombre, 30),
        int(receta.tiempo_min),
        _a_bytes(receta.dificultad, 10),
        _a_bytes(receta.categoria, 15),
    )


def _tupla_a_item(tupla):
    """Instancia un objeto válido de dominio a partir de los datos atómicos recuperados mediante el desempaquetado de struct."""
    return Receta(
        id_receta=tupla[0],
        nombre=_a_texto(tupla[1]),
        tiempo_min=tupla[2],
        dificultad=_a_texto(tupla[3]),
        categoria=_a_texto(tupla[4]),
    )


def posicion_del_id(catalogo, id_buscado):
    """Itera sobre la colección de objetos y determina el índice numérico que ocupa un registro específico."""
    for posicion, item in enumerate(catalogo):
        if item.id == id_buscado:
            return posicion
    raise ItemNoEncontradoError(f"El identificador consultado ({id_buscado}) no tiene referencias asociadas.")


def guardar_binario(ruta, items):
    """Itera sobre la estructura en memoria y sobrescribe el documento completo bajo un formato binario secuencial."""
    ruta = Path(ruta)
    cantidad = items.tamanio() if hasattr(items, "tamanio") else len(items)

    with ruta.open("wb") as archivo:
        # Se inyecta la firma de validación inicial
        archivo.write(HEADER.pack(b"AYED", TEMA_BIN, cantidad))
        for item in items:  
            archivo.write(FORMATO.pack(*_item_a_tupla(item)))


def cargar_binario(ruta):
    """Procesa un archivo de bytes, realiza pruebas de validación de formato e instancia la colección en memoria principal."""
    ruta = Path(ruta)
    if not ruta.exists():
        raise ArchivoInvalidoError(f"Error de acceso: Ausencia del archivo físico en la ruta {ruta}")

    with ruta.open("rb") as archivo:
        cabecera = archivo.read(HEADER.size)
        if len(cabecera) < HEADER.size:
            raise ArchivoInvalidoError("Fallo de lectura: La estructura inicial no satisface el tamaño requerido.")

        magia, tema, cantidad = HEADER.unpack(cabecera)
        
        # Validaciones de integridad estructural
        if magia != b"AYED":
            raise ArchivoInvalidoError("Inconsistencia en los metadatos: Firma de integridad rechazada.")
        if tema != TEMA_BIN:
            raise ArchivoInvalidoError(f"Inconsistencia de contexto: Se esperaba dominio ({TEMA_BIN!r}) pero se recibió ({tema!r}).")

        catalogo = ListaEnlazada()
        for _ in range(cantidad):
            datos = archivo.read(FORMATO.size)
            if len(datos) < FORMATO.size:
                raise ArchivoInvalidoError("Fallo de lectura: El documento fue interrumpido previo al cumplimiento total de los registros.")
            catalogo.insertar_al_final(_tupla_a_item(FORMATO.unpack(datos)))

    return catalogo


def actualizar_registro(ruta, posicion, item):
    """Sustituye de forma directa los bytes pertenecientes a un registro puntual basando el acceso en el cálculo de desplazamientos posicionales O(1)."""
    ruta = Path(ruta)
    if not ruta.exists():
        raise ArchivoInvalidoError(f"Error de acceso: Ausencia del archivo físico en la ruta {ruta}")

    # El modo 'r+b' permite mutar fragmentos específicos del archivo sin incurrir en una reescritura global.
    with ruta.open("r+b") as archivo:
        cabecera = archivo.read(HEADER.size)
        if len(cabecera) < HEADER.size:
            raise ArchivoInvalidoError("Fallo de lectura: La estructura inicial no satisface el tamaño requerido.")
            
        magia, tema, cantidad = HEADER.unpack(cabecera)
        if magia != b"AYED" or tema != TEMA_BIN:
            raise ArchivoInvalidoError("Validación rechazada: La cabecera carece de consistencia.")
            
        if posicion < 0 or posicion >= cantidad:
            raise ItemNoEncontradoError(f"El índice proporcionado excede el dominio estipulado ({cantidad} registros).")

        # Se establece la posición de inicio del registro resolviendo la ecuación algorítmica: tamaño base + (índice * amplitud modular).
        archivo.seek(HEADER.size + posicion * FORMATO.size)
        archivo.write(FORMATO.pack(*_item_a_tupla(item)))


def alta_binario(ruta, item):
    """Anexa un nuevo registro en la terminación del documento existente y procede a actualizar las estadísticas documentadas en la cabecera."""
    ruta = Path(ruta)
    if not ruta.exists():
        raise ArchivoInvalidoError(f"Error de acceso: Ausencia del archivo físico en la ruta {ruta}")

    with ruta.open("r+b") as archivo:
        cabecera = archivo.read(HEADER.size)
        if len(cabecera) < HEADER.size:
            raise ArchivoInvalidoError("Fallo de lectura: La cabecera se halla corrupta o truncada.")
        magia, tema, cantidad = HEADER.unpack(cabecera)
        if magia != b"AYED" or tema != TEMA_BIN:
            raise ArchivoInvalidoError("Validación rechazada por incompatibilidad de metadatos.")

        # Desplaza el cursor de escritura hasta el último byte disponible en el documento.
        archivo.seek(0, 2)  
        archivo.write(FORMATO.pack(*_item_a_tupla(item)))
        
        # Reposiciona el cursor en el segmento inicial para impactar el incremento de cantidad registrado.
        archivo.seek(0)     
        archivo.write(HEADER.pack(magia, tema, cantidad + 1))


def baja_binario(ruta, posicion):
    """Procesa la supresión de un registro y aplica la reorganización secuencial sobre el documento para evitar vacíos posicionales de longitud inválida."""
    ruta = Path(ruta)
    if not ruta.exists():
        raise ArchivoInvalidoError(f"Error de acceso: Ausencia del archivo físico en la ruta {ruta}")

    with ruta.open("r+b") as archivo:
        cabecera = archivo.read(HEADER.size)
        if len(cabecera) < HEADER.size:
            raise ArchivoInvalidoError("Fallo de lectura: La cabecera se halla corrupta.")
        magia, tema, cantidad = HEADER.unpack(cabecera)
        if magia != b"AYED" or tema != TEMA_BIN:
            raise ArchivoInvalidoError("Validación rechazada por incompatibilidad de metadatos.")
        if posicion < 0 or posicion >= cantidad:
            raise ItemNoEncontradoError("El índice suministrado incurre en un error de desbordamiento de límites.")

        # Se carga el volumen en memoria, se ejecuta la eliminación de la entidad y se reescribe de forma secuencial.
        registros = [archivo.read(FORMATO.size) for _ in range(cantidad)]
        del registros[posicion]

        archivo.seek(0)
        archivo.truncate()
        archivo.write(HEADER.pack(magia, tema, len(registros)))
        for datos in registros:
            archivo.write(datos)