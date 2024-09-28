# Diccionario para almacenar libros
libros = {}

# Función para agregar libros predeterminados
def agregar_libros_predeterminados():
    libros["Cien Años de Soledad"] = {
        "Categoría": "Novela",
        "Año de publicación": 1967,
        "Número de hojas": 471,
        "Autor": "Gabriel García Márquez"
    }

    libros["Don Quijote de la Mancha"] = {
        "Categoría": "Novela",
        "Año de publicación": 1605,
        "Número de hojas": 863,
        "Autor": "Miguel de Cervantes"
    }

    libros["Orgullo y Prejuicio"] = {
        "Categoría": "Novela",
        "Año de publicación": 1813,
        "Número de hojas": 432,
        "Autor": "Jane Austen"
    }

    libros["1984"] = {
        "Categoría": "Ciencia ficción",
        "Año de publicación": 1949,
        "Número de hojas": 328,
        "Autor": "George Orwell"
    }

# Función para imprimir un libro específico
def imprimir_libro(nombre):
    # Convertir el nombre ingresado a minúsculas para evitar problemas con las mayúsculas
    nombre = nombre.lower()
    # Buscar el libro ignorando mayúsculas y minúsculas
    for titulo in libros:
        if titulo.lower() == nombre:
            print(f"\nNombre: {titulo}")
            for clave, valor in libros[titulo].items():
                print(f"{clave}: {valor}")
            return
    print(f"No se encontró el libro: {nombre}")

# Función para imprimir la lista de todos los libros
def imprimir_libros():
    if libros:
        print("\nListado de libros:")
        for nombre, datos in libros.items():
            print(f"\nNombre: {nombre}")
            for clave, valor in datos.items():
                print(f"{clave}: {valor}")
    else:
        print("No hay libros registrados.")

# Agregar libros predeterminados
agregar_libros_predeterminados()

# Solicitar al usuario si quiere ver un libro o todos
opcion = input("¿Desea ver un libro en particular o todos? (escribe 'uno' o 'todos'): ").lower()

if opcion == 'uno':
    nombre_libro = input("Escriba el nombre del libro: ")
    imprimir_libro(nombre_libro)
elif opcion == 'todos':
    imprimir_libros()
else:
    print("Opción no válida.")
