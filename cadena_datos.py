import pandas as pd


def transformar_datos(data:pd.DataFrame):
    data["nombre"] = data.nombre.str.strip()
    data["nom_may"] = data.nombre.str.upper()
    data["nom_min"] = data.nombre.str.lower()

    #METODOS DE FILTRO




if __name__ == "__main__":
    d= {
        "nombre": ["  Maria   ", "Juan   ", "   Fidel", " Maria    "],
        "genero": ["F", "M", "M", "F"],
        "escolaridad": ["Universidad", "Prepa", "Maestria", "Prepa"]
    }

    data = pd.DataFrame(d)
    transformar_datos(data)
    print(data)