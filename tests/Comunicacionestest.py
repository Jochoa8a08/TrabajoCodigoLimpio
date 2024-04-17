import unittest
import gzip

# Lo importamos para poder incluir la ruta de busqueda python
import sys
sys.path.append("src")

from Compress import logicaComprension
from Compress.logicaComprension import (comprimir_audio,
                               comprimir_audio_tamaño, 
                               descomprimir_audio, 
                               descomprimir_audio_tamaño)


class TestComprension(unittest.TestCase):

    """ 
        La clase realiza las 10 pruebas unitarias de comprensión de audio que son: 
        Casos normales: 3 
        Casos de error: 4
        Casos excepcionales: 3

    """

    
    def test_comprimir_audio_corto(self): 
        archivo_original = 'audio1.mp3'
        archivo_comprimido = 'audio1_compres.gz'
        archivo_comprension_esperada = 'audio1_bueno.gz'
        comprimir_audio_tamaño(archivo_original, archivo_comprimido)
        self.assertEqual(gzip.open(archivo_comprimido, 'rb').read() , gzip.open(archivo_comprension_esperada, 'rb').read())
    

    
    def test_comprimir_audio_largo(self): 
        archivo_original = 'largo1.mp3'
        archivo_comprimido = 'audio1_largo_compres.gz'
        archivo_comprension_esperada ='largo1_bueno.gz'
        comprimir_audio_tamaño(archivo_original, archivo_comprimido)
        self.assertEqual(gzip.open(archivo_comprimido, 'rb').read() , gzip.open(archivo_comprension_esperada, 'rb').read())
    
    


    def test_comprimir_extension_diferente(self): 
        archivo_original = 'diferente.wav' 
        archivo_comprimido ='compress_dif.wav'
        self.assertRaises(logicaComprension.ErrorExtension, comprimir_audio, archivo_original, archivo_comprimido)
    

    
    def test_comprimir_ruta_vacia(self): 
        archivo_original = ' '  
        archivo_comprimido =' '
        self.assertRaises(logicaComprension.VacioError, comprimir_audio, archivo_original, archivo_comprimido)
    
    def test_comprimir_audio_no_existente(self):
        archivo_original = 'notexist.mp3'
        archivo_comprimido = 'compress_none.gz'
        self.assertRaises(logicaComprension.ErrorNoExist, comprimir_audio, archivo_original, archivo_comprimido)
    
    
    def test_comprimir_archivo_comprimido(self): 
        archivo_original = 'audio1_compres.gz'
        archivo_comprimido = 'compress_none.gz'
        self.assertRaises(logicaComprension.ErrorArchivoComprimido,comprimir_audio,archivo_original,archivo_comprimido)
    
    def test_comprimir_nombre_archivo_largo(self):  
        archivo_original = 'audiolongitudlargo.mp3'
        archivo_comprimido = 'compress_largo.gz'
        try:
            comprimir_audio(archivo_original, archivo_comprimido)
            self.assertEqual(archivo_comprimido, 0)
        except logicaComprension.LongitudExcesiva:
            pass

    def test_comprimir_archivo_caracter_especial(self):
        archivo_original = 'audio@.mp3'
        archivo_comprimido = 'compress_especial.gz'
        try:
            comprimir_audio(archivo_original, archivo_comprimido)
            self.assertEqual(archivo_original,0)
        except logicaComprension.CaracterEspecial:
            pass

class PruebasDescomprension(unittest.TestCase):
    """
        La clase realiza las 10 pruebas unitarias de descomprensión de audio que son: 
        Casos normales: 3 
        Casos de error: 4
        Casos excepcionales: 3
        
    """

    def test_descomprimir_audio_corto(self): 
        archivo_original = 'audio1.mp3'
        archivo_comprimido = 'audio4.gz'
        archivo_descomprimido ='audio1.mp3'
        descomprimir_audio_tamaño(archivo_comprimido, archivo_descomprimido)
        self.assertTrue(archivo_original, archivo_descomprimido)
    
  
    def test_descomprimir_audio_largo(self): 
        archivo_original = 'largo1.mp3'
        archivo_comprimido = 'audio4.gz'
        archivo_descomprimido ='audio1_largo_unzipped.mp3'
        descomprimir_audio_tamaño(archivo_comprimido, archivo_descomprimido)
        self.assertTrue(archivo_original, archivo_descomprimido)   

    def test_descomprimir_audio_any(self): 
        archivo_original = 'diferente.wav'
        archivo_comprimido = 'diferente_compres.gz'
        archivo_descomprimido ='diferente_unzipped.wav'
        descomprimir_audio(archivo_comprimido, archivo_descomprimido)
        self.assertTrue(archivo_original, archivo_descomprimido)
    
   
    def test_descomprimir_extension_diferente(self): 
        archivo_comprimido = 'diferente_compres.rar' 
        archivo_descomprimido ='compress_diferente.wav'
        self.assertRaises(logicaComprension.ErrorExtension, descomprimir_audio, archivo_comprimido, archivo_descomprimido)

    def test_descomprimir_audio_no_existente(self):  
        archivo_comprimido = 'notex.gz'
        archivo_descomprimido = 'compress_new.mp3'
        self.assertRaises(logicaComprension.ErrorNoExist, descomprimir_audio, archivo_comprimido, archivo_descomprimido)

    def test_descomprimir_ruta_vacia(self): 
        archivo_comprimido = 'audio1.mp3'  
        archivo_descomprimido =''
        self.assertRaises(logicaComprension.VacioError,descomprimir_audio, archivo_comprimido, archivo_descomprimido)

    #CASO ERROR 4
    def test_descomprimir_audio_pesado(self): 
        archivo_comprimido ='audio_pesado.gz'
        archivo_descomprimido ='audio_pesado_des.mp3'
        self.assertRaises(logicaComprension.ErrorTamañoGrande, descomprimir_audio_tamaño, archivo_comprimido, archivo_descomprimido)
    
    
    #CASO EXPECIONAL 1
    def test_descomprimir_nombre_archivo_largo(self):  
        archivo_comprimido = 'audio1_largo_compres.gz'
        archivo_descomprimido ='audiolongitudlargo2.mp3'
        try:
            descomprimir_audio(archivo_comprimido, archivo_descomprimido)
            self.assertEqual(archivo_comprimido,0)
        except logicaComprension.LongitudExcesiva:
            pass
    
    #CASO EXCEPCIONAL 2
    def test_descomprimir_archivo_caracter_especial(self):
        archivo_comprimido = 'audio@.gz'
        archivo_descomprimido ='descompres@.mp3'
        try:
            descomprimir_audio(archivo_comprimido, archivo_descomprimido)
            self.assertEqual(archivo_comprimido,0)
        except logicaComprension.CaracterEspecial:
            pass

    
if __name__ == '__main__':
    unittest.main()

