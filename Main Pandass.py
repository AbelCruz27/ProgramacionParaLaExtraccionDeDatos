import PruebasPandas as pp

#TODO: DESPUES LO HAGO

if __name__ == "__main__":
    df = pp.crear_dataframe()
    print(df)

    d2 = {
        "nombre": ["Juan", "Maria", "Tania", "Pedro"],
        "Promedio": [100, 90, 80, 70],
        "carrera": ["C", "IN", "C", "IN"]
    }

    df2 = pp.crear_dataframe2(d2)
    print(df2)
    print("=====================")
    print(df2.shape)
    print(df2.size)
    print(df2.columns)
    print(df2.index)
    print(df2.dtypes)
