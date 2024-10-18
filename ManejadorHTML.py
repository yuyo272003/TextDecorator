import tkinter as tk
from tkinter import filedialog, messagebox
from html.parser import HTMLParser

class ManejadorHTML:
    def __init__(self, text_area):
        self.text_area = text_area

    def guardar_como_html(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".html",
                                                 filetypes=[("Archivos HTML", "*.html"), ("Todos los Archivos", "*.*")])
        if file_path:
            try:
                contenido_html = self.convertir_a_html()
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(contenido_html)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

    def convertir_a_html(self):
        contenido = self.text_area.get(1.0, tk.END)
        tags = self.text_area.tag_ranges(tk.SEL)
        
        html = "<html><body>"
        start = "1.0"
        for tag in tags:
            end = tag
            fragment = self.text_area.get(start, end)

            # Aplicar los decoradores al HTML
            if "negrita" in self.text_area.tag_names(start):
                fragment = f"<b>{fragment}</b>"
            if "cursiva" in self.text_area.tag_names(start):
                fragment = f"<i>{fragment}</i>"
            if "subrayado" in self.text_area.tag_names(start):
                fragment = f"<u>{fragment}</u>"
            tamaño = self.obtener_tamaño_fuente(start)
            if tamaño:
                fragment = f"<span style='font-size:{tamaño}px'>{fragment}</span>"

            html += fragment
            start = end

        html += "</body></html>"
        return html

    def obtener_tamaño_fuente(self, index):
        for tag in self.text_area.tag_names(index):
            if tag.startswith("tamaño_"):
                return tag.split("_")[1]
        return None

    def abrir_archivo_html(self):
        file_path = filedialog.askopenfilename(defaultextension=".html",
                                               filetypes=[("Archivos HTML", "*.html"), ("Todos los Archivos", "*.*")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    contenido_html = file.read()
                    self.cargar_desde_html(contenido_html)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo: {e}")

    def cargar_desde_html(self, html):
        self.text_area.delete(1.0, tk.END)

        class MyHTMLParser(HTMLParser):
            def __init__(self, text_area):
                super().__init__()
                self.text_area = text_area
                self.current_tags = []
                self.current_size = None

            def handle_starttag(self, tag, attrs):
                if tag == "b":
                    self.current_tags.append("negrita")
                elif tag == "i":
                    self.current_tags.append("cursiva")
                elif tag == "u":
                    self.current_tags.append("subrayado")
                elif tag == "span":
                    for attr in attrs:
                        if attr[0] == "style" and "font-size" in attr[1]:
                            self.current_size = attr[1].split(":")[1].replace("px", "").strip()

            def handle_endtag(self, tag):
                if tag == "b":
                    self.current_tags.remove("negrita")
                elif tag == "i":
                    self.current_tags.remove("cursiva")
                elif tag == "u":
                    self.current_tags.remove("subrayado")
                elif tag == "span":
                    self.current_size = None

            def handle_data(self, data):
                start = self.text_area.index(tk.INSERT)
                self.text_area.insert(tk.INSERT, data)
                end = self.text_area.index(tk.INSERT)
                
                # Aplicar los tags correspondientes
                for tag in self.current_tags:
                    self.text_area.tag_add(tag, start, end)
                if self.current_size:
                    size_tag = f"tamaño_{self.current_size}"
                    self.text_area.tag_add(size_tag, start, end)
                    self.text_area.tag_configure(size_tag, font=("Arial", int(self.current_size)))

        parser = MyHTMLParser(self.text_area)
        parser.feed(html)
