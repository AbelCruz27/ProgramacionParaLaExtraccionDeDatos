import pandas as pd
import indexacion_datos as id


if __name__ == "__main__":
    datos= id.crearDataFrame()
    carrera = id.crear_df_carrera()
    #id.establecer_indices(datos)
    #print("====================================")
    #print(datos)
    #print("====================================")
    #datos_filtrados = datos.loc["LIN"]
    #print(datos_filtrados.promedio.mean())
    #print("====================================")
    #filtrados = datos.iloc[0:2]
    #print(filtrados)
    df_all = id.unir_DataFrames(datos,carrera)
    print(df_all)
