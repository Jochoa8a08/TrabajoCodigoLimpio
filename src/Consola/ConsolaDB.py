import os
import sys
sys.path.append("src")
sys.path.append(".")
from model.Archivo import Archivo
from controller.ControladorArchivos import ControladorArchivos
from model.Excepciones import ErrorModificarArchivo

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Crear tabla")
    print("2. Eliminar tabla")
    print("3. Insertar archivo")
    print("4. Modificar archivo")
    print("5. Eliminar archivo")
    print("6. Consultar archivo")
    print("7. Ver todos los IDs")
    print("8. Salir")



def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese la opción deseada: ")

        if opcion == '1':
            ControladorArchivos.CrearTabla()
            print("-----------")
        
        elif opcion == '2':
            ControladorArchivos.EliminarTabla()
            print("-----------")

        elif opcion == '3':
            ControladorArchivos.CrearTabla()
            ruta_archivo = input("Ingrese el nombre del archivo: ")
            if os.path.exists(ruta_archivo):
                while True:
                    id = ControladorArchivos.solicitar_id()
                    archivo = ControladorArchivos.ConsultarArchivo(id)
                    if archivo:
                        print("El ID ya existe. Intente de nuevo con otro ID.")
                    else:
                        nombre = os.path.basename(ruta_archivo)
                        extension = os.path.splitext(nombre)[1][1:]  # Obtener la extensión sin el punto
                        tamaño = os.path.getsize(ruta_archivo)
                        archivo = Archivo(id=id, nombre=nombre, extension=extension, tamaño=tamaño, fecha_creacion=None)
                        ControladorArchivos.InsertarArchivo(archivo)
                        print("Archivo insertado exitosamente.")
                        break
            else:
                    print("El archivo no existe. Por favor, verifique e intente nuevamente.")


        elif opcion == '4':
            while True:
                ControladorArchivos.CrearTabla()
                id = ControladorArchivos.solicitar_id()
                archivo =ControladorArchivos.ConsultarArchivo(id)
                nombre = input("Ingrese el nuevo nombre (deje en blanco si no desea cambiar): ")
                extension = input("Ingrese la nueva extensión (deje en blanco si no desea cambiar): ")
                try:
                    
                    ControladorArchivos.ModificarArchivo(id, nombre, extension)
                    print("Archivo modificado exitosamente.")
                    break
                except ErrorModificarArchivo as e:
                    print(e)
        
        elif opcion == '5':
            ControladorArchivos.CrearTabla()
            id = ControladorArchivos.solicitar_id()
            if ControladorArchivos.ConsultarArchivo(id):
                ControladorArchivos.EliminarArchivo(id)
                print("Archivo eliminado exitosamente.")
            else:
                print("El ID no existe. Volviendo al menú principal.")
            print("-----------")

        elif opcion == '6':
            ids = ControladorArchivos.ConsultarTodosLosIds()
            if ids:
                print("---IDs disponibles en la base de datos---")
                for id in ids:
                    print(id)
                while True:
                    id = ControladorArchivos.solicitar_id()
                    archivo = ControladorArchivos.ConsultarArchivo(id)
                    if archivo:
                        print(f"ID: {archivo.id}")
                        print(f"Nombre: {archivo.nombre}")
                        print(f"Extensión: {archivo.extension}")
                        print(f"Tamaño Kb: {archivo.tamaño}")
                        print(f"Fecha de creación: {archivo.fecha_creacion}")
                        break
                    else:
                        print("Archivo no encontrado. Intente de nuevo.")
            else:
                print("No existen IDs en la base de datos.")
                print("-----------")

        elif opcion == '7':
            print("Validando para crear la Tabla...")
            ControladorArchivos.CrearTabla()
            ids = ControladorArchivos.ConsultarTodosLosIds()
            if ids:
                print("---IDs en la base de datos---")
                for id in ids:
                    print(id)
            else:
                print("No hay archivos en la base de datos.")
            print("-----------")

        elif opcion == '8':
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
