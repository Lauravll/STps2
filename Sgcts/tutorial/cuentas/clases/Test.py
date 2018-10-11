from Admin import Admin
from Usuario import Usuario
from dbpython import *

sql = "SELECT usuario from usuarios WHERE usuario='SMartins'"
cursor.execute(sql)
row = cursor.fetchone()
usuario = str(row[0])
admin = Admin(usuario, None)
#CARGAR UN REGISTRO DE TIPO USUARIO----------
admin.crearUsuario("Fabricio", "Bustos", "Best4ARG", "CAI", "Profesor")
#CARGAR UN REGISTRO DE TIPO TP----------
sql = "SELECT * from usuarios WHERE usuario='SMartins'"
cursor.execute(sql)
row = cursor.fetchone()
idUsuario = str(row[0])
nombre = str(row[1])
apellido = str(row[2])
usuario = str(row[3])
clave = str(row[4])
tipo = str(row[5])
user = Usuario(idUsuario, nombre, apellido, usuario, clave, tipo)
user.crearTrabajoPractico()


