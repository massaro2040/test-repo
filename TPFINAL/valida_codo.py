"""
Este módulo se encarga de las validaciones de datos.
"""
import re

class Validar():
     """
        Clase Validar

        En esta clase se encuentran, los metodos para evaluar los datos.
       
     """
     
     
     def __init__(self):
      pass
   
     def control_cantidad(self, cantidad):
        """
            Función control_dni

            Esta función evalúa el dato del campo cantidad.
            
            Retorna "True" en caso de cumplir los requerimientos o un mensaje de error en caso contrario.
       
        """
        cadena = cantidad.get()
        patron = "^[0-9]*$"
        if (re.match(patron, str(cadena))):
          if cadena > 0:
             return True
          else:
             return "Error", "Ingrese un número mayor a cero por favor!" #luego borrar la palabra error
        else:
          return "Error", "Ingrese solo números por favor!"#luego borrar la palabra error
          
     def control_modificar(self, nombre, categoria, procedencia, cantidad):
        """
            Función control_modificar

            Esta función evalúa los datos de los campos de entrada de la aplicación.
            
            Retorna "True" en caso de cumplir los requerimientos o un mensaje de error en caso contrario.
       
        """
        
        cadena1 = nombre.get()
        cadena2 = categoria.get()
        cadena3 = procedencia.get()
        cadena4 = cantidad.get()
        patron = "^[0-9]*$"
        
        if len (cadena1) == 0:
            
            return "El Nombre no debe estar vacio"
        elif len (cadena2) == 0:      
            
            return "La Categoria no debe estar vacia"
        elif len (cadena3) == 0:      
            return "La Procedencia no debe estar vacia"          
        elif cadena4 == 0:
             return "La Cantidad no debe estar vacia"
        elif (re.match(patron, cadena4)):
            if (cadena4) > 0:
                return True
            else:
                return "Error", "Ingrese un número mayor a cero por favor!"
        else:
            return "Error", "Ingrese solo números por favor!"
        
     def control_consulta(self, a):
        """
            Función control_consulta

            Esta función evalúa los datos de los campos de entrada de la aplicación.
            
            Retorna "True" en caso de cumplir los requerimientos o un mensaje de error en caso contrario.
       
        """
        cadena1 = a.get()
        if len (cadena1) == 0:
            
            return "Elija que desea consultar"
        else:
           return True
    
     def control_consulta2(self, id, nomb, cate, proc):
        
        cadena1= id.get()
        cadena2= nomb.get()
        cadena3= cate.get()
        cadena4= proc.get()
        patron = "^[0-9]*$"
        print(cadena1, cadena2, cadena3, cadena4)
       
        if len (cadena1) > 0:
            if (re.match(patron, cadena1)):
                return  "1"
            else:
                return "Error", "Ingrese un ID valido por favor!"
        elif  len (cadena2) > 0:
           return "2" 
        elif len (cadena3) > 0:
           return "3"
        elif len (cadena4) > 0:
           return "4"
        else:
           return "Error", "No selecciono ningun patron de busqueda!"
            
               


