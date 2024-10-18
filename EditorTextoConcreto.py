from EditorTextoBase import EditorTextoBase
import tkinter as tk

class EditorTextoConcreto(EditorTextoBase):
    def __init__(self, text_area):
        self.text_area = text_area
        self.start_index = None
        self.end_index = None
        self.text_area.bind("<<Selection>>", self.on_select)

    def on_select(self, event):
        try:
            self.start_index = self.text_area.index(tk.SEL_FIRST)
            self.end_index = self.text_area.index(tk.SEL_LAST)
        except tk.TclError:
            self.start_index = None
            self.end_index = None

    def aplicar_formato(self):
        pass