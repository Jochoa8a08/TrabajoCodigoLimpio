from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import os
import sys
import threading

sys.path.append("src")
from Compress.logicaComprension import (
    comprimir_audio, descomprimir_audio, reproducir_audio)

class ComunicacionesApp(App):
    def build(self):
        # Creación del diseño principal
        self.layout = GridLayout(cols=2, padding=20, spacing=20)

        # Widgets de entrada de archivo y nombre
        self.layout.add_widget(Label(text="Ingrese ruta del archivo:(con su extension)"))
        self.file_path = TextInput(font_size=25, multiline=False)
        self.layout.add_widget(self.file_path)

        self.layout.add_widget(Label(text="Nombre de salida"))
        self.file_name = TextInput(font_size=25, multiline=False)
        self.layout.add_widget(self.file_name)

        # Botones para comprimir, descomprimir y reproducir
        compress_button = Button(text="Comprimir", font_size=25)
        compress_button.bind(on_press=self.comprimir)
        self.layout.add_widget(compress_button)

        decompress_button = Button(text="Descomprimir", font_size=25)
        decompress_button.bind(on_press=self.descomprimir)
        self.layout.add_widget(decompress_button)

        self.reproducir_button = Button(text="Reproducir audio descomprimido", font_size=25)
        self.reproducir_button.bind(on_press=self.reproducir)
        self.layout.add_widget(self.reproducir_button)

        # Etiqueta de estado
        self.status_label = Label(font_size=20)
        self.layout.add_widget(self.status_label)


        # Botón para limpiar entradas
        clear_button = Button(text="Limpiar entradas", font_size=25)
        clear_button.bind(on_press=self.limpiar_entradas)
        self.layout.add_widget(clear_button)

        return self.layout

    def limpiar_entradas(self, instance):
        self.file_path.text = ""
        self.file_name.text = ""
        self.status_label.text = "Las Entradas estan limpias"

    def reproducir(self, instance):
        if not hasattr(self, 'playing') or not self.playing:
            file_name = self.file_name.text  +'.mp3'
            try:
                self.playing = True
                threading.Thread(target=self.reproducir_audio, args=(file_name,)).start()
            except Exception as e:
                self.mostrar_popup(str(e))
        else:
            self.mostrar_popup("Ya se está reproduciendo un audio.")

    def reproducir_audio(self, file_name):
        try:
            reproducir_audio(file_name)
        except Exception as e:
            self.mostrar_popup(str(e))
        finally:
            self.playing = False

    def comprimir(self, instance):
        file_path = self.file_path.text
        file_name = self.file_name.text +'.gz'
        compressed_path = os.path.join(os.path.dirname(file_path), file_name)
        try:
            comprimir_audio(file_path, compressed_path)
            self.status_label.text = "Archivo comprimido con éxito!"
        except Exception as e:
            self.mostrar_popup(str(e))
            self.status_label.text ="ERROR"

    def descomprimir(self, instance):
        file_path = self.file_path.text
        file_name = self.file_name.text + '.mp3'
        decompressed_path = os.path.join(os.path.dirname(file_path), file_name)
        try:
            descomprimir_audio(file_path, decompressed_path)
            self.status_label.text = "Archivo descomprimido con éxito!"
        except Exception as e:
            self.mostrar_popup(str(e))
            self.status_label.text ="ERROR"

    def mostrar_popup(self, message):
        popup_layout = GridLayout(cols=1)
        popup_layout.add_widget(Label(text=message))
        close_button = Button(text="Cerrar")
        popup_layout.add_widget(close_button)
        popup = Popup(title="Error", content=popup_layout, size_hint=(None, None), size=(600, 300))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == "__main__":
    ComunicacionesApp().run()
