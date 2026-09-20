from src.config import TEMA # Se importa la variable TEMA desde el archivo config.py
from src.dominio.recetario import Recetario # Se importa la clase Recetario desde el archivo recetario.py

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")

def buscar_catalogo(recetario):  # Recorre los objetos Receta guardados en el recetario y los imprime.
    print("\n--- CATÁLOGO DE RECETAS ---")
    for receta in recetario.buscar_recetas():
        print(receta.resumen())  # Se llama al metodo resumen y se imprime el resultado.

    input("\nPresioná Enter para volver al menú...") # Pausa para que el usuario pueda volver al menú principal.

def mostrar_menu(): # Menú principal del programa
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Colección principal (equipo / menú / playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")

def main(): # Punto de entrada del programa
    if TEMA not in TEMAS:  # Validación de tema
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    recetario_seis= Recetario() # Se crea un objeto de la clase Recetario.
    recetario_seis.cargar_datos() # Se llama al método cargar_datos para cargar las recetas y subrecetas.
    opcion = None
    while opcion != "0": # Bucle del programa si el usuario es distinto de 0 aparece el menú
        mostrar_menu()
        opcion = input("> ").strip() # Elimina espacios en blanco al inicio y al final de la opción ingresada por el usuario
        if opcion == "0": # Si el usuario ingresa 0, se imprime chau y se sale del bucle
            print("Chau.")
        elif opcion == "1": # Si el usuario ingresa 1, se llama a la función buscar_catalogo para mostrar el catálogo de recetas
            buscar_catalogo(recetario_seis)
        elif opcion == "5": # Si el usuario ingresa 5, se realiza la operación recursiva para descomponer recetas
            print("\n--- OPERACIÓN RECURSIVA ---")
            id_ingresado = int(input("Ingresá el ID de la receta (por ejemplo, 9 para Asado): "))
            comida = recetario_seis.descomponer_recetas(id_ingresado)
            print(f"Recetas a preparar para el ID {id_ingresado}: {comida}")

            input("\nPresioná Enter para volver al menú...")
        elif opcion in {"2", "3", "4", "6", "7", "8", "9"}: 
            pendiente()
        else: # Cualquier otra opción que no sea válida
            print("Opción inválida.")

if __name__ == "__main__":  # Ejecución del programa 
    main()

