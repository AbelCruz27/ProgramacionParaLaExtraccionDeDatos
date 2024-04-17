import pandas as pd


def limpiar_datos(datos:pd.DataFrame):
    nulos = datos.isnull()
    # print(nulos.sum())
    #print(nulos.sum().sum())
    print(len(nulos))
    print(nulos.sum()/len(nulos))

if __name__ == "__main__":
    datos = pd.read_csv("Datasets/titanic.csv")
    limpiar_datos(datos)