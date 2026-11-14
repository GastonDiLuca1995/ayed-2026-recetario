# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema
- Grupo: 6
- Tema: Recetario
- Por qué lo eligieron (5–8 líneas): Elegimos el tema del recetario ya que cocinar es algo cotidiano y nos pareció más atractivo porque contiene tres datasets relacionados (recetas, ingredientes y subrecetas) para desarrollar aplicando los contenidos de la materia.

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

- Ítem del catálogo: En la primera etapa se modeló como un diccionario y a partir de la Entrega 3 se representa mediante objetos de la clase Receta almacenados dentro de nuestra ListaEnlazada. Cada instancia organiza sus atributos ("id", "nombre", "tiempo_min", "dificultad" y "categoria").
- Datos mutables: Las colecciones (ListaEnlazada de recetas, listas de ingredientes y subrecetas), los diccionarios y los atributos de las instancias de Receta son mutables, lo que permite agregar, modificar o dar de baja registros durante la ejecución del programa.
- Datos inmutables: Los tipos de datos primarios que representan los valores atómicos son inmutables en memoria: números enteros (int para ID y tiempos de cocción) y cadenas de texto (str para nombres, dificultades, categorías e ingredientes).

Cómo se relacionan catálogo, colección principal, pila y cola:

- Catálogo: Representa el inventario completo con todas las recetas cargadas en el sistema desde los archivos de persistencia.
- Colección Principal: Subconjunto de recetas seleccionadas activamente por el usuario para planificar el Menú Semanal (con tope máximo de 7 días), además del soporte de ABM persistente sobre el catálogo.
- Pila: Estructura LIFO (último en entrar, primero en salir) que registra el historial de acciones realizadas por el usuario, permitiendo deshacer la última operación.
- Cola: Estructura FIFO (primero en entrar, primero en salir) utilizada para organizar los pedidos de cocina pendientes de elaborar en estricto orden de llegada.

                            Catálogo (Todas las recetas disponibles)
                                        |
                                        ▼
                            Colección Principal (Menú Semanal)
                                        |
                                     ┌──┴──┐
                                     ▼     ▼
                                    Pila   Cola
                 (Historial de consultas)  (Recetas pendientes a preparar)

## 3. Recursión (E2)

Función: `descomponer_recetas(self, id_receta)`
Caso base: Si la receta no tiene sub-recetas asociadas (lista vacía), devuelve `[id_receta]`.
Caso recursivo: Devuelve `[id_receta]` concatenado con el resultado de las llamadas recursivas de cada una de sus sub-recetas dependientes.

Traza para "Asado" (ID 9):
Según el dataset de subrecetas, la receta 9 depende de la 1 (Chimichurri) y de la 2 (Salsa criolla).

- Llamada 1: `descomponer_recetas(9)` -> tiene subrecetas (1 y 2)
  -> devuelve `[9] + descomponer_recetas(1) + descomponer_recetas(2)`
- Llamada 2: `descomponer_recetas(1)` -> NO tiene subrecetas (caso base)
  -> devuelve `[1]`
- Llamada 3: `descomponer_recetas(2)` -> NO tiene subrecetas (caso base)
  -> devuelve `[2]`

Resultado final: `[9] + [1] + [2] = [9, 1, 2]`

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada | `insertar_al_inicio`, `insertar_al_final`, `buscar`, `eliminar`, `tamanio`, `esta_vacia`, `__iter__` | `_tamanio >= 0`. Si `_tamanio == 0`, `_cabeza` es `None`. El último nodo apunta siempre a `None`. |
| Pila | `apilar`, `desapilar`, `ver_tope`, `esta_vacia` | LIFO. Los elementos ingresan y salen únicamente por el tope (`_cabeza`). Lanza `PilaVaciaError` si se desapila estando vacía. |
| Cola | `encolar`, `desencolar`, `ver_frente`, `esta_vacia` | FIFO. Los elementos ingresan por el final y salen por el frente (`_cabeza`). Lanza `ColaVaciaError` si se desencola estando vacía. |

Dónde se usa cada uno en el dominio:

