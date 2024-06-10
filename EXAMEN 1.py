def contar_palabras_unicas():
    palabras = oracion.split()
    palabras_unicas = set(palabras)
    return {
        'cantidad': len(palabras_unicas),
        'palabras_unicas': sorted(palabras_unicas)
    }
oracion = "hola pedro hola juan"
resultado = contar_palabras_unicas()
print(resultado)

if __name__== "__main__":
    contar_palabras_unicas()