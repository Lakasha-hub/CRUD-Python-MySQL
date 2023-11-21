import mysql.connector
from mysql.connector import Error

class DAO():

    # Inicializacion de la conexión a la Base de Datos
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host = "localhost",
                port = 3306,
                user = "root",
                password = "123_python_4576",   
                db = "comercio"
            )
        except Error as error:
            print("Error al intentar conectarse a la Base de Datos: {0}".format(error))
    
    # Función que retorna los productos
    def listar_productos(self):
        # Si la conexión se realizo correctamente:
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                # Consulto la base de datos de los productos y luego los retorno
                cursor.execute("SELECT * FROM productos ORDER BY titulo ASC")
                productos = cursor.fetchall()
                return productos
            except Error as error:
                print("Error al intentar conectarse a la Base de Datos: {0}".format(error))
    
    # Función que agrega nuevos productos
    def agregar_producto(self, nuevo_producto):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                
                # Inserto el nuevo producto en la base de datos
                operacion = """INSERT INTO productos (titulo, precio, categoria, codigo_prod) 
                VALUE ('{0}', {1}, '{2}', '{3}')"""

                cursor.execute(operacion.format(nuevo_producto[0],
                 nuevo_producto[1], nuevo_producto[2], nuevo_producto[3]))
                self.connection.commit()
            except Error as error:
                print("Error al intentar conectarse a la Base de Datos: {0}".format(error))
    
    # Función que actualiza un producto
    def actualizar_producto(self, prod_actualizado):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                
                # Actualizo con los nuevos valores al producto en la base de datos
                operacion = """UPDATE productos SET titulo = '{0}', 
                precio = {1}, categoria = '{2}' WHERE codigo_prod = '{3}'"""
                
                cursor.execute(operacion.format(prod_actualizado[0], 
                    prod_actualizado[1], prod_actualizado[2], prod_actualizado[3]))
                self.connection.commit()
            except Error as error:
                print("Error al intentar conectarse a la Base de Datos: {0}".format(error))

    # Función que elimina un producto
    def eliminar_producto(self, codigo_producto):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                # Elimino el producto de la base de datos por su código
                cursor.execute(f"DELETE FROM productos WHERE codigo_prod = '{codigo_producto}'")
                self.connection.commit()
            except Error as error:
                print("Error al intentar conectarse a la Base de Datos: {0}".format(error))