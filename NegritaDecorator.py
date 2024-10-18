from FormatoDecorator import FormatoDecorator

class NegritaDecorator(FormatoDecorator):
    def aplicar_formato(self):
        if self._editor.start_index and self._editor.end_index:
            if "negrita" in self._editor.text_area.tag_names(self._editor.start_index):
                self._editor.text_area.tag_remove("negrita", self._editor.start_index, self._editor.end_index)
            else:
                self._editor.text_area.tag_add("negrita", self._editor.start_index, self._editor.end_index)
                self._editor.text_area.tag_configure("negrita", font=("Arial", 12, "bold"))