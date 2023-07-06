"""
Módulo de gestión de la base de datos
"""


import sqlite3
from excep_codo import RegistroLogTablas
import datetime

class Database():
    """
            Clase Database

            Esta clase gestiona las instrucciones de sqlit3 para ABMC .
            
            Se establece comunicación con la base de datos y se crean las tablas. 
       
    """
    def __init__(self, ):
         
         self.llamar_base()
         self.crear_tablasq3()
        
        
    def llamar_base(self,):
        """
        Comunicación con la base de datos

        Se establece comunicación con la base de datos "ferreteria_db.db"

        Retorna la comunicación con la base de datos.
        
        """ 
        self.con = sqlite3.connect('ferreteria_db.db')
        return self.con    
        
    def crear_tablasq3(self,):
        """
        Creación las tablas en la base de datos

        Se intentan crear las tablas en la base de datos "ferreteria_db.db".

        Caso contrario registra el intento en un archivo txt.

        """ 
        
        try:
            con = self.llamar_base()
            cursor = con.cursor()
            sql = "CREATE TABLE productos(id INTEGER PRIMARY KEY AUTOINCREMENT, Nombre text, Categoria text, Procedencia text, Cantidad integer)"
            cursor.execute(sql)
            con.commit()
        except sqlite3.OperationalError: 
            print("tabla ya creada")
            RegistroLogTablas(1, "db_codo.py", datetime.datetime.now()).registrar_error()
            
        
      
    def insertsq3(self, nombre, categoria, procedencia, cantidad):
        """
        Función insertsq3

        Se insertan en la tabla productos de la base de datos los registos que llegan como argumento a la función.

        Finaliza con un print.

        """
        con=self.con
        cursor=con.cursor()
        data=(nombre.get(), categoria.get(), procedencia.get(), cantidad.get())
        sql="INSERT INTO productos(Nombre, Categoria, Procedencia, Cantidad) VALUES(?, ?, ?, ?)"
        cursor.execute(sql, data)
        con.commit()
        print("Estoy en alta todo ok")


    def consultasq3(self, ):
        """
        Función consultasq3

        Se selecciona de la tabla productos de la base de datos los registos.

        Retorna todos los registros de "productos".

        """
        sql = "SELECT * FROM productos ORDER BY id ASC" 
        con = self.llamar_base()
        cursor = con.cursor()
        datos = cursor.execute(sql)
        resultado = datos.fetchall()
        return resultado
    

    def bajasq3(self, mi_id):
        """
        Función bajasq3

        Se elimina de la tabla productos de la base de datos los registos asociados al ID que llega como argumento.
        
        """

        con = self.llamar_base()
        cursor = con.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?;", (mi_id,))
        con.commit()

    def modificasq3(self , nombre, categoria, procedencia, cantidad, mi_id ):
        """
        Función modificasq3

        Se modifican de la tabla productos en la base de datos los registos que llegan como argumento a esta función.
        
        """

        con = self.llamar_base()
        cursor=con.cursor()
        data = (nombre.get(), categoria.get(), procedencia.get(), cantidad.get(), mi_id)
        sql = "UPDATE productos SET Nombre=?, categoria=?, procedencia=?, cantidad=?  WHERE id=?;"
        cursor.execute(sql, data)
        con.commit()

    def consulta_por_id (self, mi_id):
        """
        Función consulta_por_id

        Se selecciona de la tabla productos de la base de datos los registos asociados al ID que llega como argumento.

        Retorna todos los registros de "productos" asociados al ID que llega como argumento.

        """
        con = self.llamar_base()
        cursor=con.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = ?", (mi_id,))
        row = cursor.fetchone()
        return row
    
    def consulta_por_x(self, a, b):
        """
        Función consulta_por_x

        Se selecciona de la tabla productos de la base de datos los registos asociados a los nombres de las tablas que llegan como argumento.

        Retorna todos los registros de "productos" asociados la categoria o procedencia segun lo seleccionado previamente que llega como argumento.

        """
        con = self.llamar_base()
        cursor=con.cursor()
        var = b
        if var == "1":
            cursor.execute("SELECT * FROM productos WHERE categoria= ?", [a.get()])
            row = cursor.fetchall()
            return row
        else:
            cursor.execute("SELECT * FROM productos WHERE procedencia= ?", [a.get()])
            row = cursor.fetchall()
            return row
    
    def consulta_por_nombre (self, nomb):
        """
        Función consulta_por_id

        Se selecciona de la tabla productos de la base de datos los registos asociados al ID que llega como argumento.

        Retorna todos los registros de "productos" asociados al ID que llega como argumento.

        """
        con = self.llamar_base()
        cursor=con.cursor()
        cursor.execute("SELECT * FROM productos WHERE Nombre = ?", (nomb,))
        row = cursor.fetchall()
        return row