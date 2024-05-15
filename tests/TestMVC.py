#TestMVC.py
import unittest
import sys
sys.path.append( "src" )
sys.path.append( "." )

import os 
from datetime import date
from model.Archivo import Archivo
from controller.ControladorArchivos import ControladorArchivos 



class ControllerTest(unittest.TestCase):
    ControladorArchivos.CrearTabla()
    
    

    
    def testInsertarArchivo(self):
        #Prueba que se inserte correctamente un archivo en la tabla
        ruta_archivo = "audio1.mp3"
        if os.path.exists(ruta_archivo):
            id = "1234"
            nombre = os.path.basename(ruta_archivo)
            extension = os.path.splitext(nombre)[1][1:]  # Obtener la extensión sin el punto
            tamaño = os.path.getsize(ruta_archivo)
            archivo = Archivo(id=id, nombre=nombre, extension=extension, tamaño=tamaño, fecha_creacion=None)
            ControladorArchivos.InsertarArchivo(archivo)
            self.assertFalse(0, archivo)


    def testConsultarArchivo(self):
        #Prueba que se consulte correctamente un archivo en la tabla"""
        id = 1234
        archivo = ControladorArchivos.ConsultarArchivo(id)
        self.assertIsNotNone(archivo)
        self.assertEqual(id,archivo.id)
            
    def testModificarArchivo(self):
        #Prueba que se modifique correctamente un archivo en la tabla"""
        ruta_archivo = "audio1.mp3"
        if os.path.exists(ruta_archivo):
            id = "1234"
            nuevo_nombre = "nuevo_audio1.mp3"
            nueva_extension = "wav"
            ControladorArchivos.ModificarArchivo(id, nombre=nuevo_nombre, extension=nueva_extension)
            archivo_modificado = ControladorArchivos.ConsultarArchivo(id)
            self.assertIsNotNone(archivo_modificado)
            self.assertEqual(archivo_modificado.nombre, nuevo_nombre)
            self.assertEqual(archivo_modificado.extension, nueva_extension)
    
    def testEliminarArchivo(self):
        #Prueba que se elimine correctamente un archivo en la tabla"""
        id = "1234"
        ControladorArchivos.EliminarArchivo(id)
        
        
     

if __name__ == '__main__':
    unittest.main()