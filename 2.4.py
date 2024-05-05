import pandas as pd

def normalizar(df, columnas):

    df_normalizado = df.copy()
    for columna in columnas:
        valor_min = df[columna].min()
        valor_max = df[columna].max()
        df_normalizado[columna] = (df[columna] - valor_min) / (valor_max - valor_min)
    return df_normalizado

data = {'columna1': [10, 22, 31, 45, 51],
        'columna2': [12, 27, 32, 44, 56]}
df = pd.DataFrame(data)

df_normalizado = normalizar(df, ['columna1', 'columna2'])
print(df_normalizado)

print("==================================")
def normalizar_zscore(data: pd.DataFrame, columnas_normalizar: list) -> pd.DataFrame:

  for columna in columnas_normalizar:

    media = data[columna].mean()
    desviacion_estandar = data[columna].std()

    data[f"zscore_{columna}"] = (data[columna] - media) / desviacion_estandar

  return data

data = pd.DataFrame({
  "salario": [25000, 7000, 50000, 28000],
  "edad": [23, 19, 30, 28],
  "altura": [1.70, 1.65, 1.80, 1.72]
})

columnas_normalizar = ["salario", "edad"]
data_normalizada = normalizar_zscore(data.copy(), columnas_normalizar)

print(data_normalizada)

print("=======================================")

def escalado_simple(df, columnas_a_normalizar):

    for columna in columnas_a_normalizar:
        valor_min = df[columna].min()
        valor_max = df[columna].max()
        df[columna] = (df[columna] - valor_min) / (valor_max - valor_min)
    return df

datos = {
    'A': [10, 21, 34, 49, 50],
    'B': [15, 22, 36, 42, 51],
    'C': [11, 15, 84, 65, 25]
}
df = pd.DataFrame(datos)

columnas_a_normalizar = ['A', 'C']

df_normalizado = escalado_simple(df, columnas_a_normalizar)
print(df_normalizado)

if __name__ == "__main__":
  normalizar()
  normalizar_zscore()
  escalado_simple()
