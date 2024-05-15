import unittest
import sys
import os
from datetime import date

sys.path.append("src")
sys.path.append(".")

from model.Archivo import Archivo
from controller.ControladorArchivos import ControladorArchivos

class ControllerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Se ejecuta al inicio de todas las pruebas"""
        print("Invocando setUpClass")
        ControladorArchivos.EliminarTabla()
        ControladorArchivos.CrearTabla()

    
    
    def testInsertarArchivo(self):
        # Prueba que se inserte correctamente un archivo en la tabla
        print("Ejecutando testInsertarArchivo")
        ControladorArchivos.EliminarArchivo(1234)
        ruta_archivo = "audio1.mp3"
        if os.path.exists(ruta_archivo):
            id = "1234"
            nombre = os.path.basename(ruta_archivo)
            extension = os.path.splitext(nombre)[1][1:]  # Obtener la extensión sin el punto
            tamaño = os.path.getsize(ruta_archivo)
            archivo = Archivo(id=id, nombre=nombre, extension=extension, tamaño=tamaño, fecha_creacion=None)
            ControladorArchivos.InsertarArchivo(archivo)
            archivo_insertado = ControladorArchivos.ConsultarArchivo(id)
            self.assertIsNotNone(archivo_insertado)
            self.assertEqual(nombre, archivo_insertado.nombre)
            self.assertEqual(extension, archivo_insertado.extension)
            self.assertEqual(tamaño, archivo_insertado.tamaño)

    def testConsultarArchivo(self):
        # Prueba que se consulte correctamente un archivo en la tabla
        print("Ejecutando testConsultarArchivo")

        ruta_archivo = "audio1.mp3"
        os.path.exists(ruta_archivo)
        id = 1234
        nombre = os.path.basename(ruta_archivo)
        extension = os.path.splitext(nombre)[1][1:]  # Obtener la extensión sin el punto
        tamaño = os.path.getsize(ruta_archivo)
        archivo = Archivo(id=id, nombre=nombre, extension=extension, tamaño=tamaño, fecha_creacion=None)
        ControladorArchivos.InsertarArchivo(archivo)

        nombre ="audio1.mp3"
        archivo = ControladorArchivos.ConsultarArchivo(id)
        self.assertIsNotNone(archivo)
        self.assertEqual(id,archivo.id)
        self.assertEqual(nombre,archivo.nombre)

    def testModificarArchivo(self):
        print("Ejecutando testModificarArchivo ")
        #Prueba que se modifique correctamente un archivo en la tabla"""
        ruta_archivo = "audio1.mp3"
        if os.path.exists(ruta_archivo):
            id = "1234"
            nuevo_nombre = "nuevo_audio1"
            nueva_extension = "wav"
            ControladorArchivos.ModificarArchivo(id, nombre=nuevo_nombre, extension=nueva_extension)
            archivo_modificado = ControladorArchivos.ConsultarArchivo(id)
            self.assertIsNotNone(archivo_modificado)
            self.assertEqual(archivo_modificado.nombre, nuevo_nombre)
            self.assertEqual(archivo_modificado.extension, nueva_extension)


if __name__ == '__main__':
    unittest.main()
