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

## 3. Recursión (E2)

- Función:
- Caso base:
- Caso recursivo:
- Traza de un ejemplo real del dataset:

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

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
