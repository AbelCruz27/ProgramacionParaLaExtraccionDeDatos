import pandas as pd

def crear_dataframe():
    data = {
        'Departamento': ['Ventas', 'Ventas', 'HR', 'HR', 'IT', 'IT'],
        'Id': [1001, 1002, 2001, 2002, 3001, 3002],
        'Nombre': ['Juan', 'Ana', 'Luis', 'Maria', 'Pedro', 'Sofía'],
        'Edad': [30, 24, 29, 25, 32, 28],
        'Salario': [40000, 42000, 38000, 39000, 50000, 52000]
    }

    df = pd.DataFrame(data).set_index('Id')
    print(df)


def estadisticas_por_departamento(departamento):
    data = {
        'Departamento': ['Ventas', 'Ventas', 'HR', 'HR', 'IT', 'IT'],
        'Id': [1001, 1002, 2001, 2002, 3001, 3002],
        'Nombre': ['Juan', 'Ana', 'Luis', 'Maria', 'Pedro', 'Sofía'],
        'Edad': [30, 24, 29, 25, 32, 28],
        'Salario': [40000, 42000, 38000, 39000, 50000, 52000]
    }

    df = pd.DataFrame(data).set_index('Id')

    departamento_df = df[df['Departamento'] == departamento]

    # Calcular las estadísticas de edad y salario
    estadisticas = departamento_df[['Edad', 'Salario']].describe()#.describe hace todas las estadisticas, lo vimos en clase

    return estadisticas

def agregar_fecha_de_ingreso(df, lista_valores_ingreso):
    # Convertir la lista de valores de ingreso a un objeto datetime
    fecha_ingreso = pd.to_datetime(lista_valores_ingreso)

    df['Fecha_Ingreso'] = fecha_ingreso

    return df

def datos_entre_2_fechas(df, fecha_minima, fecha_maxima):
    data = {
        'Departamento': ['Ventas', 'Ventas', 'HR', 'HR', 'IT', 'IT'],
        'Id': ['2022-01-01', '2021-12-15', '2022-02-28', '2022-03-10', '2022-04-05', '2022-05-20'],
        'Nombre': ['Juan', 'Ana', 'Luis', 'Maria', 'Pedro', 'Sofía'],
        'Edad': [30, 24, 29, 25, 32, 28],
        'Salario': [40000, 42000, 38000, 39000, 50000, 52000]
    }
    df = pd.DataFrame(data)

    # Convertir la columna de fecha en índice y ordenar el índice
    df['Id'] = pd.to_datetime(df['Id'])
    df = df.set_index('Id').sort_index()

    # Seleccionar los datos entre las fechas mínima y máxima
    datos_entre_fechas = df.loc[fecha_minima:fecha_maxima]

    return datos_entre_fechas

def unir_archivos_csv(archivo1, archivo2, archivo3, archivo_salida):
    df1 = pd.read_csv(archivo1)
    df2 = pd.read_csv(archivo2)
    df3 = pd.read_csv(archivo3)

    # Concatenar los DataFrames
    df_final = pd.concat([df1, df2, df3])

    # Guardar el DataFrame resultante en un nuevo archivo CSV
    df_final.to_csv(archivo_salida)

    return df_final

def unir_archivos_csv2(archivo1, archivo2, archivo_salida):
    df1 = pd.read_csv(archivo1)
    df2 = pd.read_csv(archivo2)

    # Agregar la información adicional de df2 a las columnas correspondientes de df1
    df_final = pd.concat([df1, df2], axis=1)

    # Guardar el DataFrame resultante en un nuevo archivo CSV
    df_final.to_csv(archivo_salida)

    return df_final
if __name__ == "__main__":
    crear_dataframe()
    print("==========================================================")
    estadisticas_ventas = estadisticas_por_departamento('Ventas')
    print(estadisticas_ventas)
    print("============================================================")
    data = {
        'Departamento': ['Ventas', 'Ventas', 'HR', 'HR', 'IT', 'IT'],
        'Id': [1001, 1002, 2001, 2002, 3001, 3002],
        'Nombre': ['Juan', 'Ana', 'Luis', 'Maria', 'Pedro', 'Sofía'],
        'Edad': [30, 24, 29, 25, 32, 28],
        'Salario': [40000, 42000, 38000, 39000, 50000, 52000]
    }
    df = pd.DataFrame(data).set_index('Id')

    valores_ingreso = ['2024-01-01', '2024-01-15', '2024-02-28', '2024-03-10', '2024-04-05', '2024-05-10']

    # Llamar a la función para insertar la columna de fecha de ingreso
    df_con_fecha_ingreso = agregar_fecha_de_ingreso(df, valores_ingreso)
    print(df_con_fecha_ingreso)
    print("=================================================================")
    # Valores de fecha de ingreso
    fecha_minima = '2021-01-01'
    fecha_maxima = '2021-12-31'
    # Llamar a la función para obtener los datos entre la fecha mínima y máxima
    datos_entre_fechas = datos_entre_2_fechas(None, fecha_minima, fecha_maxima)
    print(datos_entre_fechas)
    print("=================================================================")
    archivo1 = "Datasets/Empleados1.csv"
    archivo2 = "Datasets/Empleados2.csv"
    archivo3 = "Datasets/Empleados3.csv"
    archivo_salida = "Datasets/EmpleadosFinal.csv"

    unir_archivos_csv(archivo1, archivo2, archivo3, archivo_salida)
    print("======================================================================")
    archivo1 = "Datasets/EmpleadosFinal.csv"
    archivo2 = "Datasets/Informacionextra.csv"
    archivo_salida = "Datasets/EmpleadosCompleto.csv"

    unir_archivos_csv2(archivo1, archivo2, archivo_salida)






