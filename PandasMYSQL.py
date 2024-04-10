from sqlalchemy import create_engine
import pandas as pd

def insert_pandas():
    user="root"
    pasword="Royer123."
    name="programacion"
    server="localhost"
    cadena_conexion = f"mysql+mysqlconnector://{user}:{pasword}@{server}/{name}"
    engine=create_engine(cadena_conexion)
    conexion = engine.connect()
    query = "Select * from alumno where nombre like = %s;"
    nombre= input("Dame un nombre: ")
    parametros = (f"%{nombre}%",)
    resultado = pd.read_sql(query, conexion, params=parametros)
    print(resultado)

    datos = {
        "idalumno":[20, 21, 22],
        "nombre": ["Marcela","Alan","Itzel"],
        "carrera": ["Medicina","Medicina","Medicina"]

    }

    df = pd.DataFrame(datos)
    df.to_sql("alumno",conexion, if_exists="append", index=Falsealse)

if __name__=="__main__":
    insert_pandas()
