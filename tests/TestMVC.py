#TestMVC.py
import unittest
import sys

sys.path.append("src")

from datetime import date
from model.Archivo import Archivo
from controller.ControladorArchivos import ControladorArchivos

class ControllerTest(unittest.TestCase):

    def testCreateTable(self):
        """ Prueba que se cree correctamente la tabla en la BD """

        # Llamar a la clase Controlador para que cree la tabla
        ControladorArchivos.EliminarTabla()
        ControladorArchivos.CrearTabla()

        # Insertar un Usuario en la tabla
        archivo_prueba = Archivo(id="1010", nombre="Audio1", extension=".mp3", tamaño="10",fecha_creacion="")
        ControladorArchivos.InsertarArchivo(archivo_prueba)

        # Buscar al usuario
        archivo_buscado = ControladorArchivos.BuscarArchivoid("1010")

        # Verificar Si lo trajo correctamente
        self.assertEqual(archivo_prueba.id, archivo_buscado.id)


if __name__ == '__main__':
    unittest.main()