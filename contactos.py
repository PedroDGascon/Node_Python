from conexion import *

def registrar(nombre, apellidos, empresa, telefono, email, direccion):
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' INSERT INTO contactos(
            nombre, apellidos, empresa, telefono, email, direccion)
            values(?, ?, ?, ?, ?, ?)'''
        datos = (nombre, apellidos, empresa, telefono, email, direccion)
        cursor.execute(sentencia_sql,datos)
        con.commit()
        con.close()
        return 'Registro Correcto'
    except sqlite3.Error as err:
        print('Ha ocurrido un error', err)

def mostrar():
    datos = []
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' SELECT * FROM contactos '''
        cursor.execute(sentencia_sql)
        datos = cursor.fetchall()
    except sqlite3.Error as err:
        print('Ha ocurrido un error al consultar los contactos',err)
    return(datos)


def buscar(id):
    datos = []
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' SELECT * FROM contactos WHERE id=? '''
        cursor.execute(sentencia_sql, (id,))
        datos = cursor.fetchall()
        con.close()
    except sqlite3.Error as err:
        print('Ha ocurrido un error al buscar por ID')
    return(datos)

#nombre TEXT NOT NULL,
#apellidos TEXT NOT NULL,
#empresa TEXT NOT NULL,
#telefono TEXT NOT NULL,
#email TEXT NOT NULL,
#direccion TEXT NOT NULL