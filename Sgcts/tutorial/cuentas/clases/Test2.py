from Usuario import Usuario
from dbpython import *
from TrabajoPractico import TrabajoPractico

sql = "SELECT * from usuarios WHERE usuario='SMartins'"
cursor.execute(sql)
row = cursor.fetchone()
idUsuario = str(row[0])

titulo = raw_input("Ingrese Titulo del Trabajo: ")
materia = raw_input("Ingrese la Materia: ")
carrera = raw_input("Ingrese la Carrera: ")
tp = TrabajoPractico(titulo,materia,carrera,idUsuario)
tp.comprobar()