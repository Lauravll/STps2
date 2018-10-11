class Peticion:

#CONSTRUCTOR ---------------------
    def __init__(self,idPeticion, nombre, apellido, usuario, clave):

        self.__idPeticion=idPeticion
        self.__nombre = nombre
        self.__apellido = apellido
        self.__usuario = usuario
        self.__clave = clave



    #METODOS ---------------------
    def setIdPeticion(self, idPeticion):
        self.__idPeticion = idPeticion

    def getIdPeticion(self):
        return self.__idPeticion

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre

    def setApellido(self, apellido):
        self.__apellido = apellido

    def getApellido(self):
        return self.__apellido

    def setUsuario(self, usuario):
        self.__usuario = usuario

    def getUsuario(self):
        return self.__usuario

    def setClave(self, clave):
        self.__clave = clave

    def getClave(self):
        return self.__clave



    @property
    def imprimirDatos(self):


        return ("PETICION:\nIdPeticion: "+ str(self.__idPeticion)+" Nombre: "+self.__nombre+" Apellido: "+self.__apellido+ " Usuario: "+self.__usuario+" Password: "+self.__clave+" \n")



    def crearPeticion(self):
        from dbpython import *
        sql = "INSERT INTO peticiones(nombre, apellido, email,clave) values('" + self.getNombre() + "', '" + self.getApellido() + "', '" + self.getUsuario() + "', '" + self.getClave() +  "')"
        cursor.execute(sql)
        db.commit()

    def traerPeticion(self,id ):
        from dbpython import *
        cursor = db.cursor()
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


        return Peticion(idPeticion, nombre, apellido, usuario, clave)
