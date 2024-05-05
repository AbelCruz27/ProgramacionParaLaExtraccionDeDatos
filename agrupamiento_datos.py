import pandas as pd


def agrupar(data:pd.DataFrame):
    grupo_sexo = data.groupby(["Survived","Pclass","Sex"]).Sex.count()
    print(grupo_sexo)


if __name__ == "__main__":
    data = pd.read_csv("Datasets/titanic.csv")
    agrupar(data)