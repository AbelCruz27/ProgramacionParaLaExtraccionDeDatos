import pandas as pd

def limpiar_datos(datos:pd.DataFrame):
    nulos = datos.isnull()
    print(nulos.sum())
    print("======================")
    print(nulos.sum().sum())
    print("======================")
    print(len(nulos))
    print("======================")
    print(nulos.sum()/len(nulos))
    print("======================")
    suma_columnas = nulos.sum()
    print(type(suma_columnas))
    print("======================")

    #Eliminar columnas

    datos_eliminados = datos.drop(["Age","Cabin"], axis= "columns")
    eliminar_nulos = datos.dropna(subset=["Age","Cabin"], axis= "index")
    eliminar_nulos = datos.dropna(axis="columns",thresh=12)
    print(eliminar_nulos.shape)
    print("======================")

    #print(datos.shape)
    print(datos_eliminados.shape)
    print("======================")

    #Elimminar columnas version 2
    datos.drop(["Age","Cabin"], axis= "columns", inplace=True)
    print(datos.shape)
    print("======================")

    #sustituir valores
    normal= datos.fillna("sin especificar")
    ffill = datos.ffill()
    bfill =  datos.bfill()
    mix = datos.ffill().bfill().fillna("sin especificar")
    print(mix.head())
    print("======================")
if __name__ == "__main__":
    datos = pd.read_csv("Datasets/titanic.csv")
    limpiar_datos(datos)