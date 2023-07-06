"""
En este módulo se gestiona el registro de los intentos de crear una tabla en la base de datos 
"""
import os

class RegistroLogTablas(Exception):
     """
        Clase RegistroLogTablas

        En esta clase se encuentran, los metodos para registrar en el archivo "log_tpf.txt" los intentos de crear una tabla existente.
        
        Se establece la herencia de la Clase Exception().    

     """

     BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
     ruta = os.path.join(BASE_DIR, "log_tpf.txt")

     def __init__(self, linea, archivo, fecha):
        self.linea = linea
        self.archivo = archivo
        self.fecha = fecha

     def registrar_error(self,):
        """
        Función registrar_error()

        Esta función registra en el archivo "log_tpf.txt" los intentos de crear una tabla existente.   

        """
        log = open(self.ruta, "a")
        print("Se ha intentado crear una tabla existente en ferreteria_db.db desde ", self.archivo, self.linea, self.fecha, file=log)
