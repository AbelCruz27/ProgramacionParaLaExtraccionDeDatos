import pandas as pd
import indexacion_datos as id

if __name__ == "__main__":
    alumnos = id.crearAlumno()
    print(alumnos)

    #Tecnica #1 Filtrado de datos
    c1 = alumnos.promedio > 85
    datos_filtrados = alumnos[c1]
    #print(Datos_filtrados)

    # and --- &, or -- |
    c2 = (alumnos.promedio > 90) | (alumnos.carrera == "LIN")
    datos_filtrados = alumnos[c2]
    #print(datos_filtrados)

    c3 = (alumnos.promedio > 80) & (alumnos.carrera.isin(["LIN","LC"]))
    datos_filtrados = alumnos[c3]
    #print(datos_filtrados[["nombre","promedio"]])

    #Tecanica 2 Busqueda por query
    #query es por condicion en cadena
    q1 = " carrera == 'LC' "
    q2 = " promedio > 80 and carrera == 'LC' "
    q3 = " promedio > 80 and carrera.isin (('LIN','LC'))"
    filtrado_tecnica2 = alumnos.query(q3)
    print(filtrado_tecnica2)

