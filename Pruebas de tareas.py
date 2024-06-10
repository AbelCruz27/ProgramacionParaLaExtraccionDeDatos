import pandas as pd

def unir_archivos_csv2(archivo1, archivo2, archivo_salida):
    df1 = pd.read_csv(archivo1)
    df2 = pd.read_csv(archivo2)

    # Agregar la información adicional de df2 a las columnas correspondientes de df1
    df_final = pd.concat([df1, df2], axis=1)

    # Guardar el DataFrame resultante en un nuevo archivo CSV
    df_final.to_csv(archivo_salida)

    return df_final

if __name__ == "__main__":
    archivo1 = "Datasets/EmpleadosFinal.csv"
    archivo2 = "Datasets/Informacionextra.csv"
    archivo_salida = "Datasets/EmpleadosCompleto.csv"

    unir_archivos_csv2(archivo1, archivo2, archivo_salida)










