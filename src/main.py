from src.config import TEMA      # Configuración de qué trata el programa
from src.dominio.recetario import Recetario       # Herramienta para armar el libro de recetas.                
from src.dominio.menu_semanal import MenuSemanal       # Herramienta para organizar la comida semanal.
from src.dominio.historial import Historial       # Libreta para anotar qué hacemos y deshacer.
from src.dominio.cola_preparacion import ColaPreparacion      # Herramienta para hacer la fila de pedidos.
from src.excepciones import ColeccionLlenaError, PilaVaciaError, ColaVaciaError      # Alarmas por si algo sale mal (ej: fila llena).
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria      # Formas de buscar cosas en nuestra lista.
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion    # Formas de ordenar (agarrando el menor) y (como acomodar cartas).
from src.tads.lista_enlazada import ListaEnlazada         # Herramienta para listas que pueden agrandarse.

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

def pendiente():                                                      # Aviso genérico para opciones que todavía no fabricamos.
    print("Todavía no está implementado. Completar en la entrega que corresponde.")

def listar_catalogo(recetario):                                       # Muestra el libro de recetas completo desde el principio al fin.
    print("\n--- CATÁLOGO DE RECETAS ---")
    for receta in recetario.buscar_recetas():
        print(receta.resumen())  
    input("\nPresioná Enter para volver al menú...") 

def descomponer_subrecetas(recetario, id_receta):                     # Busca si un plato necesita preparaciones previas ocultas
    subreceta = recetario.buscar_subrecetas(id_receta)                # (ej: la hamburguesa necesita hacer el pan primero) y te 
    if not subreceta:                                                 # devuelve la lista completa de absolutamente todos los pasos.
        return [id_receta]
        
    menu = [id_receta]
    for s in subreceta:
        menu += descomponer_subrecetas(recetario, s)
        
    return menu

def mostrar_menu():                                                   # Dibuja la carta de opciones en pantalla para que el usuario elija.
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Menú Semanal (Colección principal)")
    print("7. Historial (Pila)")
    print("8. Cola de preparación (Cola)")
    print("9. Guardar / cargar archivos")
    print("0. Salir")

