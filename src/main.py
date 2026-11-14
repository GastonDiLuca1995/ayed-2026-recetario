from pathlib import Path
from src.config import TEMA  
from src.dominio.receta import Receta  
from src.dominio.recetario import Recetario  
from src.dominio.menu_semanal import MenuSemanal  
from src.dominio.historial import Historial  
from src.dominio.cola_preparacion import ColaPreparacion  
from src.excepciones import ColeccionLlenaError, PilaVaciaError, ColaVaciaError, ItemNoEncontradoError, ArchivoInvalidoError
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria  
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion  
from src.tads.lista_enlazada import ListaEnlazada  
from src.persistencia.texto import guardar_csv, RUTA_RECETAS, ENCABEZADOS_RECETAS
from src.persistencia.binario import guardar_binario, cargar_binario, actualizar_registro, alta_binario, baja_binario, posicion_del_id, RUTA_BIN

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

def guardar_todo(recetario):
    """Escribe el estado actual del catálogo en los archivos de texto y binario para mantener la sincronización de los datos."""
    guardar_csv(RUTA_RECETAS, recetario.filas_del_catalogo(), ENCABEZADOS_RECETAS)
    guardar_binario(RUTA_BIN, recetario.recetas)

def listar_catalogo(recetario):  
    # Recorre la colección completa utilizando el iterador de la ListaEnlazada para mostrar cada registro.
    print("\n--- CATÁLOGO DE RECETAS ---")
    if recetario.recetas.esta_vacia():
        print("El catálogo se encuentra vacío.")
    else:
        for receta in recetario.buscar_recetas():
            print(receta.resumen())
    input("\nPresione Enter para retornar al menú...")

def ver_detalle(recetario, historial):  
    # Solicita un ID y muestra los atributos detallados de la instancia correspondiente.
    print("\n--- VER DETALLE DE RECETA ---")
    entrada = input("Ingrese el ID de la receta: ").strip()
    try:
        id_buscado = int(entrada)
    except ValueError:
        print("Error: Se requiere el ingreso de un valor numérico entero.")
        input("\nPresione Enter para retornar al menú...")
        return

    try:
        receta = recetario.buscar_por_id(id_buscado)
        historial.registrar_accion(f"Consultó el detalle de la receta ID {id_buscado} ({receta.nombre})")

        print(f"\nID: {receta.id}")
        print(f"Nombre: {receta.nombre}")
        print(f"Tiempo de cocción: {receta.tiempo_min} min")
        print(f"Dificultad: {receta.dificultad}")
        print(f"Categoría: {receta.categoria}")

        ings = recetario.buscar_ingredientes(id_buscado)
        print("Ingredientes:")
        if ings:
            for ing in ings:
                print(f"  * {ing}")
        else:
            print("  (Sin ingredientes registrados en el sistema)")

        subs = recetario.buscar_subrecetas(id_buscado)
        if subs:
            print(f"Dependencias previas (IDs): {subs}")
    except ItemNoEncontradoError as e:
        print(f"Aviso: {e}")

    input("\nPresione Enter para retornar al menú...")

def descomponer_subrecetas(recetario, id_receta):  
    # Función intermediaria que invoca la lógica de recursión para obtener el árbol de dependencias.
    return recetario.descomponer_recetas(id_receta)

def mostrar_menu():  
    # Imprime las opciones disponibles para la interacción del usuario con la interfaz de consola (CLI).
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Menú Semanal y ABM de Recetas")
    print("7. Historial (Pila)")
    print("8. Cola de preparación (Cola)")
    print("9. Guardar / cargar archivos")
    print("0. Salir")

