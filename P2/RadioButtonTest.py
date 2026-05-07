from tkinter import *
from tkinter import messagebox
import json

class Loginapp:
    def __init__(self):
        self.window = Tk()
        self.window.title("Lodin Estudiantes")
        self.window.geometry("400x300")
        self.window.resizable(False, False)
        self.students = []
        self.load_students()
        self.create_widgets()
        
    def load_students(self):
        # Cargar estudiantes desde el archivo JSON
        try:
            with open("students.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            # Los datos pueden ser una lista o un diccionario
            if type(data) == list:
                self.students = data
            else:
                self.students = data.get("students", [])

        except FileNotFoundError:
            messagebox.showerror("Error", "¡Archivo students.json no encontrado!\nAsegúrate de que esté en la misma carpeta que Main.py")
            self.students = []
        except json.JSONDecodeError as e:
            messagebox.showerror("Error", f"students.json está dañado o el JSON no es válido:\n{e}")
            self.students = []
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar students.json:\n{e}")
            self.students = []

    def create_widgets(self):
        # Etiqueta de título
        title = Label(self.window, text="Inicio de Sesión de Estudiantes", font=("Arial", 20, "bold"))
        title.pack(pady=20)

        # Marco de usuario
        frame_user = Frame(self.window)
        frame_user.pack(pady=10)
        lbl_user = Label(frame_user, text="Usuario:", font=("Arial", 12), width=12, anchor="e")
        lbl_user.pack(side=LEFT)
        self.entry_user = Entry(frame_user, font=("Arial", 12), width=20)
        self.entry_user.pack(side=LEFT, padx=5)

        # Marco de contraseña
        frame_pass = Frame(self.window)
        frame_pass.pack(pady=10)
        lbl_pass = Label(frame_pass, text="Contraseña:", font=("Arial", 12), width=12, anchor="e")
        lbl_pass.pack(side=LEFT)
        self.entry_pass = Entry(frame_pass, font=("Arial", 12), width=20, show="*")
        self.entry_pass.pack(side=LEFT, padx=5)

        # Botón de inicio de sesión
        btn_login = Button(self.window, text="Iniciar Sesión", command=self.check_login,
                           bg="#4CAF50", fg="white", font=("Arial", 12, "bold"),
                           width=15, height=1)
        btn_login.pack(pady=20)

        # Vincular la tecla Enter para iniciar sesión
        self.window.bind('<Return>', lambda event: self.check_login())
    
    def check_login(self):
        # Obtener texto de las entradas
        username = self.entry_user.get().strip()
        password = self.entry_pass.get().strip()

        # Revisar si están vacíos
        if username == "" or password == "":
            messagebox.showwarning("Advertencia", "Por favor, ingrese usuario y contraseña")
            return

        # Buscar estudiante en la lista
        found = False
        for student in self.students:
            email = student.get("email", "")
            name = student.get("name", "")
            student_password = student.get("password", "")

            # El usuario puede ser el correo o el nombre
            if username.lower() == email.lower() or username.lower() == name.lower():
                found = True
                if password == student_password:
                    self.show_user_data(student)
                else:
                    messagebox.showerror("Error", "Contraseña incorrecta")
                break

        if not found:
            messagebox.showerror("No Encontrado", "El usuario no existe. Por favor, contacte al Administrador.")

    def show_user_data(self, student):
        # Construir mensaje con datos del usuario
        name = student.get("name", "N/A")
        email = student.get("email", "N/A")
        password = student.get("password", "N/A")
        exam = student.get("exam", "N/A")
        grade = student.get("grade", "N/A")
        group = student.get("group", "N/A")
        shift = student.get("shift", "N/A")

        message = "¡Inicio de Sesión Exitoso!\n\n"
        message = message + "Nombre: " + name + "\n"
        message = message + "Correo: " + email + "\n"
        message = message + "Contraseña: " + password + "\n"
        message = message + "Examen: " + str(exam) + "\n"
        message = message + "Grado: " + str(grade) + "\n"
        message = message + "Grupo: " + str(group) + "\n"
        message = message + "Turno: " + str(shift)
        
        messagebox.showinfo("Datos del Usuario", message)

        # Limpiar entradas después de iniciar sesión
        self.entry_user.delete(0, END)
        self.entry_pass.delete(0, END)