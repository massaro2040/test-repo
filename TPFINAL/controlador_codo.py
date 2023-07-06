"""
Módulo de control del patron MVC.
Ejecuta la ventana de Tkinter y carga en el treeview con los datos actulizados de la base de datos.

"""

from tkinter import Tk
import vista_codo
#from vista_tpf import Ventana

class Controller():
    """
        Clase Controller

        Se crean atributos de instancia para la ventana master y la instancia de Panel
       
    """
    def __init__(self, master):
        
        self.root = master
        self.objeto_vista=vista_codo.Ventana(self.root)


if __name__ == "__main__":
    master_tk = Tk()
    # PASO 1 - Intancio el controlador
    mi_app= Controller(master_tk)
    # PASO 2 - Intancio el actualizar tree
    mi_app.objeto_vista.obj_de_modelo.actualizar_treeview(mi_app.objeto_vista.tree)
    master_tk.mainloop()
