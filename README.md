# AYED C2 2026 - Recetario - Grupo 6

**Integrantes:**
* Delfino, Kadyel (kadyeldelfino-byte)
* Di Luca, Gastón (GastonDiLuca1995)
* Perez Cordoba, Micaela (cordobamica65-max)

## Tema
Gestor de catálogo gastronómico (Recetario) con dependencias entre sub-recetas e ingredientes.

## Cómo ejecutarlo
Requiere Python 3.10+ (solo biblioteca estándar, sin dependencias externas). Desde la raíz del repositorio, ejecutar:
`python -m src.main`
*(En Windows, si `python` no está en el PATH, utilizar `py -3 -m src.main`)*

## Qué hace
Sistema de gestión por consola que implementa las 10 operaciones requeridas:
1. Listado completo mediante iterador propio.
2. Detalle individual de recetas e ingredientes.
3. Búsqueda iterativa (Lineal) y particional (Binaria).
4. Ordenamiento de catálogo (Selección e Inserción).
5. Desglose recursivo de sub-recetas.
6. Planificación de Menú Semanal (tope 7 días) y ABM de catálogo.
7. Historial de acciones (Pila - LIFO) con función deshacer.
8. Gestión de comandas de cocina (Cola - FIFO).
9. Persistencia de datos secuencial (.csv) y de acceso directo (.bin) con módulo `struct`.
0. Cierre seguro de sesión.

## Limitaciones conocidas
* **Interfaz:** El sistema no cuenta con interfaz gráfica (GUI) ni base de datos externa; opera exclusivamente en terminal (CLI) usando la biblioteca estándar de Python.
* **Truncamiento de texto:** Debido a la persistencia en formato binario con registros de tamaño fijo (`struct`), los nombres de recetas que superen los 30 caracteres (o 15 para la categoría) se recortarán automáticamente al guardarse en disco.
* **Bajas en tiempo O(n):** Mientras que la actualización de un registro binario se hace con acceso directo en tiempo O(1) mediante `seek`, la eliminación (baja) requiere reescribir todo el archivo secuencialmente para evitar dejar huecos.
* **Tope de planificación:** La colección del Menú Semanal está estrictamente limitada a 7 días. Si se intenta superar este tope, el sistema bloquea la carga.