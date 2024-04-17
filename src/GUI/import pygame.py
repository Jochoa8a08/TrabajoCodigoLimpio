import pygame

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

# Ruta de tu archivo de audio
ruta_audio = "audio_largo.mp3"

reproducir_audio(ruta_audio)
