import pandas as pd

def imprimir_df():
    datos = {
        "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
        "Ventas": [30500, 35600, 28300, 33900],
        "Gastos": [22000, 23400, 18100, 20700]
    }

    df = pd.DataFrame(datos)
    print(df)

def obtener_estadisticas():
    # Cargar los datos desde el archivo CSV
    df = pd.read_csv('Alviery/cotizacion.csv', sep=';',decimal=',',thousands='.')

    # Seleccionar las columnas de interés (a partir de la segunda)
    columnas_de_interes = ['Final', 'Máximo', 'Mínimo', 'Volumen', 'Efectivo']
    df_seleccionado = df[columnas_de_interes]

    # Calcular los estadísticos
    minimos = df_seleccionado.min()
    maximos = df_seleccionado.max()
    medias = df_seleccionado.mean()

    # Crear un DataFrame con los resultados
    resultados = pd.DataFrame({'Mínimo': minimos, 'Máximo': maximos, 'Media': medias})

    # Imprimir los resultados
    print(resultados)

def obtener_informacion():
    df = pd.read_csv("Datasets/titanic.csv")

    print("Informacion")
    print(df.info())
    print("10 primeras filas")
    print(df.head(10))
    print("ultimas 10 filas")
    print(df.tail(10))
    print("10 filas aleatorias")
    print(df.sample(10))


if __name__ == "__main__":
    imprimir_df()
    print("================================")
    obtener_estadisticas()
    print("================================")
    obtener_informacion()
