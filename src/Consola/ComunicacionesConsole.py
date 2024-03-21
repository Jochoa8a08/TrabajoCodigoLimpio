import os

import sys
sys.path.append("src")
from Compress import logicaComprension
from Compress.logicaComprension import comprimir_audio, descomprimir_audio
import math

def main():
    while True:
        opcion = input("¿Qué desea hacer? (c para comprimir, d para descomprimir, q para salir): ").lower()
        
        if opcion == 'c':
            comprimir()
        elif opcion == 'd':
            descomprimir()
        elif opcion == 'q':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione 'c', 'd' o 'q'.")

def comprimir():
    ruta_audio_original = input("Ingrese la ruta del archivo de audio original: ")
    ruta_audio_comprimido = 'audio_comconsole.gz'
    
    # Comprimir el audio original
    comprimir_audio(ruta_audio_original, ruta_audio_comprimido)

    tamaño_original = math.ceil(os.path.getsize(ruta_audio_original) / 1024)
    tamaño_comprimido = math.ceil(os.path.getsize(ruta_audio_comprimido) / 1024)

    print("Tamaño del audio original:", tamaño_original, "KB")
    print("Tamaño del audio comprimido:", tamaño_comprimido, "KB")
    print("El proceso de compresión se completó correctamente.")

def descomprimir():
    ruta_audio_comprimido = input("Ingrese la ruta del archivo de audio comprimido: ")
    ruta_audio_descomprimido = 'audio_desconsole.mp3'
    
    # Descomprimir el audio comprimido
    descomprimir_audio(ruta_audio_comprimido, ruta_audio_descomprimido)
    
    tamaño_descomprimido = math.ceil(os.path.getsize(ruta_audio_descomprimido) / 1024)

    print("Tamaño del audio descomprimido:", tamaño_descomprimido, "KB")
    print("El proceso de descompresión se completó correctamente.")

if __name__ == "__main__":
    main()
