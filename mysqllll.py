
from mysql.connector import connect, Error

def conectar():
    try:
        db_conexion = connect(host="localhost", user="root",password="Royer123.",database="programacion")

        cursor = db_conexion.cursor()
        sql = "show database;"
        cursor.execute(sql)
        lista_datos = cursor.fetchall()
        for item in lista_datos:
            print(item)


    except Error as e:
        print(e)

if __name__ == "__main__":
    conectar()