import string
from dbpython import *
class Actividad:
    def __init__(self, idTrabajo, numero, consigna, respuesta1, respuesta2, respuesta3, correcta):
        self.__idTrabajo = idTrabajo
        self.__consigna = consigna
        self.__respuesta1 = respuesta1
        self.__respuesta2 = respuesta2
        self.__respuesta3 = respuesta3
        self.__correcta = correcta
        self.__numero = numero

#METODOS ---------------------

    def setIdTrabajo(self, idTrabajo):
        self.__idTrabajo = idTrabajo

    def getIdTrabajo(self):
        return self.__idTrabajo

    def setConsigna(self, consigna):
        self.__consigna = consigna

    def getConsigna(self):
        return self.__consigna

    def setRespuesta1(self, respuesta):
        self.__respuesta1 = respuesta

    def getRespuesta1(self):
        return self.__respuesta1

    def setRespuesta2(self, respuesta):
        self.__respuesta2 = respuesta

    def getRespuesta2(self):
        return self.__respuesta2

    def setRespuesta3(self, respuesta):
        self.__respuesta3 = respuesta

    def getRespuesta3(self):
        return self.__respuesta3

    def setCorrecta(self, correcta):
        self.__correcta = correcta

    def getCorrecta(self):
        return self.__correcta

    def setNumero(self, numero):
        self.__numero = numero

    def getNumero(self):
        return self.__numero

    def imprimirDatos(self):
        print "idTrabajo: ", self.getIdTrabajo()
        print "Numero: ", self.getNumero()
        print "Consigna: ", self.getConsigna()
        print "Respuesta1: ", self.getRespuesta1()
        print "Respuesta2: ", self.getRespuesta2()
        print "Respuesta3: ", self.getRespuesta3()
        print "Correcta: ", self.getCorrecta()

    def crearActividad(self, idtrab):
        numconsigna = str(self.getNumero())
        consigna = str(self.getConsigna())
        respuesta1 = str(self.getRespuesta1())
        respuesta2 = str(self.getRespuesta2())
        respuesta3 = str(self.getRespuesta3())
        correcta = str(self.getCorrecta())
        sql = "INSERT INTO actividades(idTrabajo, numero, consigna, respuesta1, respuesta2, respuesta3, correcta) values('" + idtrab + "', '" + numconsigna + "', '" + consigna + "', '" + respuesta1 + "', '" + respuesta2 + "', '" + respuesta3 + "', '" + correcta + "')"
        cursor.execute(sql)
        db.commit()
        sql = "Select numero from actividades where consigna = '" + consigna + "' and respuesta1 = '" + respuesta1 + "' and respuesta2 = '" + respuesta2 + "'"
        cursor.execute(sql)
        row = cursor.fetchone()
        idConsigna = str(row[0])
        return idConsigna
