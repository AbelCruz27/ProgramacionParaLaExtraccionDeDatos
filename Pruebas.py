import numpy as np

def pruebas():
    array= np.array([3,12,7,-1])
    print(array)
    print(type(array))
    rest=array * array
    print(rest)

    def pares(lista):
        array=np.array(lista)
        return array % 2 == 0

if __name__ == "__main__":
    pruebas()
    lista = [3,5,8,9,10]
    resultado = pares(lista)
    print(resultado)


















