# mysql-connector-python
# SQLAlchemy
from mysqllll.connector import connect, Error

def conectar():
    try:
        # database="test"
        dbConexion= connect(host="localhost:3306", user="root",
                            password="Royer123.")
        cursor = dbConexion.cursor()
        sql = "show databases;"
        cursor.execute(sql)
        lista_datos = cursor.fetchall()
        for item in lista_datos:
            print(item)
    except Error as e:
        print(e)


if __name__ == "__main__":
    conectar()
