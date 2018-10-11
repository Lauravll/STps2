import string
from dbpython import *
class TrabajoPractico:
    def __init__(self, id, titulo, materia, carrera, idUsuario):
        self.__titulo = titulo
        self.__materia = materia
        self.__carrera = carrera
        self.__idUsuario = idUsuario

#METODOS ---------------------

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def getTitulo(self):
        return self.__titulo

    def setMateria(self, materia):
        self.__materia = materia

    def getMateria(self):
        return self.__materia

    def setCarrera(self, carrera):
        self.__carrera = carrera

    def getCarrera(self):
        return self.__carrera

    def setIdUsuario(self, idUsuario):
        self.__idUsuario = idUsuario

    def getIdUsuario(self):
        return self.__idUsuario

    def imprimirDatos(self):
        print "Titulo: ", self.getTitulo()
        print "Materia: ", self.getMateria()
        print "Carrera: ", self.getCarrera()


    def traerIDTP(self):
        sql = "Select idTrabajo from trabajos where titulo = '" + self.getTitulo() + "' and materia = '" + self.getMateria() + "' and carrera = '" + self.getCarrera() + "'"
        cursor.execute(sql)
        row = cursor.fetchone()
        idTrabajo = str(row[0])
        return idTrabajo


    def comprobar(self):
        idTrabajo = self.traerIDTP()
        sql = "Select consigna, respuesta from actividades where idTrabajo ='" + idTrabajo + "'"
        cursor.execute(sql)
        row = cursor.fetchone()
        consigna = str(row[0])
        print "Consigna: "+ consigna
        respuesta = str(row[1])
        #print "Respuesta:" + respuesta
        respuestaA = raw_input("Ingrese su respuesta: ")

        # Ignora mayusculas, minusculas, espacios y acentos
        remove = string.punctuation + string.whitespace
        if (respuesta.lower().translate(None, remove) == respuestaA.lower().translate(None, remove)):
            print "Respuesta Verdadera"
        else:
            print "Respuesta Falsa"
