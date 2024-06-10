import pandas as pd

def crearAlumno():
    d = {
        "nombre":["juan","maria","lisa","pedro"],
        "carrera":["LIN","LC","LIN","LC"],
        "semestre":[3,5,5,7],
        "promedio":[90,85,100,80]
    }
    df = pd.DataFrame(d)
    return df

def crear_df_carrera():
    carrera = {
        "carrera":["LIN","LC","LNI","LAE"],
        "creditos":[352,350,360,365]
    }
    return pd.DataFrame(carrera)


def establecer_indices(datos:pd.DataFrame):
    datos2 = datos.set_index(["carrera","semestre"], inplace=True)
    print(datos2)


def unir_DataFrames(df1:pd.DataFrame,df2:pd.DataFrame):
    union = pd.merge(df1,df2, on="carrera", how="right")
    return union