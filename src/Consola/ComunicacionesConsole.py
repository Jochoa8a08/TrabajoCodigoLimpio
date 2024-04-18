import os
import sys

sys.path.append("src")
from Compress.logicaComprension import comprimir_audio, descomprimir_audio, reproducir_audio

def main():
    while True:
        print("BIENVENIDO")
        print("Seleccione una opción:")
        print("a - Comprimir archivo de audio")
        print("b - Descomprimir archivo de audio")
        print("c - Reproducir archivo de audio")
        print("d - Salir del programa")
        
        opcion = input("¿Qué desea hacer? ").lower()
        
        if opcion == 'a':
            comprimir()
        elif opcion == 'b':
            descomprimir()
        elif opcion == 'c':
            reproducir()
        elif opcion == 'd':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione 'a', 'b', 'c' o 'd'.")

def comprimir():
    ruta_audio_original = input("Ingrese la ruta del archivo de audio original: ")
    nombre_salvar = input("Ingrese el nombre con el que desea guardar el archivo comprimido (sin extensión): ")
    ruta_audio_comprimido = nombre_salvar + '.gz'
    
    try:
        # Verificar si el archivo original existe
        if not os.path.exists(ruta_audio_original):
            print("El archivo de audio original no existe.")
            return
        
        """Llama a la función comprimir audio"""
        comprimir_audio(ruta_audio_original, ruta_audio_comprimido)
    
        tamaño_original = os.path.getsize(ruta_audio_original) / 1024
        tamaño_comprimido = os.path.getsize(ruta_audio_comprimido) / 1024

        print("Tamaño del audio original:", tamaño_original, "KB")
        print("Tamaño del audio comprimido:", tamaño_comprimido, "KB")
        print("El proceso de compresión se completó correctamente.")
    except Exception as e:
        print("Error durante la compresión:", e)

def descomprimir():
    ruta_audio_comprimido = input("Ingrese la ruta del archivo de audio comprimido (con extensión .gz): ")
    guardar_nombre = input("Ingrese el nombre con el que desea guardar su audio descomprimido (sin extensión): ")
    ruta_audio_descomprimido = guardar_nombre + '.mp3'
    
    try:
        # Verificar si el archivo comprimido existe
        if not os.path.exists(ruta_audio_comprimido):
            print("El archivo comprimido no existe.")
            return
        
        """Descomprimir el audio comprimido"""
        descomprimir_audio(ruta_audio_comprimido, ruta_audio_descomprimido)
    
        tamaño_descomprimido = os.path.getsize(ruta_audio_descomprimido) / 1024

        print("Tamaño del audio descomprimido:", tamaño_descomprimido, "KB")
        print("El proceso de descompresión se completó correctamente.")
        
    except Exception as e:
        print("Error durante la descompresión:", e)

def reproducir():
    ruta_audio = input("Ingrese la ruta del archivo de audio que desea reproducir(con su extension)")
    try:
        if not os.path.exists(ruta_audio):
            print("El archivo de audio no existe.")
            return
        
        reproducir_audio(ruta_audio)
    except Exception as e:
        print("Error al reproducir el audio:", e)

if __name__ == "__main__":
    main()
