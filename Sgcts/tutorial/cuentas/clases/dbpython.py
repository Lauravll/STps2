import pymysql
#CONEXION DE LA BASE DE DATOS ------------
db = pymysql.connect(user="root",
    passwd="root",
    host="127.0.0.1",
    port=3306,
    db="dbpython")
print(db)
import pymysql
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
version = cursor.fetchone()
print(version)
