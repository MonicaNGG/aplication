import pymysql.cursors

class Conexion:

    def __init__(self, servidor, usuario, clave, base_datos):
        self.db = pymysql.connect(host = servidor,
                             user = usuario,
                             password = clave,
                             database = base_datos,
                             cursorclass = pymysql.cursors.DictCursor)
        self.cursor = self.db.cursor()
        print("Conexión a Base de datos exitosa")

    def consulta_sp(self, sql):
        self.cursor.execute(sql)
        return self.cursor

    def consulta_cp(self, sql,tupla):
        self.cursor.execute(sql,tupla)
        return self.cursor

    def cerrar_conexion(self):
        self.db.close()
        print("Base de datos desconectada")

    def commit(self):
        self.db.commit()
        return

    def rollback(self):
        self.db.rollback()
        return