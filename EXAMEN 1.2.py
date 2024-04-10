def ventass(ventas):
    ventas_totales = 0
    ventas_maximas = 0
    ventas_minimas = 100000
    dia_maximo = ""
    dia_minimo = ""

    for dia, monto in ventas:
        ventas_totales += monto
        if monto > ventas_maximas:
            ventas_maximas = monto
            dia_maximo = dia

            if monto < ventas_minimas:
                ventas_minimas = monto
                dia_minimo = dia

    ventas_promedio = ventas_totales / len(ventas)
    return {
        "ventas_promedio": ventas_promedio,
        "dia_maximo": dia_maximo,
        "ventas_maximas": ventas_maximas,
        "dia_minimo": dia_minimo,
        "ventas_minimas": ventas_minimas
    }


if __name__ == "__main__":
    datos_ventas = [("lunes", 10), ("martes", 10), ("miércoles", 10), ("Jueves", 10), ("viernes", 10)]
    print(ventass(datos_ventas))

