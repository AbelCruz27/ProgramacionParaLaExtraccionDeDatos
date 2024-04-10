import pandas as pd

def crearcsv(path, separador= ",", decimal= ".", miles= None):
    df = pd.read_csv(path, sep = separador, decimal = decimal, thousands = miles)
    return df


if __name__ =="__main__":
    df = crearcsv("../datasets/cotizacion.csv", ";", ",", ".")
    df_titanic = crearcsv("../datasets/titanic.csv")
    df_colesterol = crearcsv("https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesteroles.csv", ";",",")
    print(df.head(10))
    print("Columnas:", list(df.columns))
    print("========================================================================")
    print(df_titanic.head(10))
    print("========================================================================")
    print(df_colesterol)
    #print(df.Name)
    #print(df["Name"])
    #print(df[["Name","Age","Sex"]])

    #print(df.Survived.sum(numeric_only=True))
    #print(df.Survived.mean(numeric_only=True))
# https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesteroles.csv

