"""
Este módulo se encarga deL GUI con Tkinter.
"""


from tkinter import StringVar
from tkinter import IntVar
from tkinter import ttk
from tkinter import Label
from tkinter import Entry
from tkinter import messagebox
from tkinter import Button
from tkinter import LabelFrame
from tkinter import Tk

from modelo_codo import Crud
import os



class Ventana():
        """
            Clase Ventana

            Esta clase gestiona la ventana de la aplicación.
            
            Se crean atributos de instancia de la clase "Crud()"
       
         """
        def __init__(self, windows):
                
                
                self.obj_de_modelo= Crud()
                self.master=windows
                self.master.title("Trabajo final Martinez Prieto")
                 
                self.master.geometry("600x500")
                
                #para que funciones se debe cargar la ruta extacta desde donde se ejecuta, lo comento a fin de entregarlo y no surja un error
                self.marco= LabelFrame(self.master, text= "Ingreso de productos")
                self.marco.place(x=50, y=20, width=500, height=450)
                BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
                ruta = os.path.join(BASE_DIR, "codoacodo.ico")
                self.master.iconbitmap(ruta) #no se ve muy bien pero lo intente :P
                
                self.var_nombre = StringVar()
                self.var_categoria = StringVar()
                self.var_procedencia = StringVar()
                self.var_cantidad = IntVar()
                self.var_a = StringVar()
                self.var_b = StringVar()
                self.var_a = "1"
                self.var_b = "2"
                


                self.nombre = Label (self.marco, text="Nombre")
                self.nombre.grid(row=2, column=1, sticky="w")
                self.categoria= Label (self.marco, text="Categoría")
                self.categoria.grid(row=3, column=1, sticky="w")
                self.procedencia= Label (self.marco, text="Procedencia")
                self.procedencia.grid(row=4, column=1, sticky="w")
                self.cantidad = Label (self.marco, text="Cantidad")
                self.cantidad.grid(row=5, column=1, sticky="w")

                self.entry_nombre = Entry(self.marco, textvariable=self.var_nombre, width=25)
                self.entry_nombre.grid(row=2, column=2 , pady=5)
                self.categ = ["Herramientas", "Consumibles", "Otros" ]
                self.entry_categoria = ttk.Combobox(self.marco, values= self.categ,  textvariable=self.var_categoria,width=22)
                #self.entry_categoria.current(0)
                self.entry_categoria.grid(row=3, column=2, pady=5)
                self.proc = ["Nacional", "Importado"]
                self.entry_procedencia = ttk.Combobox(self.marco, values= self.proc, textvariable=self.var_procedencia,width=22)
                #self.entry_procedencia.current(0)
                self.entry_procedencia.grid(row=4, column=2, pady=5)
                self.entry_cantidad = Entry(self.marco, textvariable=self.var_cantidad, width=25)
                self.entry_cantidad.grid(row=5, column=2, pady=5)



                self.tree = ttk.Treeview(self.marco)
                self.tree["columns"] = ("col1", "col2", "col3", "col4")
                self.tree.column("#0", width=50, minwidth=50, anchor="w")
                self.tree.column("col1", width=160, minwidth=80, anchor="w")
                self.tree.column("col2", width=110, minwidth=80, anchor="w")
                self.tree.column("col3", width=90, minwidth=80, anchor="center")
                self.tree.column("col4", width=45, minwidth=80, anchor="center")
                self.tree.heading("#0", text="ID")
                self.tree.heading("col1", text="Nombre")
                self.tree.heading("col2", text="Categoria")
                self.tree.heading("col3", text="Procedencia")
                self.tree.heading("col4", text="Cantidad")

                self.tree.bind("<ButtonRelease-1>", lambda evento :self.vista_mostrar(self.var_nombre, self.var_categoria, self.var_procedencia, self.var_cantidad, self.tree,),)

                self.tree.grid(column=0, row=9, columnspan=4, padx=16, pady=10)

                self.boton_g = Button(self.marco, text="Guardar", command=lambda:self.vista_insertar(self.var_nombre, self.var_categoria, self.var_procedencia, self.var_cantidad, self.tree))
                self.boton_g.grid(row=15, column=0, sticky="E")
                self.boton_b = Button(self.marco, text="Borrar", command=lambda:self.vista_borrar(self.var_nombre, self.var_categoria, self.var_procedencia, self.var_cantidad, self.tree))
                self.boton_b.grid(row=15, column=1)
                
                self.boton_m = Button(self.marco, text="consulta que no anda" , width=17, fg = "red", command=lambda: self.ventana_consulta())
                self.boton_m.grid(row=15, column=3)
                self.boton_a = Button(self.marco, text="Modificar", command=lambda:self.vista_modificar(self.var_nombre, self.var_categoria, self.var_procedencia, self.var_cantidad, self.tree))
                self.boton_a.grid(row=15, column=2, sticky="w")

                self.boton_consul_cat = Button(self.marco, text="<- Consultar", command=lambda: self.consular_reporte_vista(self.var_categoria, self.var_a, self.tree), state="active")
                self.boton_consul_cat.grid(row=3, column=3, pady=5)
                self.boton_consul_pro = Button(self.marco, text="<- Consultar", command=lambda: self.consular_reporte_vista(self.var_procedencia, self.var_b, self.tree), state="active")
                self.boton_consul_pro.grid(row=4, column=3, pady=5)

        def consular_reporte_vista(self, a, b, tree):
                retorno = self.obj_de_modelo.consulta_reporte_mod(a, b,  tree)
                messagebox.showinfo("Aviso", retorno)
        

        def vista_insertar(self,a, b, c, d, tree):
               
                """
                Función vista_insertar

                Esta función envia los argumentos a la función "insertar()" de la clase "Crud()".
                
                Retorna un mensaje del estado del alta.
        
                """
                retorno = self.obj_de_modelo.insertar(a, b, c, d, tree)
                messagebox.showinfo("Aviso", retorno)

        def vista_borrar(self,a, b, c, d, tree):
                """
                Función vista_borrar

                Esta función envia los argumentos a la función "borrar()" de la clase "Crud()".
                
                Retorna un mensaje del estado de la baja.
        
                """
                retorno = self.obj_de_modelo.borrar(a, b, c, d, tree)
                messagebox.showinfo("Aviso", retorno)   
                        
        def vista_mostrar(self,a, b, c, d, tree):
                
                """
                Función vista_mostrar

                Esta función envia los argumentos a la función "mostrar()" de la clase "Crud()".
                
                Retorna un mensaje de como debe continuar el operador.
        
                """
                retorno = self.obj_de_modelo.mostrar(a, b, c, d, tree)
                messagebox.showinfo("Aviso", retorno)      

        def vista_modificar(self,a, b, c, d, tree):
                
                """
                Función vista_modificar

                Esta función envia los argumentos a la función modificar() de la clase "Crud()".
                
                Retorna un mensaje del estado de la modificación.
        
                """
                retorno = self.obj_de_modelo.modificar(a, b, c, d, tree)
                messagebox.showinfo("Aviso", retorno)     
    

        def ventana_exit(self, ):
               
                self.master.destroy()

        def ventana_consulta(self, ):
                self.root = Tk()
                self.root.title("Consulta")
                self.root.geometry("300x180")
                BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
                ruta = os.path.join(BASE_DIR, "codoacodo.ico")
                self.root.iconbitmap(ruta) #no se ve muy bien pero lo intente :P
        
                self.var_id_cons = StringVar()        
                self.var_nom_cons = StringVar()
                self.var_cat_cons = StringVar()
                self.var_proc_cons = StringVar()


        
                self.busc_id=Label(self.root, text="Buscar por ID").grid(row=0, column=0, sticky="W", padx=5)
                self.busc_nom=Label(self.root, text="Buscar por Nombre").grid(row=1, column=0, sticky="W", padx=5)
                
                
                self.busc_id_entry = Entry(self.root, textvariable=self.var_id_cons, width=20).grid(row=0, column=1, padx=10, pady=5)
                self.busc_nom_entry = Entry(self.root, textvariable=self.var_nom_cons, width=20).grid(row=1, column=1, padx=10, pady=5)
                        
                self.cat= Label (self.root, text="Buscar por Categoría").grid(row=2, column=0, sticky="w", padx=5, pady=5)
                self.proce= Label (self.root, text="Buscar por Procedencia").grid(row=3, column=0, sticky="w", padx=5, pady=5)              
                
                self.categ = ["Herramientas", "Consumibles", "Otros" ]
                self.entry_categoria = ttk.Combobox(self.root, values= self.categ ,  textvariable=self.var_cat_cons, width=17)
                self.entry_categoria.grid(row=2, column=1, pady=5)
                self.proc = ["Nacional", "Importado"]
                self.entry_procedencia = ttk.Combobox(self.root, values= self.proc, textvariable= self.var_proc_cons, width=17)
                self.entry_procedencia.grid(row=3, column=1, pady=5)

                self.boton_b = Button(self.root, text="Buscar", command=lambda:self.consular_reporte_vista2(self.var_id_cons, self.var_nom_cons, self.var_cat_cons, self.var_proc_cons, self.tree), width=10)
                self.boton_b.grid(row=4, column=0, pady=15)
                self.boton_c = Button(self.root, text="Cancelar", command= lambda: self.quit() , width=10)
                self.boton_c.grid(row=4, column=1, pady=15)
                
                self.root.mainloop()
        
        def quit(self):
                self.root.destroy()

        def consular_reporte_vista2(self, a, b, c, d, tree):
                #ap= a.get()
                print(a)
                retorno = self.obj_de_modelo.consulta_reporte_mod2(a, b, c, d, tree)
                messagebox.showinfo("Aviso", retorno)
                self.quit()
                
                
                        