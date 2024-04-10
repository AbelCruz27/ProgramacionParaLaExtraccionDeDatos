# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 17:21:08 2024

@author: alumnoFCA
"""

# veny abel melendres cruz
# grupo 952
# fecha 13/02/2024
# Duplicados. Desarrolle una función que dada una lista de números enteros,
# retorna True si al menos un valor aparece dos veces,
# y Falso si todos los elementos son distintos.

# True
def duplicados(nums):
  return len(set(nums)) != len(nums)

nums = [1, 2, 3, 1]
duplicados(nums)
resultado = duplicados(nums)
print(resultado)


# False
def duplicados2(nums2):
  return len(set(nums2)) != len(nums2)

nums2 = [1, 2, 3, 4]
duplicados2(nums2)
resultado2 = duplicados2(nums2)
print(resultado2)
print("------------------------------------------------------")

def busquedaSuma(numeros, target):
  num_dict = {}

  for i, numero in enumerate(numeros):
    complemento = target - numero
    if complemento in num_dict:
      return (num_dict[complemento], i)
    num_dict[numero] = i

  #En caso de no encontrar una solucion
  return None

#Ejemplos de uso
nums1 = [2, 7, 11, 15]
target1 = 9
print(busquedaSuma(nums1, target1))

nums2 = [3, 2, 4]
target2 = 6
print(busquedaSuma(nums2, target2))

print("------------------------------------------------------")
def detectar_cambios(estado_anterior, estado_actual):
  cambios = {}
  for i in estado_anterior:
    if i in estado_actual and estado_anterior[i] != estado_actual[i]:
      cambios[i] = estado_actual[i]
  return cambios


estado_anterior = {'a': 1, 'b': 2, 'c': 3}
estado_actual = {'a': 5, 'b': 5, 'c': 3,}

resultado = detectar_cambios(estado_anterior, estado_actual)
print(resultado)
print("------------------------------------------------------")
def generar_clave():
  alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
  clave = alfabeto[::-1]#Invertir el alfabeto
  return clave


def encriptar_mensaje(mensaje):
  clave = generar_clave()
  alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
  diccionario_encriptacion = dict(zip(alfabeto, clave))

  mensaje_encriptado = ""
  for letra in mensaje:
    if letra in diccionario_encriptacion:
      mensaje_encriptado += diccionario_encriptacion[letra]
    else:
      mensaje_encriptado += letra

  return mensaje_encriptado, clave


def desencriptar_mensaje(mensaje_encriptado, clave):
  alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
  diccionario_encriptacion = dict(zip(clave, alfabeto))#Invertir el diccionario de encriptación

  mensaje_desencriptado = ""
  for letra in mensaje_encriptado:
    if letra in diccionario_encriptacion:
      mensaje_desencriptado += diccionario_encriptacion[letra]
    else:
      mensaje_desencriptado += letra

  return mensaje_desencriptado


mensaje = "CU CU PUMAS"
mensaje_encriptado, clave = encriptar_mensaje(mensaje)
print("Mensaje encriptado:", mensaje_encriptado)
mensaje_desencriptado = desencriptar_mensaje(mensaje_encriptado, clave)
print("Mensaje desencriptado:", mensaje_desencriptado)
print("------------------------------------------------------")
inventario = {}

def agregar_producto(codigo, nombre, precio, cantidad):
    if codigo not in inventario:
        inventario[codigo] = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
        print("Producto agregado con éxito")
    else:
        print("Ya existe un producto con ese código")

def editar_producto(codigo, nombre=None, precio=None, cantidad=None):
    if codigo in inventario:
        if nombre:
            inventario[codigo]['nombre'] = nombre
        if precio:
            inventario[codigo]['precio'] = precio
        if cantidad:
            inventario[codigo]['cantidad'] = cantidad
        print("Producto editado con éxito")
    else:
        print("No se encontró ningún producto con ese código")

def eliminar_producto(codigo):
    if codigo in inventario:
        del inventario[codigo]
        print("Producto eliminado")
    else:
        print("No se encontró ningún producto con ese código")

def realizar_venta(codigo, cantidad):
    if codigo in inventario:
        if inventario[codigo]['cantidad'] >= cantidad:
            inventario[codigo]['cantidad'] -= cantidad
            print("Venta realizada con éxito.")
        else:
            print("No hay suficiente inventario para realizar la venta")
    else:
        print("No se encontró ningún producto con ese código.")

def imprimir_inventario():
    print("Inventario de Productos:")
    for codigo, producto in inventario.items():
        print(f"Código: {codigo}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

agregar_producto('19', 'Camiseta', 250, 90)
agregar_producto('22', 'Pantalón', 600, 45)

imprimir_inventario()

editar_producto('29', nombre='Sueter', precio=600)
imprimir_inventario()

realizar_venta('29', 5)
imprimir_inventario()

eliminar_producto('19')
imprimir_inventario()

