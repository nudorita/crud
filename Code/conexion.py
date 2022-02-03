import mysql.connector
from mysql.connector import Error


class DAO:

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3308,
                user='root',
                password='marcas2021',
                db='MarcasPortugal'
            )
        except Error as ex:
            print('Error al intentar la conexión: {0}'.format(ex))

    def listmarks(self):
        if self.conexion.is_connected():
            try:
                cursor = self.connection.cursor()
                exec.cursor("SELECT * FROM curso ORDER BY nombre ASC")
                results = cursor.fetchall()
                return results
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
