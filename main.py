import os
from tabulate import tabulate
from conexion import *
from contactos import *


con = conectar()
crear_tabla(con)

def iniciar():
    os.system('cls')
    print('Seleccione una opción')
    print('\t1. Añadir un contacto')
    print('\t2. Mostrar un contacto')
    print('\t3. Buscar un contacto')
    print('\t4. Modificar un contacto')
    print('\t5. Eliminar un contacto')
    print('\t6. Salir de la aplicación')
    opcion = input('Escoja una opción: ')
    if opcion == '1':
        nuevo_contacto()
    elif opcion == '2':
        ver_contacto()
    elif opcion == '3':
        buscar_contacto()

def nuevo_contacto():
    nombre = input('Ingrese el nombre: ')
    apellidos = input('Ingrese el apellido: ') 
    empresa = input('Ingrese la empresa: ')
    telefono = input('Ingrese el telefono: ')
    email = input('Ingrese el email: ')
    direccion = input('Ingrese la direccion: ')
    respuesta = registrar(nombre, apellidos, empresa, telefono, email, direccion)
    print(respuesta)

def ver_contacto():
    datos = mostrar()
    headers = ['ID','NOMBRE','APELLIDOS','EMPRESA','TELEFONO','EMAIL','DIRECCION',]
    tabla = tabulate(datos,headers, tablefmt='fancy_grid')
    print(tabla)

def buscar_contacto():
    id = input( 'Ingrese el ID del contacto: ')
    datos = buscar(id)
    headers = ['ID','NOMBRE','APELLIDOS','EMPRESA','TELEFONO','EMAIL','DIRECCION',]
    tabla = tabulate(datos,headers, tablefmt='fancy_grid')
    print(tabla)
    


iniciar()

#nombre, apellidos, empresa, telefono, email, direccion 