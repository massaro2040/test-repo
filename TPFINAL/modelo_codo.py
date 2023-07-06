"""
En este módulo perteneciente al patrón MVC se gestiona ABMC

"""
import re
from db_codo import Database
from valida_codo import Validar

#FUNCIONES: MODELO

class Crud(Database):
    """
        Clase Crud

        En esta clase se encuentran, los metodos para dar ALTA, BAJA, MODIFICACIÓN y CONSULTA a la base de datos
        
        Se establece la herencia de la Clase Database().    

        Se crean atributos de instancia para validar campos.
               
    """
    def __init__(self):
       
        super(Crud, self).__init__()
        self.obj_control=Validar()
         
        



    def insertar(self, nombre, categoria, procedencia, cantidad, tree): #ALTA DE DATOS
        
        """
        Alta de los datos en la base de datos

        Se verifica el DNI en el metodo "control_dni()" de la clase "Validar()".

        Si "Validar()" devuelve "True" se dan de alta los datos en la DB.

        Retorna un mensaje según el caso.
        
        """
        retorno=self.obj_control.control_cantidad(cantidad)
        if retorno == True:
                self.insertsq3(nombre, categoria, procedencia, cantidad)
                self.actualizar_treeview(tree)
                nombre.set("")
                cantidad.set("")
                procedencia.set("")
                cantidad.set("")
                return "Su registro se logro guardar"
        else: 
                return retorno

        
        

    def actualizar_treeview(self, tree): #ACTUALIZACION DEL TREE, CONSULTA LA db Y LA IMPRIME EN EL TREE
        super(Crud, self).consultasq3()
        """
        Actualizar el Treeview de Tkinter

        Se Eliminan todos los elementos del Treeview seleccionados en la variable "records".
        
        A través del metodo "consultasq3()" se realiza una consulta a la DB y se insertan los datos en el Treeview.
       
        """
        records = tree.get_children()
        for element in records:
            tree.delete(element)

        resultado = self.consultasq3()
        for fila in resultado:
            tree.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4]))

    
    
    def borrar(self, nombre, categoria, procedencia, cantidad, tree): #BAJA DE DATOS
        
        """
        
        Borrar registros en la base de datos

        Se Eliminan los registros, seleccionados desde el Treeview con el metodo "bajasq3()" de la clase "Database()".
        
        Si se toca el boton "Borrar" sin seleccionar un registro en el Treeview aparece un mensaje.

        Luego se borra el elemento seleccionado en el Treeview y se dejan los entrys vacios.

        :finalmente retorna un mensaje donde informa que se elimino segun el ID seleccionado.
       
        """
        seleccion = tree.selection()
        if not seleccion:
            return "No eligió ningun dato para borrar!"
        
        item = tree.item(seleccion)
        mi_id = item['text']
        self.bajasq3(mi_id)
        tree.delete(seleccion)
        
        nombre.set("")
        categoria.set("")
        procedencia.set("")
        cantidad.set("")
        return ("Eliminó con exito la posición ID: " + str(mi_id)) 

    
    
    def modificar(self, nombre, categoria, procedencia, cantidad, tree): #MODICACION DE DATOS EN db
        """
        Modificación de los datos en la base de datos

        Si se toca el boton "Modificar" sin seleccionar un registro en el Treeview aparece un mensaje.

        Se verifica los ingresos en los campos de entrada con en el metodo "control_modificar()" de la clase "Validar()".

        Si "Validar()" devuelve "True" se modifican los datos en la DB.

        Retorna un mensaje según el caso.
        
        """
        
        seleccion = tree.selection()
        if not seleccion:
            return "No eligió ningún dato para modificar"
        item = tree.item(seleccion)
        mi_id = item['text']
        
        retorno=self.obj_control.control_modificar(nombre, categoria, procedencia, str(cantidad))
        
        if retorno == True:          
                self.modificasq3(nombre, categoria, procedencia, cantidad, mi_id)
                self.actualizar_treeview(tree)
                nombre.set("")
                categoria.set("")
                procedencia.set("")
                cantidad.set("")
                return ("Modificó con exito la posición ID: " + str(mi_id))
        else:
                return retorno
        

        
    def mostrar(self, nombre, categoria, procedencia, cantidad, tree): #LLENADO DE ENTRYS PARA LUEGO MODIFICAR EN db
        """
        Llenado de campos de entrada con los datos del ID elegido en el Treeview
     
        Si se toca el boton "modificar" sin seleccionar un registro en el Treeview aparece un mensaje.

        Luego con el metodo "consulta_por_id()" de la clase "Database()" se seleccionan los registros.

        Se completan de campos de entrada con los datos de la consulta.

        Finalmente retorna un mensaje.
        """
        seleccion = tree.selection()
        if not seleccion:
            return "No eligió ningún dato para modificar"
        item = tree.item(seleccion)
        mi_id = item['text']
        row=self.consulta_por_id(mi_id)
        nombre.set("")
        nombre.set(row[1])
        categoria.set("")
        categoria.set(row[2])
        procedencia.set("")
        procedencia.set(row[3])
        cantidad.set("")
        cantidad.set(row[4])
        return "Ahora puede *Modificar* o *Borrar* el registros si desea"
    
    
    def consulta_reporte_mod(self, a, b, tree):
        retorno=self.obj_control.control_consulta(a)
        
        if retorno == True:          
            records = tree.get_children()
            for element in records:
                tree.delete(element)

            resultado = self.consulta_por_x(a, b)
            
            for fila in resultado:
                tree.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4]))
            a.set("")
            return "Consulta en pantalla"
        else:
             return retorno
        
    def consulta_reporte_mod2(self, a, b, c, d, tree):
        retorno=self.obj_control.control_consulta2(a, b, c, d)
        
        if len (retorno) == 1:          
            records = tree.get_children()
            for element in records:
                tree.delete(element)
            if retorno == "1":
                resultado = self.consulta_por_id(a)
            elif retorno == "2":
                 resultado = self.consulta_por_nombre(b)
            elif retorno == "3":
                 resultado = self.consulta_por_x(c, "1")     
            elif retorno == "4":
                 resultado = self.consulta_por_x(d,"2") 

            for fila in resultado:
                tree.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4]))
            a.set("")
            b.set("")
            c.set("")
            d.set("")
            return "Consulta en pantalla"
        else:
             return retorno
        

        
        


