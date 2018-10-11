import Usuario
import dbpython
class Admin:
#CONSTRUCTOR ---------------------
    def __init__(self, Usuario):
        self.usuario = Usuario
        self.__lst = []

#METODOS ---------------------

    def setUsuario(self, Usuario):
        self.usuario = Usuario

    def getUsuario(self):
        return self.usuario
    def setLst(self, lst):
        self.__lst.append(lst)

    def getLst(self):
        # type: () -> object
        return self.__lst

    def imprimirDatos(self):
        print "Nombre: ", self.getNombre()
        print "Apellido: ", self.getApellido()
        print "Usuario: ", self.getUsuario()
        print "Password: ", self.getClave()

    def crearUsuario(self, nombre, apellido, usuario, clave):
        cursor = dbpython.db.cursor()
        sql = "INSERT INTO usuarios(usuario,nombre, apellido, clave, tipo) values('"+ usuario + "', '" + nombre + "', '" + apellido + "', '"  + clave +  "', 'Docente')"
        cursor.execute(sql)
        dbpython.db.commit()




#aprueba la peticion y agrega el usuario impactando la tabl usuarios y aprobados
    def aprobarPeticion(self,Peticion):
        cursor = dbpython.db.cursor()

        user= self.getUsuario()
        self.crearUsuario(Peticion.getNombre(),Peticion.getApellido(),Peticion.getUsuario(),Peticion.getClave())
        #sql = "INSERT INTO usuariosxpeticiones (usuario,idPeticion) values('" + self.usuario.getUsuario()+ "', '" +Peticion.getIdPeticion() + "')"
        #cursor.execute(sql)
        #dbpython.db.commit()
        print("peticion aprobada")

#trae las peticiones por id devolviendo un objeto
    def traerPeticion(self,id):

        from Peticion import Peticion
        cursor = dbpython.db.cursor()
        idPeticion=str(id)
        sql = "SELECT * FROM peticiones WHERE idPeticion="+idPeticion
        cursor.execute(sql)
        row = cursor.fetchone()

        # Trigger app correspondient
        idPeticion =str(row[0])
        nombre = str(row[1])
        apellido = str(row[2])
        usuario = str(row[3])
        clave = str(row[4])


        peticion=Peticion(idPeticion, nombre, apellido, usuario, clave)
        return peticion

#trae lista de peticiones devolviendo una lista
    def traerPeticiones(self):

        from Peticion import Peticion
        cursor = dbpython.db.cursor()

        sql = "SELECT * FROM peticiones "
        cursor.execute(sql)

        for idPeticion,nombre,apellido,usuario,clave in cursor.fetchall():
            ("{0} {1} {2} {3} {4} ".format(idPeticion,nombre,apellido,usuario,clave))

            peticion=Peticion(idPeticion, nombre, apellido, usuario, clave)
            print peticion.imprimirDatos
            self.setLst(peticion)
        return self.__lst

