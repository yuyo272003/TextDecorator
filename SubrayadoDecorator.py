from FormatoDecorator import FormatoDecorator

class SubrayadoDecorator(FormatoDecorator):
    def aplicar_formato(self):
        if self._editor.start_index and self._editor.end_index:
            if "subrayado" in self._editor.text_area.tag_names(self._editor.start_index):
                self._editor.text_area.tag_remove("subrayado", self._editor.start_index, self._editor.end_index)
            else:
                self._editor.text_area.tag_add("subrayado", self._editor.start_index, self._editor.end_index)
                self._editor.text_area.tag_configure("subrayado", font=("Arial", 12, "underline"))