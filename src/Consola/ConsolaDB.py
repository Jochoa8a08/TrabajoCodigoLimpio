import os
import sys
sys.path.append( "src" )
sys.path.append( "." )
from model.Archivo import Archivo
from controller.ControladorArchivos import ControladorArchivos

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Crear tabla")
    print("2. Eliminar tabla")
    print("3. Insertar archivo")
    print("4. Modificar archivo")
    print("5. Eliminar archivo")
    print("6. Consultar archivo")
    print("7. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese la opción deseada: ")

        if opcion == '1':
            ControladorArchivos.CrearTabla()
            print("Tabla creada exitosamente.")
        
        elif opcion == '2':
            ControladorArchivos.EliminarTabla()
            print("Tabla eliminada exitosamente.")

        elif opcion == '3':
            ruta_archivo = input("Ingrese el nombre del archivo: ")
            if os.path.exists(ruta_archivo):
                id = input("Ingrese el id del archivo: ")
                nombre = os.path.basename(ruta_archivo)
                extension = os.path.splitext(nombre)[1][1:]  # Obtener la extensión sin el punto
                tamaño = os.path.getsize(ruta_archivo)
                archivo = Archivo(id=id, nombre=nombre, extension=extension, tamaño=tamaño, fecha_creacion=None)
                ControladorArchivos.InsertarArchivo(archivo)
                print("Archivo insertado exitosamente.")
            else:
                print("El archivo no existe en la ruta especificada. Por favor, verifique la ruta e intente nuevamente.")

        elif opcion == '4':
            id = input("Ingrese el id del archivo a modificar: ")
            nombre = input("Ingrese el nuevo nombre (deje en blanco si no desea cambiar): ")
            extension = input("Ingrese la nueva extensión (deje en blanco si no desea cambiar): ")
            tamaño = input("Ingrese el nuevo tamaño (deje en blanco si no desea cambiar): ")
            tamaño = int(tamaño) if tamaño else None
            ControladorArchivos.ModificarArchivo(id, nombre, extension, tamaño)
            print("Archivo modificado exitosamente.")

        elif opcion == '5':
            id = input("Ingrese el id del archivo a eliminar: ")
            ControladorArchivos.EliminarArchivo(id)
            print("Archivo eliminado exitosamente.")

        elif opcion == '6':
            id = input("Ingrese el id del archivo a consultar: ")
            archivo = ControladorArchivos.ConsultarArchivo(id)
            if archivo:
                print(f"ID: {archivo.id}")
                print(f"Nombre: {archivo.nombre}")
                print(f"Extensión: {archivo.extension}")
                print(f"Tamaño: {archivo.tamaño}")
                print(f"Fecha de creación: {archivo.fecha_creacion}")
            else:
                print("Archivo no encontrado.")

        elif opcion == '7':
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