def main():                                                           # Acá arranca a funcionar el programa completo.
    if TEMA not in TEMAS:  
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    mi_recetario = Recetario() 
    mi_recetario.cargar_datos() 
    
    mi_menu = MenuSemanal(tope=7)
    historial = Historial()
    cola_cocina = ColaPreparacion()
    
    estado_orden = None 
    
    opcion = None
    while opcion != "0":                                              # Repite el menú una y otra vez hasta que elijamos salir con "0".
        mostrar_menu()
        opcion = input("> ").strip() 
        
        if opcion == "0":                                             # Cierra el programa.
            print("Chau.")
            
        elif opcion == "1":                                           # Anota la acción en la libreta y muestra todas las recetas.
            historial.registrar_accion("Consultó el catálogo completo")
            listar_catalogo(mi_recetario)

        elif opcion == "3":                                           # Busca una comida de forma lenta (hoja por hoja) o rápida (mitades).
            print("\n--- BUSCAR RECETA ---")
            print("1) Búsqueda Lineal (por nombre)")
            print("2) Búsqueda Binaria (por nombre)")
            sub_op = input("> ").strip()

            if sub_op in ["1", "2"]:
                criterio = input("Ingresá el nombre a buscar: ").strip()
                lista_recetas = list(mi_recetario.recetas)

                if sub_op == "1":
                    resultado = busqueda_lineal(lista_recetas, criterio, obtener_clave=lambda r: r.nombre)
                    if resultado:
                        print(f"\n¡Encontrado (Lineal)! {resultado.resumen()}")
                    else:
                        print("\nNo encontrado.")

                elif sub_op == "2":
                    if estado_orden != "nombre":
                        print("\n[Aviso] El catálogo no estaba ordenado por nombre. Ordenando automáticamente con Inserción...")
                        lista_recetas = ordenar_insercion(lista_recetas, obtener_clave=lambda r: r.nombre.lower())
                        estado_orden = "nombre"
                        
                        mi_recetario.recetas = ListaEnlazada()
                        for rec in lista_recetas:
                            mi_recetario.recetas.insertar_al_final(rec)

                    resultado = busqueda_binaria(lista_recetas, criterio, obtener_clave=lambda r: r.nombre)
                    if resultado:
                        print(f"\n¡Encontrado (Binaria)! {resultado.resumen()}")
                    else:
                        print("\nNo encontrado.")
            else:
                print("Opción inválida.")
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "4":                                           # Ordena el recetario por nombre alfabético o tiempo de cocción.
            print("\n--- ORDENAR CATÁLOGO ---")
            print("Criterio: 1) Nombre (alfabético) 2) Tiempo de cocción (minutos)")
            crit_op = input("> ").strip()

            print("Algoritmo: 1) Selección 2) Inserción ")
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

                mi_recetario.recetas = ListaEnlazada()
                for rec in lista_recetas:
                    mi_recetario.recetas.insertar_al_final(rec)

                estado_orden = criterio_str
                print(f"\n Catálogo ordenado por {criterio_str} ({alg_str}).")
            else:
                print("Opción inválida.")
            input("\nPresioná Enter para volver al menú...")
            
        elif opcion == "5":                                           # Revisa un plato, busca sus pasos y te hace la lista de compras exacta.
            print("\n--- OPERACIÓN RECURSIVA ---")
            id_ingresado = int(input("Ingresá el ID de la receta (ej. 10 para Empanadas): "))
            
            historial.registrar_accion(f"Consultó receta ID {id_ingresado}")
            
            comida = descomponer_subrecetas(mi_recetario, id_ingresado)
            print(f"Recetas a preparar para el ID {id_ingresado}: {comida}")
            
            print("\nLista de ingredientes necesarios:")
            for num_receta in comida:
                ings = mi_recetario.buscar_ingredientes(num_receta)
                if ings: 
                    print(f"\nPara la receta {num_receta}:")
                    for i in ings:
                        print(f"  * {i}")
            input("\nPresioná Enter para volver al menú...")
            
        elif opcion == "6":                                           # Arma los platos exactos para los 7 días de la semana con un tope máximo.
            print("\n--- MENÚ SEMANAL ---")
            print("1. Agregar plato al menú")
            print("2. Ver menú de la semana")
            sub_op = input("> ").strip()
            
            if sub_op == "1": 
                plato = input("Nombre de la receta: ").strip()
                try: 
                    mi_menu.agregar(plato)
                    print(f"¡'{plato}' agregado con éxito!")
                except ColeccionLlenaError as e: 
                    print(f"Error: {e}")
            elif sub_op == "2": 
                print("\nMenú para esta semana:")
                mi_menu.listar()
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "7":                                           # Usa la libreta de historial para borrar tu último error (como una goma).
            print("\n--- HISTORIAL (DESHACER) ---")
            try: 
                accion_deshecha = historial.deshacer_accion()
                print(f"Deshecho: {accion_deshecha}")
            except PilaVaciaError as e: 
                print(f"Error: {e}")
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "8":                                           # Maneja la fila de la cocina (el primer pedido en entrar es el primero en salir).
            print("\n--- COLA DE PREPARACIÓN ---")
            print("1. Encolar receta para cocinar")
            print("2. Cocinar próximo plato")
            sub_op = input("> ").strip()
            
            if sub_op == "1": 
                plato = input("Nombre de la receta: ").strip()
                cola_cocina.agregar_pedido(plato)
                print(f"¡'{plato}' encolado! Está esperando su turno.")
            elif sub_op == "2": 
                try:
                    plato_listo = cola_cocina.cocinar_proximo()
                    print(f"¡A cocinar! Saliendo orden de: {plato_listo}")
                except ColaVaciaError as e: 
                    print(f"Error: {e}")
            input("\nPresioná Enter para volver al menú...")

        elif opcion in {"2", "9"}: 
            pendiente()
        else: 
            print("Opción inválida.")

if __name__ == "__main__":  
    main()