from FormatoDecorator import FormatoDecorator

class CursivaDecorator(FormatoDecorator):
    def aplicar_formato(self):
        if self._editor.start_index and self._editor.end_index:
            if "cursiva" in self._editor.text_area.tag_names(self._editor.start_index):
                self._editor.text_area.tag_remove("cursiva", self._editor.start_index, self._editor.end_index)
            else:
                self._editor.text_area.tag_add("cursiva", self._editor.start_index, self._editor.end_index)
                self._editor.text_area.tag_configure("cursiva", font=("Arial", 12, "italic"))