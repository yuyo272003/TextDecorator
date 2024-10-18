from EditorTextoBase import EditorTextoBase

class FormatoDecorator(EditorTextoBase):
    def __init__(self, editor):
        self._editor = editor

    def aplicar_formato(self):
        self._editor.aplicar_formato()