# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema
- Grupo: 6
- Tema: Recetario
- Por qué lo eligieron (5–8 líneas): Elegimos el tema del recetario ya que cocinar es algo cotidiano y nos parecio mas atractivo ya que contiene tres datasets para desarrollar aplicando los contenidos que veremos en clase.

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

-Item del catálogo: Es un diccionario guardado dentro de una lista. Cada diccionario representa una receta individual y organiza sus atributos ("id", "nombre", "tiempo_min", "dificultad" y "categoria") mediante pares clave-valor.

- Datos mutables: Las listas (Lista_recetas, Lista_ingredientes, Lista_subrecetas) y los diccionarios son estructuras mutables. Esto significa que pueden modificarse durante la ejecución del programa, ya sea agregando o eliminando recetas en las listas, o cambiando valores específicos en los diccionarios.

- Datos inmutables: Los datos primarios que funcionan como clave y valor son inmutables, ya que una vez creados en la memoria de la computadora no pueden modificarse. Esto incluye a los números enteros o integers (como los ID y tiempos de cocción) y a las cadenas de texto o strings (como los nombres, categorías e ingredientes).

Cómo se relacionan catálogo, colección principal, pila y cola.

- Catálogo: Representa el inventario completo con todas las recetas cargadas en el sistema.
- Colección Principal: Subconjunto de recetas seleccionadas activamente por el usuario para planificar el menú de la semana.
- Pila: Estructura LIFO (último en entrar, primero en salir) que registra las últimas recetas consultadas o agregadas al menú, permitiendo volver atrás o deshacer la última acción.
- Cola: Estructura FIFO (primero en entrar, primero en salir) utilizada para organizar las preparaciones pendientes de elaborar en estricto orden de llegada.

                            Catálogo(Todas las recetas disponibles)
                                        |
                                        ▼
                            Colección Principal(Menú Semanal)
                                        |
                                     ┌──┴──┐
                                     ▼     ▼
                                    Pila   Cola
                 (Historial de consultas)  (Recetas pendientes a preparar)

## Recursión (E2)

Función: `descomponer_recetas(recetario, id_receta)`
Caso base: Si la receta no tiene sub-recetas (lista vacía), devuelve `[id_receta]`.
Caso recursivo: Devuelve `[id_receta]` + las llamadas recursivas de cada una de sus dependencias.
Traza para "Asado" (ID 9):
Según la lista, la receta 9 depende de la 1 (Chimichurri) y de la 2 (Salsa Criolla).

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
| ListaEnlazada | `insertar_al_inicio`, `insertar_al_final`, `buscar`, `eliminar`, `tamanio`, `esta_vacia`, `__iter__` | `_tamanio >= 0`. Si `_tamanio == 0`, `_cabeza` es `None`. El último nodo apunta a `None`. |
| Pila | `apilar`, `desapilar`, `ver_tope`, `esta_vacia` | LIFO. Los elementos ingresan y salen únicamente por el tope. Lanza excepción si se desapila estando vacía. |
| Cola | `encolar`, `desencolar`, `ver_frente`, `esta_vacia` | FIFO. Ingresan exclusivamente por el final y salen por el frente. Lanza excepción si se desencola estando vacía. |

Dónde se usa cada uno en el dominio.

- ListaEnlazada: Es la estructura base para construir la Pila y la Cola. Dentro del dominio, se implementa para almacenar el catálogo principal de recetas (`recetario.py`) y para gestionar la colección con límite de capacidad de 7 platos en el `menu_semanal.py`.
- Pila: Se utiliza para el Historial del sistema. Registra las interacciones del usuario (como listar el catálogo o consultar una receta específica) permitiendo deshacer acciones sacando siempre la última que se ingresó.
- Cola: Se utiliza para gestionar la Cola de Preparación en la cocina. Los platos ingresan al final de la fila de espera y se atienden desde el frente, garantizando que el primero en pedirse sea el primero en cocinarse.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
