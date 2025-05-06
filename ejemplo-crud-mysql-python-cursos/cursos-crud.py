import mysql.connector
from datetime import datetime

# Conexión a MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="epik-user",
    password="epik-pass",
    database="epik"
)

cursor = conexion.cursor()

def crear_curso():
    nombre = input("Nombre del curso: ")
    profesor = input("Nombre del profesor: ")
    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
    fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")
    descripcion = input("Descripción: ")

    sql = "INSERT INTO cursos (nombre, profesor, fecha_inicio, fecha_fin, descripcion) VALUES (%s, %s, %s, %s, %s)"
    datos = (nombre, profesor, fecha_inicio, fecha_fin, descripcion)
    cursor.execute(sql, datos)
    conexion.commit()
    print("Curso creado correctamente.")

def listar_cursos():
    cursor.execute("SELECT * FROM cursos")
    cursos = cursor.fetchall()
    print("\nLista de cursos:")
    for curso in cursos:
        print(f"ID: {curso[0]}, Nombre: {curso[1]}, Profesor: {curso[2]}, Inicio: {curso[3]}, Fin: {curso[4]}, Desc: {curso[5]}")

def actualizar_curso():
    id = input("Ingrese el ID del curso a actualizar: ")
    nuevo_nombre = input("Nuevo nombre: ")
    nuevo_profesor = input("Nuevo profesor: ")
    nueva_fecha_inicio = input("Nueva fecha de inicio (YYYY-MM-DD): ")
    nueva_fecha_fin = input("Nueva fecha de fin (YYYY-MM-DD): ")
    nueva_descripcion = input("Nueva descripción: ")

    sql = """UPDATE cursos 
             SET nombre=%s, profesor=%s, fecha_inicio=%s, fecha_fin=%s, descripcion=%s 
             WHERE id=%s"""
    datos = (nuevo_nombre, nuevo_profesor, nueva_fecha_inicio, nueva_fecha_fin, nueva_descripcion, id)
    cursor.execute(sql, datos)
    conexion.commit()
    print("Curso actualizado correctamente.")

def eliminar_curso():
    id = input("Ingrese el ID del curso a eliminar: ")
    cursor.execute("DELETE FROM cursos WHERE id = %s", (id,))
    conexion.commit()
    print("Curso eliminado correctamente.")

def menu():
    while True:
        print("\n--- Menú de Cursos ---")
        print("1. Crear curso")
        print("2. Listar cursos")
        print("3. Actualizar curso")
        print("4. Eliminar curso")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_curso()
        elif opcion == "2":
            listar_cursos()
        elif opcion == "3":
            actualizar_curso()
        elif opcion == "4":
            eliminar_curso()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú principal
menu()

# Cerrar conexión
cursor.close()
conexion.close()
