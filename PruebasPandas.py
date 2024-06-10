import pandas as pd

def crear_dataframe():
    d = {
        "nombre": ["Juan","Maria","Tania","Pedro"],
        "edad": [20,21,19,25],
        "carrera":["C","IN","C","IN"]
    }

    df = pd.DataFrame(d)
    return df


def crear_dataframe2(datos:dict):
    df = pd.DataFrame(datos)
    return df

if __name__ == "__main__":
    # Crear el primer DataFrame usando la primera función
    df1 = crear_dataframe()
    print(df1)
    print("======================================================")
    # Crear un diccionario para pasar a la segunda función
    datos = {
        "nombre": ["Ana", "Luis", "Carlos", "Marta"],
        "edad": [23, 30, 25, 22],
        "ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla"]
    }

    # Crear el segundo DataFrame usando la segunda función
    df2 = crear_dataframe2(datos)
    print(df2)