def main():  
    # Punto de entrada principal de la aplicación. Inicializa las estructuras y gestiona el bucle de control.
    if TEMA not in TEMAS:
        print("Debe configurar la variable TEMA en src/config.py con una opción válida.")
        return

    mi_recetario = Recetario()
    try:
        mi_recetario.cargar_datos()
    except ArchivoInvalidoError as e:
        print(f"Se produjo un error al cargar los conjuntos de datos iniciales: {e}")

    mi_menu = MenuSemanal(tope=7)
    historial = Historial()
    cola_cocina = ColaPreparacion()
    estado_orden = None
    opcion = None

    # Bucle principal: mantiene el programa en ejecución hasta que el usuario decida finalizar la sesión.
    while opcion != "0":  
        mostrar_menu()
        opcion = input("> ").strip()

        if opcion == "0":  
            print("Finalizando la ejecución del programa.")

        elif opcion == "1":  
            historial.registrar_accion("Ejecutó el listado general del catálogo")
            listar_catalogo(mi_recetario)

        elif opcion == "2":  
            ver_detalle(mi_recetario, historial)

        elif opcion == "3":  
            # Implementa la selección entre algoritmos de búsqueda iterativa.
            print("\n--- BUSCAR RECETA ---")
            print("1) Búsqueda Lineal (por nombre)")
            print("2) Búsqueda Binaria (por nombre)")
            sub_op = input("> ").strip()

            if sub_op in ["1", "2"]:
                criterio = input("Ingrese el nombre del elemento a buscar: ").strip()
                lista_recetas = list(mi_recetario.recetas)

                if sub_op == "1":
                    resultado = busqueda_lineal(lista_recetas, criterio, obtener_clave=lambda r: r.nombre)
                    if resultado:
                        historial.registrar_accion(f"Ejecutó búsqueda lineal para el criterio '{criterio}'")
                        print(f"\nElemento encontrado mediante método lineal: {resultado.resumen()}")
                    else:
                        print("\nEl elemento solicitado no se encuentra en el catálogo.")

                elif sub_op == "2":
                    if estado_orden != "nombre":
                        print("\n[Aviso] El catálogo requiere ordenamiento previo. Aplicando algoritmo de inserción...")
                        lista_recetas = ordenar_insercion(lista_recetas, obtener_clave=lambda r: r.nombre.lower())
                        estado_orden = "nombre"

                        # Actualiza la lista enlazada principal tras el ordenamiento.
                        mi_recetario.recetas = ListaEnlazada()
                        for rec in lista_recetas:
                            mi_recetario.recetas.insertar_al_final(rec)

                    resultado = busqueda_binaria(lista_recetas, criterio, obtener_clave=lambda r: r.nombre)
                    if resultado:
                        historial.registrar_accion(f"Ejecutó búsqueda binaria para el criterio '{criterio}'")
                        print(f"\nElemento encontrado mediante partición binaria: {resultado.resumen()}")
                    else:
                        print("\nEl elemento solicitado no se encuentra en el catálogo.")
            else:
                print("La opción ingresada no es válida.")
            input("\nPresione Enter para retornar al menú...")

        elif opcion == "4":  
            # Gestiona la invocación de algoritmos de ordenamiento cuadráticos.
            print("\n--- ORDENAR CATÁLOGO ---")
            print("Criterio: 1) Nombre (alfabético) 2) Tiempo de cocción (minutos)")
            crit_op = input("> ").strip()

            print("Algoritmo: 1) Selección 2) Inserción")
            alg_op = input("> ").strip()

            if crit_op in ["1", "2"] and alg_op in ["1", "2"]:
                lista_recetas = list(mi_recetario.recetas)

                if crit_op == "1":
                    clave_fn = lambda r: r.nombre.lower()
                    criterio_str = "nombre"
                else:
                    clave_fn = lambda r: r.tiempo_min
                    criterio_str = "tiempo"

                if alg_op == "1":
                    lista_recetas = ordenar_seleccion(lista_recetas, obtener_clave=clave_fn)
                    alg_str = "Selección"
                else:
                    lista_recetas = ordenar_insercion(lista_recetas, obtener_clave=clave_fn)
                    alg_str = "Inserción"

                # Reconstruye la estructura de datos para mantener la consistencia.
                mi_recetario.recetas = ListaEnlazada()
                for rec in lista_recetas:
                    mi_recetario.recetas.insertar_al_final(rec)

                estado_orden = criterio_str
                guardar_todo(mi_recetario)
                historial.registrar_accion(f"Ordenó el catálogo por {criterio_str} mediante el método de {alg_str}")
                print(f"\nEl catálogo ha sido ordenado por {criterio_str} ({alg_str}) y sincronizado en los archivos de persistencia.")
            else:
                print("La opción ingresada no es válida.")
            input("\nPresione Enter para retornar al menú...")

        elif opcion == "5":  
            # Invoca el proceso recursivo para trazar el árbol de componentes de una receta.
            print("\n--- OPERACIÓN RECURSIVA ---")
            entrada = input("Ingrese el identificador (ID) de la receta: ").strip()
            try:
                id_ingresado = int(entrada)
                receta_principal = mi_recetario.buscar_por_id(id_ingresado)
            except ValueError:
                print("Error: Se requiere el ingreso de un valor numérico entero.")
                input("\nPresione Enter para retornar al menú...")
                continue
            except ItemNoEncontradoError as e:
                print(f"Aviso: {e}")
                input("\nPresione Enter para retornar al menú...")
                continue

            historial.registrar_accion(f"Descompuso recursivamente la receta ID {id_ingresado} ({receta_principal.nombre})")

            comida = descomponer_subrecetas(mi_recetario, id_ingresado)
            print(f"Secuencia de preparaciones para '{receta_principal.nombre}' (ID {id_ingresado}): {comida}")

            print("\nInsumos requeridos para la elaboración:")
            for num_receta in comida:
                ings = mi_recetario.buscar_ingredientes(num_receta)
                if ings:
                    print(f"\nPara la etapa correspondiente al ID {num_receta}:")
                    for i in ings:
                        print(f"  * {i}")
            input("\nPresione Enter para retornar al menú...")

        elif opcion == "6":  
            # Operaciones de Alta, Baja y Modificación (ABM) con escritura directa a memoria secundaria.
            print("\n--- MENÚ SEMANAL Y ABM DE RECETAS ---")
            print("1. Incorporar plato al menú semanal (límite de 7 elementos)")
            print("2. Visualizar la planificación de la semana")
            print("3. Registrar nueva receta en el sistema (Alta persistente)")
            print("4. Modificar atributos de receta (Acceso directo en archivo binario)")
            print("5. Eliminar receta del sistema (Baja persistente)")
            sub_op = input("> ").strip()

            if sub_op == "1":
                plato = input("Nombre de la receta a incorporar: ").strip()
                if not plato:
                    print("El campo de nombre no admite valores nulos.")
                else:
                    try:
                        mi_menu.agregar(plato)
                        historial.registrar_accion(f"Incorporó el elemento '{plato}' a la planificación semanal")
                        print(f"La operación finalizó exitosamente: '{plato}' añadido.")
                    except ColeccionLlenaError as e:
                        print(f"Excepción de capacidad: {e}")

            elif sub_op == "2":
                print("\nPlanificación semanal actual:")
                mi_menu.listar()

            elif sub_op == "3":  
                # Procedimiento de creación de un nuevo registro (Alta).
                try:
                    nuevo_id_str = input("Asigne un ID a la nueva receta (Presione Enter para asignación automática): ").strip()
                    if nuevo_id_str:
                        nuevo_id = int(nuevo_id_str)
                        for r in mi_recetario.recetas:
                            if r.id == nuevo_id:
                                print(f"Error: El identificador {nuevo_id} se encuentra actualmente en uso.")
                                nuevo_id = None
                                break
                        if nuevo_id is None:
                            input("\nPresione Enter para retornar al menú...")
                            continue
                    else:
                        max_id = 0
                        for r in mi_recetario.recetas:
                            if r.id > max_id:
                                max_id = r.id
                        nuevo_id = max_id + 1

                    nombre = input("Ingrese la denominación de la receta: ").strip()
                    tiempo_min = int(input("Establezca el tiempo de cocción (en minutos): ").strip())
                    dificultad = input("Especifique el nivel de complejidad (baja/media/alta): ").strip() or "baja"
                    categoria = input("Especifique la categoría funcional (principal/entrada/postre/salsa/base): ").strip() or "principal"

                    if not nombre or tiempo_min < 0:
                        print("Error: Los parámetros provistos no cumplen con las validaciones de dominio.")
                    else:
                        nueva = Receta(nuevo_id, nombre, tiempo_min, dificultad, categoria)
                        if not RUTA_BIN.exists():
                            guardar_binario(RUTA_BIN, mi_recetario.recetas)
                        
                        # Actualiza la colección en memoria y persiste el cambio inmediatamente.
                        mi_recetario.recetas.insertar_al_final(nueva)
                        alta_binario(RUTA_BIN, nueva)
                        guardar_csv(RUTA_RECETAS, mi_recetario.filas_del_catalogo(), ENCABEZADOS_RECETAS)
                        
                        estado_orden = None
                        historial.registrar_accion(f"Generó el alta de la receta ID {nuevo_id} ({nombre})")
                        print(f"El registro '{nombre}' (ID {nuevo_id}) ha sido persistido exitosamente en los formatos CSV y Binario.")
                except ValueError:
                    print("Error de tipo: Se esperaban valores numéricos enteros.")
                except ArchivoInvalidoError as e:
                    print(f"Excepción de entrada/salida: {e}")

            elif sub_op == "4":  
                # Procedimiento de actualización in situ (acceso posicional en archivo binario).
                try:
                    id_mod = int(input("Ingrese el identificador (ID) de la receta a modificar: ").strip())
                    receta = mi_recetario.buscar_por_id(id_mod)
                    posicion = posicion_del_id(mi_recetario.recetas, id_mod)

                    print(f"Modificando el registro: {receta.resumen()} (Ubicado en el índice {posicion} de la estructura física)")
                    nuevo_nombre = input(f"Nueva denominación [{receta.nombre}]: ").strip()
                    nuevo_tiempo = input(f"Nuevo tiempo en minutos [{receta.tiempo_min}]: ").strip()
                    nueva_dif = input(f"Nuevo nivel de dificultad [{receta.dificultad}]: ").strip()
                    nueva_cat = input(f"Nueva categoría funcional [{receta.categoria}]: ").strip()

                    # Aplica mutaciones solo a los campos proporcionados por el usuario.
                    if nuevo_nombre:
                        receta.nombre = nuevo_nombre
                    if nuevo_tiempo:
                        receta.tiempo_min = int(nuevo_tiempo)
                    if nueva_dif:
                        receta.dificultad = nueva_dif
                    if nueva_cat:
                        receta.categoria = nueva_cat

                    if not RUTA_BIN.exists():
                        guardar_binario(RUTA_BIN, mi_recetario.recetas)
                    else:
                        actualizar_registro(RUTA_BIN, posicion, receta)

                    guardar_csv(RUTA_RECETAS, mi_recetario.filas_del_catalogo(), ENCABEZADOS_RECETAS)
                    estado_orden = None
                    historial.registrar_accion(f"Ejecutó la actualización del registro ID {id_mod} ubicado en la posición física {posicion}")
                    print(f"El registro ha sido actualizado mediante acceso directo (O(1)) en el archivo binario.")
                except ValueError:
                    print("Error de tipo: Se requiere el ingreso de un valor numérico entero.")
                except (ItemNoEncontradoError, ArchivoInvalidoError) as e:
                    print(f"Excepción capturada: {e}")

            elif sub_op == "5":  
                # Procedimiento de eliminación de registros (Baja).
                try:
                    id_baja = int(input("Ingrese el identificador (ID) de la receta a dar de baja: ").strip())
                    receta = mi_recetario.buscar_por_id(id_baja)
                    posicion = posicion_del_id(mi_recetario.recetas, id_baja)

                    if not RUTA_BIN.exists():
                        guardar_binario(RUTA_BIN, mi_recetario.recetas)

                    # Elimina el nodo de la estructura en memoria y reescribe los repositorios persistentes.
                    mi_recetario.recetas.eliminar(receta)
                    baja_binario(RUTA_BIN, posicion)
                    guardar_csv(RUTA_RECETAS, mi_recetario.filas_del_catalogo(), ENCABEZADOS_RECETAS)
                    
                    historial.registrar_accion(f"Ejecutó la baja del registro ID {id_baja} ({receta.nombre})")
                    print(f"El registro '{receta.nombre}' ha sido purgado de la memoria y las estructuras de almacenamiento.")
                except ValueError:
                    print("Error de tipo: Se requiere el ingreso de un valor numérico entero.")
                except (ItemNoEncontradoError, ArchivoInvalidoError) as e:
                    print(f"Excepción capturada: {e}")
            else:
                print("La opción ingresada no es válida.")
            input("\nPresione Enter para retornar al menú...")

        elif opcion == "7":  
            # Gestión del historial a través de la estructura abstracta Pila (LIFO).
            print("\n--- HISTORIAL (REVERSIÓN DE OPERACIONES) ---")
            try:
                accion_deshecha = historial.deshacer_accion()
                print(f"Operación revertida exitosamente: {accion_deshecha}")
            except PilaVaciaError as e:
                print(f"Excepción estructural: {e}")
            input("\nPresione Enter para retornar al menú...")

        elif opcion == "8":  
            # Procesamiento secuencial mediante la estructura abstracta Cola (FIFO).
            print("\n--- GESTIÓN DE COLA DE PREPARACIÓN ---")
            print("1. Encolar nueva solicitud de preparación")
            print("2. Desencolar y despachar solicitud en curso")
            sub_op = input("> ").strip()

            if sub_op == "1":
                plato = input("Denominación del plato a solicitar: ").strip()
                if not plato:
                    print("El parámetro ingresado no puede ser nulo.")
                else:
                    cola_cocina.agregar_pedido(plato)
                    historial.registrar_accion(f"Añadió la solicitud '{plato}' a la cola de atención")
                    print(f"Solicitud procesada: '{plato}' ha sido integrado a la secuencia de espera.")
            elif sub_op == "2":
                try:
                    plato_listo = cola_cocina.cocinar_proximo()
                    historial.registrar_accion(f"Despachó el pedido correspondiente a '{plato_listo}'")
                    print(f"Iniciando preparación. El sistema despacha el elemento: {plato_listo}")
                except ColaVaciaError as e:
                    print(f"Excepción estructural: {e}")
            else:
                print("La opción ingresada no es válida.")
            input("\nPresione Enter para retornar al menú...")

        elif opcion == "9":  
            # Rutinas de entrada/salida y manejo explícito de archivos de persistencia.
            print("\n--- ADMINISTRACIÓN DE ALMACENAMIENTO ---")
            print("a) Importar colección desde documento de texto (.csv)")
            print("b) Exportar colección hacia documento de texto (.csv)")
            print("c) Exportar colección hacia estructura binaria (.bin)")
            print("d) Importar colección desde estructura binaria (.bin)")
            sub = input("Seleccione subopción > ").strip().lower()

            try:
                if sub == "a":
                    ruta_in = input(f"Especifique la ruta física (Enter para usar el valor predeterminado '{RUTA_RECETAS.name}'): ").strip()
                    ruta_usar = Path(ruta_in) if ruta_in else RUTA_RECETAS
                    mi_recetario.cargar_catalogo_desde_csv(ruta_usar)
                    estado_orden = None
                    historial.registrar_accion(f"Importó los registros desde el archivo físico ({ruta_usar.name})")
                    print(f"Operación finalizada. Volumen de carga: {mi_recetario.recetas.tamanio()} entidades.")

                elif sub == "b":
                    guardar_csv(RUTA_RECETAS, mi_recetario.filas_del_catalogo(), ENCABEZADOS_RECETAS)
                    historial.registrar_accion("Exportó la colección principal al formato de texto secuencial")
                    print(f"Los datos se han salvaguardado en el archivo {RUTA_RECETAS.name}.")

                elif sub == "c":
                    guardar_binario(RUTA_BIN, mi_recetario.recetas)
                    historial.registrar_accion("Exportó la colección principal al formato binario de longitud fija")
                    print(f"Los datos se han codificado en el archivo {RUTA_BIN.name}.")

                elif sub == "d":
                    ruta_in = input(f"Especifique la ruta física (Enter para usar el valor predeterminado '{RUTA_BIN.name}'): ").strip()
                    ruta_usar = Path(ruta_in) if ruta_in else RUTA_BIN
                    mi_recetario.recetas = cargar_binario(ruta_usar)
                    estado_orden = None
                    historial.registrar_accion(f"Restauró el estado del sistema a partir de datos binarios ({ruta_usar.name})")
                    print(f"Lectura estructural completada. Instancias recuperadas: {mi_recetario.recetas.tamanio()}.")

                else:
                    print("La opción ingresada carece de validez funcional.")
            except ArchivoInvalidoError as error:
                print(f"Validación fallida al intentar procesar el archivo: {error}")

            input("\nPresione Enter para retornar al menú...")

        else:
            print("El valor ingresado no corresponde a ninguna acción programada.")

if __name__ == "__main__":
    main()