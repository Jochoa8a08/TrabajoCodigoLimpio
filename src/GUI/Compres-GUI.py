from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
import os
import sys

sys.path.append("src")
from Compress.logicaComprension import (
    comprimir_audio, comprimir_audio_tamaño_corto, comprimir_audio_tamaño_largo, 
    descomprimir_audio, descomprimir_audio_tamaño_corto, descomprimir_audio_tamaño_largo,
    ErrorExtension, ErrorNoExist, VacioError, ErrorArchivoComprimido, ErrorTamañoGrande, LongitudExcesiva, CaracterEspecial
)

class CompressApp(App):
    def build(self):
        layout = GridLayout(cols=2, padding=20, spacing=20)

        layout.add_widget(Label(text="Ruta del archivo:"))
        self.file_path = TextInput(font_size=20, multiline=False)
        layout.add_widget(self.file_path)

        layout.add_widget(Label(text="Nombre de salida:"))
        self.file_name = TextInput(font_size=20, multiline=False)
        layout.add_widget(self.file_name)

        compress_button = Button(text="Comprimir", font_size=20)
        layout.add_widget(compress_button)
        compress_button.bind(on_press=self.handle_compression)

        decompress_button = Button(text="Descomprimir", font_size=20)
        layout.add_widget(decompress_button)
        decompress_button.bind(on_press=self.handle_decompression)

        self.status_label = Label(font_size=18)
        layout.add_widget(self.status_label)
        layout.add_widget(Label())

        return layout

    def handle_compression(self, instance):
        file_path = self.file_path.text
        file_name = self.file_name.text + '.gz'
        compressed_path = os.path.join(os.path.dirname(file_path), file_name)
        try:
            comprimir_audio(file_path, compressed_path)
            self.status_label.text = "Archivo comprimido con éxito!"
        except Exception as e:
            self.show_popup(str(e))

    def handle_decompression(self, instance):
        file_path = self.file_path.text
        if not file_path.lower().endswith('.gz'):
            file_path += '.gz'  # Añade automáticamente la extensión .gz si no está presente
        file_name = self.file_name.text
        decompressed_path = os.path.join(os.path.dirname(file_path), file_name)
        try:
            descomprimir_audio(file_path, decompressed_path)
            self.status_label.text = "Archivo descomprimido con éxito!"
        except Exception as e:
            self.show_popup(str(e))

    def show_popup(self, message):
        popup_layout = GridLayout(cols=1)
        popup_layout.add_widget(Label(text=message))
        close_button = Button(text="Cerrar")
        popup_layout.add_widget(close_button)
        popup = Popup(title="Error", content=popup_layout, size_hint=(None, None), size=(600, 300))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == "__main__":
    CompressApp().run()
