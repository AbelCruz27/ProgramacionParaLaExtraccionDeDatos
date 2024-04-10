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