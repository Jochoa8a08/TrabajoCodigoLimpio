import unittest
import sys
import os
from datetime import date

sys.path.append("src")
sys.path.append(".")

from model.Archivo import Archivo
from controller.ControladorArchivos import ControladorArchivos
from model.Excepciones import ErrorInsertarArchivo, ErrorModificarArchivo,ErrorEliminarArchivo


class ControllerTest(unittest.TestCase):

    def setUpClass():
        """Se ejecuta al inicio de todas las pruebas"""
        print("Invocando setUpClass")
        ControladorArchivos.EliminarTabla()
        ControladorArchivos.CrearTabla()
    
    def setUp(self):
        """ Se ejecuta siempre antes de cada metodo de prueba """
        print("Invocando setUp")
        ControladorArchivos.BorrarFilas()
  
    def testInsertarArchivo(self):
        """Prueba que se inserte correctamente un archivo en la tabla"""
        print("Ejecutando testInsertarArchivo")
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
        """Prueba que se consulte correctamente un archivo en la tabla"""
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
        """Prueba que se modifique correctamente un archivo en la tabla"""
        print("Ejecutando testModificarArchivo ")
        ruta_archivo = "audio1.mp3"
        if os.path.exists(ruta_archivo):
            id = "1234"
            nombre = os.path.basename(ruta_archivo)
            extension = os.path.splitext(nombre)[1][1:]  # Obtener la extensión sin el punto
            tamaño = os.path.getsize(ruta_archivo)
            archivo = Archivo(id=id, nombre=nombre, extension=extension, tamaño=tamaño, fecha_creacion=None)
            ControladorArchivos.InsertarArchivo(archivo)
            nuevo_nombre = "nuevo_audio1"
            nueva_extension = "wav"
            ControladorArchivos.ModificarArchivo(id, nombre=nuevo_nombre, extension=nueva_extension)
            archivo_modificado = ControladorArchivos.ConsultarArchivo(id)
            self.assertIsNotNone(archivo_modificado)
            self.assertEqual(archivo_modificado.nombre, nuevo_nombre)
            self.assertEqual(archivo_modificado.extension, nueva_extension)

    def testEliminarArchivo(self):
        """Prueba la funcionalidad de eliminar archivos"""
        print("Ejecutando testEliminarArchivo")
        ruta_archivo = "4321.mp3"
        if os.path.exists(ruta_archivo):
            id = 4545
            nombre = os.path.basename(ruta_archivo)
            extension = os.path.splitext(nombre)[1][1:]  # Obtener la extensión sin el punto
            tamaño = os.path.getsize(ruta_archivo)
            archivo = Archivo(id=id, nombre=nombre, extension=extension, tamaño=tamaño, fecha_creacion=None)
            ControladorArchivos.InsertarArchivo(archivo)
            ControladorArchivos.EliminarArchivo(id)
            resultado = ControladorArchivos.ConsultarArchivo(id)
            self.assertIsNone(resultado, "Se esperaba None después de eliminar el archivo, pero se encontró algo más.")


    def testErrorInsertar(self):
        """ Prueba que se lance ErrorInsertarArchivo cuando el ID no es un dígito """
        print("Ejecutando testErrorInsertar")
        ruta_archivo = "audio1.mp3"
        if os.path.exists(ruta_archivo):
            id = "abcd"
            nombre = os.path.basename(ruta_archivo)
            extension = os.path.splitext(nombre)[1][1:]  # Obtener la extensión sin el punto
            tamaño = os.path.getsize(ruta_archivo)
            archivo = Archivo(id=id, nombre=nombre, extension=extension, tamaño=tamaño, fecha_creacion=None)
            self.assertRaises(ErrorInsertarArchivo, ControladorArchivos.InsertarArchivo, archivo)
  
    def testErrorConsultar(self):
        
        """Prueba que se retorne None cuando consulte un archivo que no exista"""
        print("Ejecutando testErrorConsultar")
        ruta_archivo = "audio1.mp3"
        id = "1234"
        nombre = os.path.basename(ruta_archivo)
        extension = os.path.splitext(nombre)[1][1:]  # Obtener la extensión sin el punto
        tamaño = os.path.getsize(ruta_archivo)
        archivo = Archivo(id=id, nombre=nombre, extension=extension, tamaño=tamaño, fecha_creacion=None)
        ControladorArchivos.InsertarArchivo(archivo)
        
        os.path.exists(ruta_archivo)  # Esta línea no tiene efecto si no usas su resultado
        id_inexistente = 9999
        resultado = ControladorArchivos.ConsultarArchivo(id_inexistente)
        self.assertIsNone(resultado, "Se esperaba None para un ID inexistente, se recibió algo más.")


    def testErrorModificar(self):
        ruta_archivo = "audio1.mp3"
        if os.path.exists(ruta_archivo):
            id = "1234"
            nombre = os.path.basename(ruta_archivo)
            extension = os.path.splitext(nombre)[1][1:]  # Obtener la extensión sin el punto
            tamaño = os.path.getsize(ruta_archivo)
            archivo = Archivo(id=id, nombre=nombre, extension=extension, tamaño=tamaño, fecha_creacion=None)
            ControladorArchivos.InsertarArchivo(archivo)
        """Prueba que se lance ErrorModificarArchivo cuando se intenta modificar un archivo que no existe o con datos inválidos"""
        print("Ejecutando testErrorModificar")
        id_inexistente = "000999000"
        nuevo_nombre = "nuevo_nombremod"
        nueva_extension = "wav"
        ControladorArchivos.ModificarArchivo(id, nombre=nuevo_nombre, extension=nueva_extension)
        #Verifia que al intentar modificar un archivo que no existe identificandolo por su id lanza error
        self.assertRaises(ErrorModificarArchivo, ControladorArchivos.ModificarArchivo, id_inexistente, nombre=nuevo_nombre,extension=nueva_extension)

    

    def testErrorEliminar(self):
        """Prueba que se lance ErrorEliminarArchivo al intentar eliminar un archivo inexistente"""
        print("Ejecutando testErrorEliminarArchivo")
        id_inexistente = 97384648336840283674647363272782372300  # Asegúrate de que este ID no existe en la base de datos
        with self.assertRaises(ErrorEliminarArchivo):
            ControladorArchivos.EliminarArchivo(id_inexistente)

    
   
if __name__ == '__main__':
    unittest.main()
