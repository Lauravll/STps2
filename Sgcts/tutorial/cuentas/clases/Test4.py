from Admin import Admin
from Usuario import Usuario
from dbpython import *
from Peticion import Peticion



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


admin = Admin(user,None)
print admin.traerPeticion(2).getApellido()

print admin.getLst()

#traer lista de peticiones
admin.traerPeticiones()
#aprobar peticion de id=1
admin.aprobarPeticion(admin.traerPeticion(1))
