from FormatoDecorator import FormatoDecorator
class TamañoFuenteDecorator(FormatoDecorator):
    def __init__(self, editor, tamaño_fuente):
        super().__init__(editor)
        self.tamaño_fuente = tamaño_fuente

    def aplicar_formato(self):
        if self._editor.start_index and self._editor.end_index:
            self._editor.text_area.tag_add(f"tamaño_{self.tamaño_fuente}", self._editor.start_index, self._editor.end_index)
            self._editor.text_area.tag_configure(f"tamaño_{self.tamaño_fuente}", font=("Arial", self.tamaño_fuente))