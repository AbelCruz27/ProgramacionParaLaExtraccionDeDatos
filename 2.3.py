import pandas as pd

def porcentaje_valores_nulos(df):

    porcentaje_nulos = (df.isnull().sum() / df.shape[0]) * 100
    porcentaje_nulos.rename(index={'True': '% Valores Nulos'}, inplace=True)
    return porcentaje_nulos

data = {'Columna1': [1, 2, 3, None, 5],
        'Columna2': ['a', 'b', None, 'd', 'e'],
        'Columna3': [True, False, True, None, None]}

df = pd.DataFrame(data)

porcentaje_nulos_df = porcentaje_valores_nulos(df)
print(porcentaje_nulos_df)

print("=========================================")

def contar_filas_duplicadas(df):

    return df.duplicated().sum()

data = {'Columna1': [1, 1, 3, 1, 5],
        'Columna2': ['a', 'a', None, 'd', 'e'],
        'Columna3': [True, True, True, None, None]}

df = pd.DataFrame(data)

numero_filas_duplicadas = contar_filas_duplicadas(df)
print(f"Número de filas duplicadas: {numero_filas_duplicadas}")

import pandas as pd

print("=========================================")

def eliminar_columnas_nulos_altos(df, porcentaje_nulo_maximo):

    if not (0 <= porcentaje_nulo_maximo <= 1):
        raise ValueError("El porcentaje máximo debe estar entre 0 y 1")

    porcentajes_nulos = (df.isnull().sum() / df.shape[0]) * 100

    columnas_a_eliminar = ["Columna3"]
    for columna, porcentaje_nulo in porcentajes_nulos.items():
        if porcentaje_nulo >= porcentaje_nulo_maximo:
            columnas_a_eliminar.append(columna)

    df.drop(columnas_a_eliminar, axis=1, inplace=True)
    return columnas_a_eliminar

data = {'Columna1': [1, None, 3, 1, 5],
        'Columna2': ['a', 'b', None, 'd', 'e'],
        'Columna3': [True, False, None, None, None],
        'Columna4': [5, 6, 7, 8, 9]}

df = pd.DataFrame(data)

porcentaje_nulo_maximo = 0.5  # 50%

columnas_eliminadas = eliminar_columnas_nulos_altos(df.copy(), porcentaje_nulo_maximo)
print(f"Columnas eliminadas: {columnas_eliminadas}")
print(df)

print("=========================================")

def rellenar_valores_nulos(dataframe, columnas, metodo):

  if metodo not in ['mean', 'bfill', 'ffill']:
    raise ValueError("El método especificado debe ser 'mean', 'bfill' o 'ffill'.")

  df_modificado = dataframe.copy()

  for columna in columnas:
    if metodo == 'mean':
      df_modificado[columna].fillna(df_modificado[columna].mean(), inplace=True)
    elif metodo == 'bfill':
      df_modificado[columna].fillna(method='bfill', inplace=True)
    elif metodo == 'ffill':
      df_modificado[columna].fillna(method='ffill', inplace=True)

  return df_modificado

data = {'A': [1, 2, None, 4, 5],
        'B': [None, 10, None, None, 50],
        'C': [100, None, None, None, 500]}
df = pd.DataFrame(data)

columnas = ['A', 'B', 'C']

metodo = 'mean'  # Puede ser 'mean', 'bfill' o 'ffill'

nuevo_df = rellenar_valores_nulos(df, columnas, metodo)
print("DataFrame original:")
print(df)
print("\nDataFrame modificado:")
print(nuevo_df)

print("=========================================")

def eliminar_renglones_repetidos(dataframe):

  cantidad_anterior = len(dataframe)

  dataframe.drop_duplicates(inplace=True)

  cantidad_actual = len(dataframe)

  renglones_eliminados = cantidad_anterior - cantidad_actual

  return renglones_eliminados

data = {'A': [1, 2, 3, 1, 2],
        'B': ['x', 'y', 'z', 'x', 'y']}
df = pd.DataFrame(data)

print("DataFrame original:")
print(df)

renglones_eliminados = eliminar_renglones_repetidos(df)
print("\nCantidad de renglones eliminados:", renglones_eliminados)
print("\nDataFrame después de eliminar renglones repetidos:")
print(df)

if __name__ == "__main__":
    porcentaje_valores_nulos(df)
    contar_filas_duplicadas(df)
    eliminar_columnas_nulos_altos(df, porcentaje_nulo_maximo)
    rellenar_valores_nulos(data, columnas, metodo)
    eliminar_renglones_repetidos()