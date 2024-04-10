import pandas as pd
import numpy as np

datos = {
    "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
    "Ventas": [30500, 35600, 28300, 33900],
    "Gastos": [22000, 23400, 18100, 20700]
}

df = pd.DataFrame(datos)
print(df)

print("=================================================")

def obtener_estadisticas(archivo_csv):
    df = pd.read_csv(archivo_csv)

    estadisticas = {
        'Mínimo': df.min(),
        'Máximo': df.max(),
        'Media': df.mean()
    }

    df_estadisticas = pd.DataFrame(estadisticas)

    return df_estadisticas

estadisticas = obtener_estadisticas("Datasets/cotizacion.csv")

print(estadisticas)
print("=================================================")

df = pd.read_csv("Datasets/titanic.csv")

print("Informacion")
print(df.info())
print("10 primeras filas")
print(df.head(10))
print("ultimas 10 filas")
print(df.tail(10))
print("10 filas aleatorias")
print(df.sample(10))

#escribir una funcion que reciba como parametro una oracion(cadena), la funcion debe retornar un diccionario con la cantidad de palabras unicas y una lista con las palabras unicas en orden alafabetico