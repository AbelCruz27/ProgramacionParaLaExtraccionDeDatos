import pandas as pd


def limpiar_datos(datos:pd.DataFrame):
    nulos = datos.isnull()
    # print(nulos.sum())
    #print(nulos.sum().sum())
    #print(len(nulos))
    #print(nulos.sum()/len(nulos))
    #suma_columnas = nulos.sum()
    #print(type(suma_columnas))

    #Eliminar columnas

    datos_eliminados = datos.drop(["Age","Cabin"], axis= "columns")
    #eliminar_nulos = datos.dropna(subset=["Age","Cabin"], axis= "index")
    #eliminar_nulos = datos.dropna(axis="columns",thresh=12)
    #print(eliminar_nulos.shape)

    #print(datos.shape)
    #print(datos_eliminados.shape)

    #Elimminar columnas version 2
    #datos.drop(["Age","Cabin"], axis= "columns", inplace=True)
    #print(datos.shape)

    #sustituir valores
    normal= datos.fillna("sin especificar")
    ffill = datos.ffill()
    bfill =  datos.bfill()
    mix = datos.ffill().bfill().fillna("sin especificar")
    print(mix.head())
if __name__ == "__main__":
    datos = pd.read_csv("Datasets/titanic.csv")
    limpiar_datos(datos)