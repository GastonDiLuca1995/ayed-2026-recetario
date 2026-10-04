from src.config import TEMA # Se importa la variable TEMA desde el archivo de configuración para determinar el tema actual del programa.
from src.dominio.recetario import Recetario # Se importa la clase Recetario desde el módulo recetario.py, que contiene la lógica para manejar las recetas y sus subrecetas.

# Se importan las clases MenuSemanal, Historial y ColaPreparacion desde sus respectivos módulos en el paquete dominio. Estas clases representan la colección principal de recetas, la pila para deshacer acciones y la cola para la preparación de recetas, respectivamente.
from src.dominio.menu_semanal import MenuSemanal
from src.dominio.historial import Historial
from src.dominio.cola_preparacion import ColaPreparacion
from src.excepciones import ColeccionLlenaError, PilaVaciaError, ColaVaciaError

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")

def listar_catalogo(recetario):  # Esta función recibe un objeto recetario y muestra en pantalla un listado de todas las recetas disponibles en el catálogo.
    print("\n--- CATÁLOGO DE RECETAS ---")
    for receta in recetario.buscar_recetas():
        print(receta.resumen())  
    input("\nPresioná Enter para volver al menú...") 

def descomponer_subrecetas(recetario, id_receta): # Esta función recibe un objeto recetario y un ID de receta, y devuelve una lista con el ID de la receta y todos los IDs de sus subrecetas, utilizando recursión para descomponer las subrecetas en caso de que existan.
    subreceta = recetario.buscar_subrecetas(id_receta)
    if not subreceta:
        return [id_receta]
        
    menu = [id_receta]
    for s in subreceta:
        menu += descomponer_subrecetas(recetario, s)
        
    return menu

def mostrar_menu(): 
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

def main(): 
    if TEMA not in TEMAS:  
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    mi_recetario = Recetario() 
    mi_recetario.cargar_datos() 
    
    # Instanciamos los objetos usando las clases del dominio
    mi_menu = MenuSemanal(tope=7)
    historial = Historial()
    cola_cocina = ColaPreparacion()
    
    opcion = None
    while opcion != "0": 
        mostrar_menu()
        opcion = input("> ").strip() 
        
        if opcion == "0": 
            print("Chau.")
        elif opcion == "1": # Listar catálogo
            historial.registrar_accion("Consultó el catálogo completo")
            listar_catalogo(mi_recetario)
            
        elif opcion == "5": # Operación recursiva
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
            
        elif opcion == "6": # Menú Semanal (Colección principal)
            print("\n--- MENÚ SEMANAL ---")
            print("1. Agregar plato al menú")
            print("2. Ver menú de la semana")
            sub_op = input("> ").strip()
            
            if sub_op == "1": # Agregar plato al menú
                plato = input("Nombre de la receta: ").strip()
                try: 
                    mi_menu.agregar(plato)
                    print(f"¡'{plato}' agregado con éxito!")
                except ColeccionLlenaError as e: 
                    print(f"Error: {e}")
            elif sub_op == "2": # Ver menú de la semana
                print("\nMenú para esta semana:")
                mi_menu.listar()
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "7": # Historial (Pila)
            print("\n--- HISTORIAL (DESHACER) ---")
            try: # Intentamos deshacer la última acción registrada en el historial.
                accion_deshecha = historial.deshacer_accion()
                print(f"Deshecho: {accion_deshecha}")
            except PilaVaciaError as e: # Si la pila está vacía, capturamos la excepción y mostramos un mensaje de error.
                print(f"Error: {e}")
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "8": # Cola de preparación (Cola)
            print("\n--- COLA DE PREPARACIÓN ---")
            print("1. Encolar receta para cocinar")
            print("2. Cocinar próximo plato")
            sub_op = input("> ").strip()
            
            if sub_op == "1": # Encolar receta para cocinar
                plato = input("Nombre de la receta: ").strip()
                cola_cocina.agregar_pedido(plato)
                print(f"¡'{plato}' encolado! Está esperando su turno.")
            elif sub_op == "2": # Cocinar próximo plato
                try:
                    plato_listo = cola_cocina.cocinar_proximo()
                    print(f"¡A cocinar! Saliendo orden de: {plato_listo}")
                except ColaVaciaError as e: # Si la cola está vacía, capturamos la excepción y mostramos un mensaje de error.
                    print(f"Error: {e}")
            input("\nPresioná Enter para volver al menú...")

        elif opcion in {"2", "3", "4", "9"}: 
            pendiente()
        else: 
            print("Opción inválida.")

if __name__ == "__main__":  
    main()