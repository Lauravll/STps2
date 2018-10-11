from Peticion import Peticion

#crea peticiones
"""""
nombre = raw_input("Ingrese nombre: ")
apellido = raw_input("Ingrese apellido: ")
usuario = raw_input("Ingrese usuario: ")
password = raw_input("Ingrese password: ")
tipo = raw_input("Ingrese tipo: ")
peticion=Peticion(None,nombre,apellido,usuario,password,tipo)



Peticion.crearPeticion(peticion)

"""

peticion1=Peticion(None,None,None,None,None,None)

print(peticion1.traerPeticion(2).getApellido())

print(peticion1.traerPeticion(1).getUsuario())
peticion2=Peticion.traerPeticion(peticion1,1)
print peticion2.getIdPeticion()
