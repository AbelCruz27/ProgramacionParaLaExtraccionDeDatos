import pandas as pd

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

obtener_estadisticas()