from mysql.connector import connect, Error
import pandas as pd
def conectar():
    try:
        db_conexion = connect(host="localhost", user="root",password="quesadillas1",database="ventacoches")

        cursor = db_conexion.cursor()
        Creartabla= "CREATE TABLE IF NOT EXISTS ventas (id INT AUTO_INCREMENT PRIMARY KEY, Marca VARCHAR(50),Modelo VARCHAR(100), Tipo VARCHAR(50),Potencia INT,Precio DECIMAL(10, 2));"
        InsertarRegistros = "INSERT INTO Ventas (fecha, modelo, precio, cantidad) VALUES (%s, %s, %s, %s)" #Los %s se utilizan como marcadores de posición en la consulta SQL.
        # Leer el archivo CSV
        data = pd.read_csv("Datasets/coches.csv")
        cursor.execute(Creartabla, InsertarRegistros)
        # Insertar datos en la tabla Ventas
        for row in data.iterrows():
            cursor.execute(InsertarRegistros, (row['Marca'], row['Modelo'], row['Tipo'], row['Potencia'], row['Precio']))
        lista_datos = cursor.fetchall()
        for item in lista_datos:
            print(item)

    except Error as e:
        print(e)

print("===================================================")

def autos_vendidos(Marca=None):
    try:
        conexion = connect(host="localhost", user="root",password="quesadillas1",database="ventacoches")

    query = "SELECT * FROM ventas"

    df = pd.read_sql_query(query, conexion)

    if Marca is not None:
        df = df[df['Marca'] == Marca]


    resultado = df.groupby('Marca').agg({'Precio': 'sum', 'Modelo': 'count'})

    resultado.columns = ['Ganancia_Total', 'Autos_Vendidos']

    return resultado

except Error as e:
print(e)

print("===================================================")

def carros_con_mayor_precio(cantidad_carros, mysql):

  # Conexión a la Base de Datos
  conexion = mysql.connector.connect(host="localhost", user="root", password="quesadillas1", database="ventacoches")
  cursor = conexion.cursor()

  # Validación de la cantidad de carros
  if cantidad_carros <= 0:
    print("Ingresa un numero valido")

if __name__ == "__main__":
    conectar()
