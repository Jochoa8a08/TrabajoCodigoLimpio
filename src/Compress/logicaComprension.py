import gzip
import os
import pygame


"""
    Reproduce un archivo de audio utilizando pygame.

    Parámetros:
    ruta (str): Ruta al archivo de audio a reproducir.

    Lanza:
    pygame.error: Si ocurre un error durante la reproducción del audio.
    """

def reproducir_audio(ruta):
    pygame.init()
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except pygame.error as e:
        print("Error al reproducir el audio:", e)

class ErrorExtension(Exception):
    """El archivo no tiene la extensión .mp3 o .gz"""

class ErrorNoExist(Exception):
    """El archivo no existe"""

class VacioError(Exception):
    """RUTA VACIA"""

class ErrorArchivoComprimido(Exception):
    """Intento de comprimir un archivo que ya está comprimido"""

class ErrorTamañoGrande(Exception):
    """El tamaño del archivo es muy grande"""

class LongitudExcesiva(Exception):
    pass

class CaracterEspecial(Exception):
    pass

tamaño_umbral_archivo = 301
caracteres_especiales = "@"

"""
    Comprime un archivo de audio en formato .mp3 o .gz.

    Parámetros:
    archivo_original (str): Ruta al archivo de audio original.
    archivo_comprimido (str): Ruta donde se guardará el archivo comprimido.

    Lanza:
    VacioError: Si la ruta del archivo original está vacía.
    ErrorExtension: Si el archivo original no tiene la extensión .mp3 o .gz.
    ErrorNoExist: Si el archivo original no existe.
    LongitudExcesiva: Si la longitud de la ruta del archivo excede los 20 caracteres.
    CaracterEspecial: Si el nombre del archivo original contiene caracteres especiales.
    """
def comprimir_audio(archivo_original, archivo_comprimido):

    
    if not archivo_original.strip():
        raise VacioError("La ruta está vacía")

    if not archivo_original.lower().endswith('.mp3') and not archivo_original.lower().endswith('.gz'):
        raise ErrorExtension("el Audio no tiene la extensión .mp3")

    if not os.path.exists(archivo_original):
        raise ErrorNoExist("El archivo no existe")

    if archivo_original.endswith('.gz'):
        raise ErrorArchivoComprimido("Intento de comprimir un archivo que ya está comprimido")

    if len(archivo_original) > 20:
        raise LongitudExcesiva("La longitud de la ruta del archivo excede los 20 caracteres")

    if any(caracter in archivo_original for caracter in caracteres_especiales):
        raise CaracterEspecial("El nombre del archivo tiene @")
    
    with open(archivo_original, 'rb') as f_in:
        with gzip.open(archivo_comprimido, 'wb') as f_out:
            f_out.writelines(f_in)

def comprimir_audio_tamaño(archivo_original, archivo_comprimido):
    file_size_kb = os.path.getsize(archivo_original) / 1024

    if file_size_kb <= tamaño_umbral_archivo:
        print("El archivo de audio ingresado es corto.")
    elif file_size_kb >= tamaño_umbral_archivo:
        print("El archivo de audio ingresado es largo (300 o más KB).")   
    comprimir_audio(archivo_original, archivo_comprimido)



"""
    Descomprime un archivo de audio comprimido en formato .gz.

    Parámetros:
    archivo_comprimido (str): Ruta al archivo de audio comprimido (.gz).
    archivo_descomprimido (str): Ruta donde se guardará el archivo descomprimido.

    Lanza:
    VacioError: Si la ruta del archivo comprimido está vacía.
    ErrorExtension: Si el archivo comprimido no tiene la extensión .gz.
    ErrorNoExist: Si el archivo comprimido no existe.
    LongitudExcesiva: Si la longitud de la ruta del archivo comprimido excede los 20 caracteres.
    CaracterEspecial: Si el nombre del archivo comprimido contiene caracteres especiales.
    """
        
def descomprimir_audio(archivo_comprimido, archivo_descomprimido):

    archivo_comprimido = os.path.basename(archivo_comprimido)
    
    if not archivo_comprimido.lower().endswith('.mp3') and not archivo_comprimido.lower().endswith('.gz'):
        raise ErrorExtension("La ruta no tiene la extensión .gz")

    if not archivo_descomprimido.strip():
        raise VacioError("La ruta está vacía")
    
    if not os.path.exists(archivo_comprimido):
        raise ErrorNoExist("El archivo no existe")

    if len(archivo_comprimido) > 20:
        raise LongitudExcesiva("La longitud de la ruta del archivo excede los 20 caracteres")

    if any(caracter in archivo_comprimido for caracter in caracteres_especiales):
        raise CaracterEspecial("El nombre del archivo tiene @")

    with gzip.open(archivo_comprimido, 'rb') as f_in:
        with open(archivo_descomprimido, 'wb') as f_out:
            f_out.write(f_in.read())


def descomprimir_audio_tamaño(archivo_comprimido, archivo_descomprimido):
    tamaño_audio = os.path.getsize(archivo_comprimido) / 1024

    if tamaño_audio <= tamaño_umbral_archivo:
        print("El archivo de audio comprimido es corto.")
    elif tamaño_audio >= tamaño_umbral_archivo:
        raise ErrorTamañoGrande("El archivo de audio comprimido es grande (300 o más KB).")

    descomprimir_audio(archivo_comprimido, archivo_descomprimido)
