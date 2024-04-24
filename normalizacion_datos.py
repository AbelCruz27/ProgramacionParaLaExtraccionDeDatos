import pandas as pd

# z-score = (Xi - promedio)/std
def z_score(data:pd.DataFrame):
    prom_salario = data.salario.mean()
    std_salario = data.salario.std()
    data["zscore_salario"] = (data.salario - prom_salario) / std_salario

    prom_edad = data.edad.mean()
    std_edad = data.edad.std()
    data["zscore_edad"] = (data.edad - prom_edad) / std_edad

def escalado_simple(data:pd.DataFrame):
    max_salario = data.salario.max()
    max_edad = data.edad.max()
    data["es salario"] = data.salario / max_salario
    data["es edad"] = data.edad / max_edad

if __name__ == "__main__":
    personas = {"salario":[25000, 7000, 50000, 28000],
                "edad": [23, 19, 30, 28]}
    data = pd.DataFrame(personas)
    z_score(data)
    escalado_simple(data)
    print(data)