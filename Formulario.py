from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb

class MuestraWidgetsActividad:
    def __init__(self, raiz):
        raiz.title("Procesamiento CSV")
        self.Nombre = StringVar()
        self.ApellidoPaterno = StringVar()
        self.ApellidoMaterno = StringVar()
        self.Correo = StringVar()
        self.Movil = StringVar()
        self.estado = StringVar()
        self.registros = []
        self.crear_interfaz()
        self.cargar_registros()  
        
    def cargar_registros(self):
        self.lista_registros.delete(0,'end')
        self.registros=[]
        try:
            with open("registros.csv", "r") as csvfile:
                lines = csvfile.readlines()
                for line in lines:
                    registro = line.strip().split(",")
                    self.registros.append(registro)
                    self.lista_registros.insert('end', registro)
        except FileNotFoundError:
            self.registros = []
    def actualizar_registros(self):
        self.lista_registros.delete(0, 'end')  # Limpiar la lista de registros
        self.cargar_registros()  # Volver a cargar los registros actualizados
#funcion para crear toda la interfaz
    def crear_interfaz(self):
        mainFrame = ttk.Frame(raiz, padding="10 10 20 10")
        mainFrame.grid(column=0, row=0, padx=10)
        Frame1 = ttk.Frame(mainFrame, padding="20 10 10 10", borderwidth=3, relief="raised")
        Frame1.grid(column=0, row=0, pady=15)
        Frame2 = ttk.Frame(mainFrame, padding="10 10 10 10", borderwidth=3, relief="raised")
        Frame2.grid(column=0, row=1, sticky=(W), pady=15)
        Frame3 = ttk.Frame(mainFrame, padding="10 10 10 10")
        Frame3.grid(column=1, row=0, padx=10)
        Frame4 = ttk.Frame(mainFrame, padding="10 10 10 10")
        Frame4.grid(column=0, row=2, padx=10)

        self.NombreEntry = ttk.Entry(Frame1, width=25)
        self.NombreEntry.grid(column=2, row=1)

        self.ApellidoPaternoEntry = ttk.Entry(Frame1, width=25)
        self.ApellidoPaternoEntry.grid(column=2, row=2, pady=12)

        self.ApellidoMaternoEntry = ttk.Entry(Frame1, width=25)
        self.ApellidoMaternoEntry.grid(column=2, row=3)

        self.CorreoEntry = ttk.Entry(Frame1, width=25)
        self.CorreoEntry.grid(column=2, row=4)

        self.MovilEntry = ttk.Entry(Frame1, width=25)
        self.MovilEntry.grid(column=2, row=5)

        self.estudiante = ttk.Radiobutton(Frame3, text="Estudiante",variable=self.estado,value="Estudiante")
        self.estudiante.grid(column=4, row=2, sticky=(W), padx=12)
        self.empleado = ttk.Radiobutton(Frame3, text="Empleado",variable=self.estado, value="Empleado")
        self.empleado.grid(column=4, row=3, sticky=(W), padx=12)
        self.desempleado = ttk.Radiobutton(Frame3, text="Desempleado",variable=self.estado,value="Desempleado")
        self.desempleado.grid(column=4, row=4, sticky=(W), padx=12)
        ttk.Label(Frame2, text="Aficiones                                                   ").grid(column=0, row=1, pady=12)
        self.leer = ttk.Checkbutton(Frame2, text="Leer")
        self.leer.grid(column=0, row=2, sticky=(W), pady=12)
        self.musica = ttk.Checkbutton(Frame2, text="Música")
        self.musica.grid(column=2, row=2, sticky=(W), pady=12)
        self.videojuegos = ttk.Checkbutton(Frame2, text="Videojuegos")
        self.videojuegos.grid(column=0, row=3, sticky=(W), pady=12)
        self.deportes = ttk.Checkbutton(Frame2, text="Deportes")
        self.deportes.grid(column=2, row=3, sticky=(W), pady=12)

        ttk.Label(Frame1, text="Nombre:").grid(column=1, row=1, sticky=(E))
        ttk.Label(Frame1, text="Apellido Paterno:").grid(column=1, row=2, sticky=(E))
        ttk.Label(Frame1, text="Apellido Materno:").grid(column=1, row=3, sticky=(E))
        ttk.Label(Frame1, text="Correo:").grid(column=1, row=4, sticky=(E))
        ttk.Label(Frame1, text="Móvil:").grid(column=1, row=5, sticky=(E))
        ttk.Label(Frame3, text="Estado:").grid(column=3, row=1, sticky=(E))

        
        ttk.Button(Frame4, text="Guardar", command=self.guardar_registro).grid(column=4, row=5, pady=12)

        self.lista_registros = Listbox(Frame3, height=10, width=50)
        self.lista_registros.grid(column=5, row=2, rowspan=4)
#Funcionar para guardar el registro.
    def guardar_registro(self):
        nombre = self.NombreEntry.get()
        apellido_paterno = self.ApellidoPaternoEntry.get()
        apellido_materno = self.ApellidoMaternoEntry.get()
        correo = self.CorreoEntry.get()
        movil = self.MovilEntry.get()
        estado = self.estado.get()
        aficiones = []
        if self.leer.state():
            aficiones.append("Leer")
        if self.musica.state():
            aficiones.append("Música")
        if self.videojuegos.state():
            aficiones.append("Videojuegos")
        if self.deportes.state():
            aficiones.append("Deportes")

        registro = [nombre, apellido_paterno, apellido_materno, correo, movil, estado, aficiones]
        self.registros.append(registro)
        self.lista_registros.insert('end', registro)

        self.limpiar_campos()

        with open("registros.csv", "a") as csvfile:
            csvfile.write(",".join(str(item)for item in registro) + "\n")
        self.cargar_registros()    

    def limpiar_campos(self):
        self.NombreEntry.delete(0, 'end')
        self.ApellidoPaternoEntry.delete(0, 'end')
        self.ApellidoMaternoEntry.delete(0, 'end')
        self.CorreoEntry.delete(0, 'end')
        self.MovilEntry.delete(0, 'end')
        self.estado.set('')
        self.leer.state(['!selected'])
        self.musica.state(['!selected'])
        self.videojuegos.state(['!selected'])
        self.deportes.state(['!selected'])

    def salir(self):
        if mb.askyesno("Salir", "¿Estás seguro de que deseas salir?"):
            raiz.destroy()

raiz = Tk()
aplicacion = MuestraWidgetsActividad(raiz)
raiz.mainloop()
