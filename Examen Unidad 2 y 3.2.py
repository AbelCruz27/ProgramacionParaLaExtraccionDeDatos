import pandas as pd

def Generar_Dataframe():
    df = pd.read_csv("Datasets/bank-loans.csv")
    print(df)

def Generar_Dataframe2():
    df = pd.read_csv("Datasets/bank-loans.csv")

    Multpilos10= df.iloc[::10]
    print(Multpilos10)

def clientes_por_edad(edad_minima, edad_maxima):
    df = pd.read_csv("Datasets/bank-loans.csv")

    df_filtrado = df[(df['age'] >= edad_minima) & (df['age'] <= edad_maxima)]
    print(df_filtrado)

def clientes_edad_meses():
  df = pd.read_csv("Datasets/bank-loans.csv")

  df['Edad_Meses'] = df['age'] * 12
  print(df)


def frecuencias_de_trabajos():
    df = pd.read_csv("Datasets/bank-loans.csv")

    frecuencias_oficios = df['job'].value_counts()
    print(frecuencias_oficios)

def promedio_de_edades_por_educacion():
    df = pd.read_csv("Datasets/bank-loans.csv")
    edades_medias = df.groupby('education')['age'].mean()
    print(edades_medias)

def porcentaje_de_hipotecas_por_estado_civil():
    df = pd.read_csv("Datasets/bank-loans.csv")
    total_por_estado_civil = df['marital'].value_counts()
    con_hipoteca_por_estado_civil = df[df['housing'] == 'yes']['marital'].value_counts()
    porcentaje_hipoteca_por_estado_civil = (con_hipoteca_por_estado_civil / total_por_estado_civil) * 100
    print(porcentaje_hipoteca_por_estado_civil)

def porcentaje_de_valores_unknown():
    df = pd.read_csv("Datasets/bank-loans.csv")
    unknown_percentajes = (df == 'unknown').mean().sort_values(ascending=False) * 100
    print(unknown_percentajes)

if __name__ == "__main__":
    Generar_Dataframe()
    print("=========================================================")
    Generar_Dataframe2()
    print("=========================================================")
    # PRango de edades
    edad_minima = 29
    edad_maxima = 33
    clientes_por_edad(edad_minima, edad_maxima)
    print("=========================================================")
    clientes_edad_meses()
    print("=========================================================")
    frecuencias_de_trabajos()
    print("=========================================================")
    promedio_de_edades_por_educacion()
    print("=========================================================")
    porcentaje_de_hipotecas_por_estado_civil()
    print("=========================================================")
    porcentaje_de_valores_unknown()