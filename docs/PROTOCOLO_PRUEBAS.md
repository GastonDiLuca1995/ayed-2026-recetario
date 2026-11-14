# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar catálogo | Opción 1 (`recetas.csv`) | Lista las 30 recetas sin error | pasa | Usa el iterador de ListaEnlazada |
| P02 | E1 | Elegir un ítem inexistente | Opción 2, `id = -1` | Mensaje claro, el menú sigue | pasa | Captura `ItemNoEncontradoError` |
| P03 | E2 | Operación recursiva sobre un ítem con cadena | Opción 5, `id = 9` (Asado) | Imprime la cadena completa: `[9, 1, 2]` | pasa | Incluye ingredientes de cada una |
| P04 | E2 | Operación recursiva sobre un ítem sin derivados | Opción 5, `id = 7` (Pesto) | Solo el ítem: `[7]` (caso base) | pasa | Caso base sin subrecetas |
| P05 | E2 | Ver el detalle de un ítem que existe | Opción 2, `id = 12` (Locro) | Muestra todos sus datos e ingredientes | pasa | - |
| P06 | E2 | Ver el detalle de un ítem que NO existe | Opción 2, `id = 99` | Mensaje claro, no se corta el programa | pasa | Captura `ItemNoEncontradoError` |
| P07 | E2 | Elegir una opción de menú inválida | Ingreso = `"9z"` | Avisa opción inválida y vuelve al menú | pasa | - |
| P08 | E2 | Pasar enter vacío en el menú | Entrada vacía `""` | No explota; vuelve a mostrar el menú | pasa | - |
| P09 | E3 | Agregar a la colección principal hasta el tope | Opción 6 -> 1 (cargar 8 platos) | El octavo falla con `ColeccionLlenaError` | pasa | Tope configurado en 7 días |
| P10 | E3 | Desapilar historial vacío | Opción 7 apenas inicia el CLI | Captura `PilaVaciaError`, el menú sigue | pasa | - |
| P11 | E3 | Desencolar cola vacía | Opción 8 -> 2 con cola vacía | Captura `ColaVaciaError`, el menú sigue | pasa | - |
| P12 | E3 | Listar colección con el iterador | Agregar 2+ ítems y listar | El orden coincide con las inserciones | pasa | - |
| P13 | E4 | Búsqueda lineal de un nombre que existe | Opción 3 -> 1, `"Locro"` | Lo encuentra y muestra su resumen | pasa | Insensible a mayúsculas/minúsculas |
| P14 | E4 | Búsqueda lineal de un nombre que no existe | Opción 3 -> 1, `"Ceviche"` | No encontrado, sin traceback, el menú sigue | pasa | - |
| P15 | E4 | Búsqueda binaria con catálogo desordenado | Opción 3 -> 2, `"Asado"` (sin ordenar antes) | Avisa y ordena automáticamente por nombre | pasa | Evita falsos negativos |
| P16 | E4 | Ordenar por un criterio y después por otro | Opción 4 por nombre y luego por tiempo | El orden del catálogo cambia correctamente | pasa | Probado con Selección e Inserción |
| P17 | E5 | Guardar CSV, salir, volver a entrar | Alta/modificación en Opción 6 o 9b, salir y abrir | Los cambios persisten al volver a iniciar | pasa | Lee directamente de `data/recetas.csv` |
| P18 | E5 | Guardar binario y modificar un registro por id | Opción 9c, luego Opción 6 -> 4 (`id = 12`), recargar 9d | Al recargar el binario, el campo modificado cambió | pasa | Usa `actualizar_registro` con `seek` |
| P19 | E5 | Abrir un binario truncado o con magia mala | Opción 9d con archivo basura/truncado | Lanza `ArchivoInvalidoError`, el menú sigue | pasa | Probado con magia inválida y archivo corto |