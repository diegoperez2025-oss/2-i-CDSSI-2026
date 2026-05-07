import itertools
import json

from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas


class MyFirstPDF:

    def agrupador(self, iterable, n):
        # Ayuda a organizar los datos en grupos para las páginas
        args = [iter(iterable)] * n
        return itertools.zip_longest(*args)

    def exportar_a_pdf(self, datos):
        c = canvas.Canvas("grilla-alumnos.pdf", pagesize=LETTER)
        w, h = LETTER
        max_filas_por_pagina = 45
        x_offset = 50
        y_offset = 50
        espaciado = 15

        xlist = [x + x_offset for x in [0, 200, 250, 300, 350, 400, 480]]
        ylist = [h - y_offset - i*espaciado for i in range(max_filas_por_pagina + 1)]

        for filas in self.agrupador(datos, max_filas_por_pagina):
            filas = tuple(filter(bool, filas))
            c.grid(xlist, ylist[:len(filas) + 1])
            for y, fila in zip(ylist[:-1], filas):
                for x, celda in zip(xlist, fila):
                    c.drawString(x + 2, y - espaciado + 3, str(celda))
            c.showPage()
        c.save()

# 1. Esto cargará el archivo json
with open("students.json", "r", encoding="utf-8") as f:
    estudiantes = json.load(f)

# 2. Esto creará la fila del encabezado
datos = [("NOMBRE", "EXAMEN", "NOTA", "GRADO", "GRUPO", "TURNO", "EMAIL")]

# 3. Esto recorrerá cada estudiante y agregará sus datos
for estudiante in estudiantes:
    datos.append((
        estudiante["name"],
        estudiante["exam"],
        estudiante["note"],
        estudiante["grade"],
        estudiante["group"],
        estudiante["shift"],
        estudiante["email"]
    ))

# 4. Genera el PDF con la información de los estudiantes de toda la clase
mi_pdf = MyFirstPDF()
mi_pdf.exportar_a_pdf(datos)
print("¡Archivo creado con éxito!")