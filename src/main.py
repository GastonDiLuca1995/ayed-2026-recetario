from src.config import TEMA # Se importa la variable TEMA desde el archivo config.py
from src.dominio.recetario import Lista_recetas #Se importa la lista de recetas desde el archivo recetario.py

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")

def listar_catalogo(): # Función que lista el catálogo de recetas
    print("\n--- CATÁLOGO DE RECETAS ---")
    for receta in Lista_recetas:
        print(f"{receta['id']:>3}  {receta['nombre']} - {receta['tiempo_min']} min ({receta['dificultad']}) ({receta['categoria']})")
    
    input("\nPresioná Enter para volver al menú...") # Se hace una pausa para que el usuario vea el catalogo antes de volver al menú

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

    opcion = None
    while opcion != "0": # Bucle del programa si el usuario es distinto de 0 aparece el menú
        mostrar_menu()
        opcion = input("> ").strip() # Elimina espacios en blanco al inicio y al final de la opción ingresada por el usuario
        if opcion == "0": # Si el usuario ingresa 0, se imprime chau y se sale del bucle
            print("Chau.")
        elif opcion == "1": # Si el usuario ingresa 1, se llama a la función listar_catalogo()
            listar_catalogo()  
        elif opcion in {"2", "3", "4", "5", "6", "7", "8", "9"}: # Si el usuario ingresa cualquiera de estas opciones, se llama a la función pendiente()
            pendiente()
        else: # Cualquier otra opción que no sea válida
            print("Opción inválida.")

if __name__ == "__main__":  # Ejecución del programa 
    main()