- ListaEnlazada: Es la estructura base sobre la que se construyen la Pila y la Cola. En el dominio se utiliza para almacenar el catálogo principal de recetas y para gestionar la colección con tope de 7 platos del Menú Semanal.
- Pila: Se utiliza en la clase Historial para registrar las acciones del usuario y deshacer siempre la última operación realizada.
- Cola: Se utiliza en la clase ColaPreparacion para encolar pedidos en la cocina y atenderlos en orden de llegada.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
| Listar catálogo | $O(n)$ | $O(1)$ | Recorre los $n$ elementos de la colección una sola vez mediante el iterador. |
| Búsqueda lineal | $O(n)$ | $O(1)$ | En el peor caso compara cada elemento secuencialmente hasta llegar al final. |
| Búsqueda binaria | $O(\log n)$ | $O(1)$ | En cada paso divide el espacio de búsqueda a la mitad sobre la colección ordenada. |
| Ordenar por selección | $O(n^2)$ | $O(1)$ | Utiliza dos bucles anidados realizando siempre $\approx n^2/2$ comparaciones. |
| Ordenar por inserción | $O(n)$ mejor, $O(n^2)$ peor | $O(1)$ | Si ya está ordenado realiza una comparación por elemento; en orden inverso desplaza todos los anteriores. |
| Ver detalle de un ítem | $O(n)$ | $O(1)$ | Al estar sobre una ListaEnlazada, recorre nodo por nodo hasta encontrar el ID buscado. |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
| Búsqueda lineal (nombre) | 30 | 0.000019 |
| Búsqueda lineal (nombre, x10) | 300 | 0.000012 |
| Búsqueda binaria (nombre) | 30 | 0.000016 |
| Búsqueda binaria (nombre, x10) | 300 | 0.000007 |
| Ordenar por selección (nombre) | 30 | 0.000138 |
| Ordenar por selección (nombre, x10) | 300 | 0.012182 |
| Ordenar por inserción (nombre) | 30 | 0.000106 |
| Ordenar por inserción (nombre, x10) | 300 | 0.010392 |

## 6. Persistencia (E5)

- **Layout del registro binario (campos, `struct`, anchos):** Se utiliza `struct.Struct("<I 30s H 10s 15s")`, lo que genera registros de longitud fija de **61 bytes** en formato little-endian (`<`):
  - `id`: `I` (unsigned int, 4 bytes).
  - `nombre`: `30s` (cadena UTF-8 de 30 bytes fijos).
  - `tiempo_min`: `H` (unsigned short, 2 bytes).
  - `dificultad`: `10s` (cadena UTF-8 de 10 bytes fijos).
  - `categoria`: `15s` (cadena UTF-8 de 15 bytes fijos).
  - Las cadenas de texto se codifican en UTF-8 y se ajustan al ancho fijo truncando o rellenando con bytes nulos (`\x00`) a la derecha; al leer se eliminan los `\x00` finales con `rstrip(b"\x00")`.
- **Header:** Se utiliza `struct.Struct("<4s 1s I")` de **9 bytes** totales:
  - `magia`: `4s` con el valor fijo `b"AYED"` (4 bytes) para validar que el archivo pertenece al sistema.
  - `tema`: `1s` con el valor `b"R"` (1 byte) correspondiente a Recetario.
  - `cantidad`: `I` (unsigned int, 4 bytes) que indica el total de registros almacenados.
- **Cómo se actualiza un registro por posición:** Mediante la función `actualizar_registro(ruta, posicion, item)` abriendo el archivo en modo lectura/escritura binaria (`"r+b"`). Como todos los registros miden exactamente lo mismo, se calcula el desplazamiento exacto con `seek(HEADER.size + posicion * FORMATO.size)` (es decir, $9 + \text{posicion} \times 61$ bytes) y se sobrescribe únicamente ese registro en tiempo constante $O(1)$ (acceso directo), sin reescribir el resto del archivo. Por ejemplo, el registro en la posición 7 comienza exactamente en el byte 436. El alta posiciona el cursor al final con `seek(0, 2)`, agrega el nuevo registro y actualiza el contador del header en el byte 0; la baja elimina el registro y reescribe los restantes actualizando la cabecera para no dejar huecos.

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |