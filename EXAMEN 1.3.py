import pandas as pd
def exploracion(archivo, n):
    df = pd.read_csv(archivo)

    # imprimir las primeras n filas
    print("primeras n filas")
    print(df.head(n))
    print("==============================")
    # imprimir las últimas n filas
    print("imprimir las ultimas n filas")
    print(df.tail(n))
    print("==============================")
    # imprimir n filas aleatorias
    print("filas aleatorias")
    print(df.sample(n))
    print("==============================")
    # imprimir la información estadística
    print("información estadística")
    print(df.describe())
    print("==============================")
    # imprimir la información del dataframe
    print("información del dataFrame")
    print(df.info())

    # Retornar el DataFrame
    return df


if __name__ == "__main__":
    exploracion("Datasets/olimpiadas.csv",3)