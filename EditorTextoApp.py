import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from EditorTextoConcreto import EditorTextoConcreto
from NegritaDecorator import NegritaDecorator
from CursivaDecorator import CursivaDecorator
from SubrayadoDecorator import SubrayadoDecorator
from TamañoFuenteDecorator import TamañoFuenteDecorator
from ManejadorHTML import ManejadorHTML

class EditorTextoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Editor de Texto Enriquecido")
        self.geometry("600x400")

        # Crear el área de texto
        self.text_area = tk.Text(self, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(expand=True, fill='both')

        # Crear el editor base
        self.editor_base = EditorTextoConcreto(self.text_area)

        # Inicializar el manejador HTML
        self.manejador_html = ManejadorHTML(self.text_area)

        # Crear la barra de menú
        self.menu_bar = tk.Menu(self)

        # Crear el menú de archivo
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Abrir", command=self.abrir_archivo)
        file_menu.add_command(label="Guardar Como", command=self.guardar_archivo)
        file_menu.add_command(label="Abrir HTML", command=self.abrir_archivo_html)
        file_menu.add_command(label="Guardar Como HTML", command=self.guardar_archivo_html)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.quit)
        self.menu_bar.add_cascade(label="Archivo", menu=file_menu)

        # Crear el menú de formato
        format_menu = tk.Menu(self.menu_bar, tearoff=0)
        format_menu.add_command(label="Negrita", command=self.aplicar_negrita)
        format_menu.add_command(label="Cursiva", command=self.aplicar_cursiva)
        format_menu.add_command(label="Subrayado", command=self.aplicar_subrayado)
        format_menu.add_command(label="Cambiar Tamaño de Fuente", command=self.cambiar_tamaño_fuente)
        self.menu_bar.add_cascade(label="Formato", menu=format_menu)

        # Configurar la barra de menú
        self.config(menu=self.menu_bar)

    def abrir_archivo(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Archivos de Texto", "*.txt"), ("Todos los Archivos", "*.*")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    contenido = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, contenido)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo: {e}")

    def guardar_archivo(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Archivos de Texto", "*.txt"), ("Todos los Archivos", "*.*")])
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    contenido = self.text_area.get(1.0, tk.END)
                    file.write(contenido)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

    def abrir_archivo_html(self):
        self.manejador_html.abrir_archivo_html()

    def guardar_archivo_html(self):
        self.manejador_html.guardar_como_html()

    def aplicar_negrita(self):
        negrita = NegritaDecorator(self.editor_base)
        negrita.aplicar_formato()

    def aplicar_cursiva(self):
        cursiva = CursivaDecorator(self.editor_base)
        cursiva.aplicar_formato()

    def aplicar_subrayado(self):
        subrayado = SubrayadoDecorator(self.editor_base)
        subrayado.aplicar_formato()

    def cambiar_tamaño_fuente(self):
        tamaño = simpledialog.askinteger("Tamaño de Fuente", "Introduce el tamaño de la fuente:")
        if tamaño:
            tamaño_fuente_decorator = TamañoFuenteDecorator(self.editor_base, tamaño)
            tamaño_fuente_decorator.aplicar_formato()
