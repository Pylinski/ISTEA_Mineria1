#Recomendacion de Libros

""" Desarrolla un sistema de recomendación de libros en Python. La aplicación debe permitir a
los usuarios buscar libros por género y recibir recomendaciones basadas en sus intereses.

Instrucciones:
● Define una clase llamada “Libro” con los siguientes atributos: titulo, autor, genero y
puntuacion (valor numérico que representa la popularidad del libro). Crea un método
__init__ para inicializar estos atributos.
● Crea una lista llamada lista_libros donde almacenarás los objetos de la clase Libro.
● Implementa un bucle que permita a los usuarios realizar las siguientes acciones:
    ○ Agregar Libro: Solicita al usuario que ingrese el título, autor, género y
puntuación del libro. Crea un objeto Libro con estos atributos y agrega el
objeto a la lista lista_libros.
    ○ Buscar Libros por Género: Pregunta al usuario por un género y muestra
una lista de títulos de libros en ese género.
    ○ Recomendar Libro: Pregunta al usuario por su género de interés y muestra
el título del libro con la puntuación más alta en ese género.
● Ejecuta el bucle hasta que el usuario decida salir de la aplicación. """



class Libro:
    def __init__(self,Titulo,Autor,Genero,Puntuacion):
        self.Titulo = Titulo
        self.Autor = Autor
        self.Genero = Genero
        self.Puntuacion = Puntuacion

Lista_Libros = []
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficcion", 4.5)
libro2 = Libro("1984", "George Orwell", "Ciencia Ficcion", 4.3)
libro3 = Libro("El Hobbit", "J.R.R. Tolkien", "Fantasia", 4.7)
libro4 = Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2)
libro5 = Libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clasico", 4.4)
libro6 = Libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1)
libro7 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clasico", 4.6)
libro8 = Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasia", 4.8)
libro9 = Libro("Los Pilares de la Tierra", "Ken Follett", "Historica", 4.4)
libro10 = Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasia", 4.0)

Lista_Libros.extend([libro1, libro2, libro3, libro4, libro5, libro6, libro7, libro8, libro9, libro10])

while True:
    print('Opciones:')
    print('1. Buscar')
    print('2. Recomendar')
    print('3. Salir')

    opcion = input("Seleccionar una Opcion: ")

    if opcion == "1":
        busqueda_genero=input("Ingresar el Genero que desea Buscar: ")
        libros_en_genero= [libro.titulo for libro in Lista_Libros if libro.genero == busqueda_genero]

        if libros_en_genero:
            print("Libros en el genero '{}' : " .format(busqueda_genero))
            for titulo_libro in libros_en_genero:
                print(titulo_libro)
        else:
            print("No hay Libros con ese Genero")

    elif opcion == "2":
        recomendacion_genero= input("Que genero le gusta?: ")
        libros_en_genero=[libro for libro in Lista_Libros if libro.genero == recomendacion_genero]

        if libros_en_genero:
            recomendacion_genero= max(libros_en_genero, key=lambda libro: libro.puntuacion)
            print("La Recomendacion es: '{}'  con puntuacion {}".format(recomendacion_genero.titulo, recomendacion_genero.puntuacion))
        else:
            print("No hay libros para recomendar")

    elif opcion == "3":
        print("Saludos")
        break
    else:
        print("Opcion INVALIDA.")
