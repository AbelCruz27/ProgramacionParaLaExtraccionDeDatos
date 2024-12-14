habitaciones_disponibles = {1,2,3,4,5,6,7,8 ,9,10}
habitaciones_reservadas = set()

def mostrar_habitaciones_disponibles():
    print(f"habitaciones disponibles: {habitaciones_disponibles}")

def mostrar_habitaciones_reservadas():
    print(f"habitaciones reservadas: {habitaciones_reservadas}")

def reservar_habitacion(numero_habitacion):
    if numero_habitacion in habitaciones_disponibles:
        habitaciones_disponibles.remove(numero_habitacion)
        habitaciones_reservadas.add(numero_habitacion)
        print(f"habitación {numero_habitacion} esta reservada")
    else:
        print(f"habitación {numero_habitacion} no esta reservada")

def liberar_habitacion(numero_habitacion):
    if numero_habitacion in habitaciones_reservadas:
        habitaciones_reservadas.remove(numero_habitacion)
        habitaciones_disponibles.add(numero_habitacion)
        print(f"habitación {numero_habitacion} esta disponible")
    else:
        print(f"habitación {numero_habitacion} no esta disponible")

def invertir_alfabeto():
  alfabeto = "qwertyuiopasdfghjklzxcvbnm7894561230.@#$%^&*(),/*-+"
  clave = alfabeto[::-1]#esta parte invierte el alfabeto
  return clave

def encriptar_mensaje(mensaje):
  clave = invertir_alfabeto()
  alfabeto = "qwertyuiopasdfghjklzxcvbnm7894561230.@#$%^&*(),/*-+"
  diccionario_encriptacion = dict(zip(alfabeto, clave))

  mensaje_encriptado = ""
  for letra in mensaje:
    if letra in diccionario_encriptacion:
      mensaje_encriptado += diccionario_encriptacion[letra]
    else:
      mensaje_encriptado += letra

  return mensaje_encriptado, clave

def desencriptar_mensaje(mensaje_encriptado, clave):
  alfabeto = "qwertyuiopasdfghjklzxcvbnm7894561230.@#$%^&*(),/*-+"
  diccionario_encriptacion = dict(zip(clave, alfabeto))

  mensaje_desencriptado = ""
  for letra in mensaje_encriptado:
    if letra in diccionario_encriptacion:
      mensaje_desencriptado += diccionario_encriptacion[letra]
    else:
      mensaje_desencriptado += letra

  return mensaje_desencriptado

inventario={}
def agregar_producto(codigo, nombre, precio, cantidad):
    if codigo not in inventario:
        inventario[codigo] = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
        print("producto agregado con exito")
    else:
        print("ya existe un producto con ese código")

def editar_producto(codigo, nombre=None, precio=None, cantidad=None):
    if codigo in inventario:
        if nombre:
            inventario[codigo]['nombre'] = nombre
        if precio:
            inventario[codigo]['precio'] = precio
        if cantidad:
            inventario[codigo]['cantidad'] = cantidad
        print("product editado con éxito")
    else:
        print("no se encontro ningún producto con ese codigo")

def eliminar_producto(codigo):
    if codigo in inventario:
        del inventario[codigo]
        print("producto eliminado")
    else:
        print("no se encontro ningún producto con ese codigo")

def realizar_venta(codigo, cantidad):
    if codigo in inventario:
        if inventario[codigo]['cantidad'] >= cantidad:
            inventario[codigo]['cantidad'] -= cantidad
            print("venta realizada con exito")
        else:
            print("no hay suficiente inventario para realizar la venta")
    else:
        print("no se encontro ningun producto con ese codigo.")

def imprimir_inventario():
    print("nventario de productos:")
    for codigo, producto in inventario.items():
        print(f"codigo: {codigo}, nombre: {producto['nombre']}, precio: {producto['precio']}, cantidad: {producto['cantidad']}")

if __name__ == "__main__":
    mostrar_habitaciones_disponibles()
    mostrar_habitaciones_reservadas()
    #reservar habitación 102
    reservar_habitacion(2)
    mostrar_habitaciones_disponibles()
    mostrar_habitaciones_reservadas()
    #intentar reservar la misma habitación
    reservar_habitacion(2)
    #liberar la habitación 102
    liberar_habitacion(2)
    mostrar_habitaciones_disponibles()
    mostrar_habitaciones_reservadas()
    #intentar liberar una habitación no reservada
    liberar_habitacion(9)
    print("=================================================")
    #mensaje a encriptar
    mensaje = "dr.shine"
    mensaje_encriptado, clave = encriptar_mensaje(mensaje)
    #mensje encriptado
    print("Mensaje encriptado:", mensaje_encriptado)
    mensaje_desencriptado = desencriptar_mensaje(mensaje_encriptado, clave)
    #mensaje desencriptado
    print("Mensaje desencriptado:", mensaje_desencriptado)
    print("=================================================")
    #agregar productos
    print("productos agregados")
    agregar_producto('55', 'camisas', 400, 150)
    agregar_producto('555', 'corbatas', 150, 95)
    agregar_producto('222', 'pantalon', 800, 50)
    imprimir_inventario()
    #editar productos
    print("productos editados")
    editar_producto('555', nombre='corbatas', precio=80)
    imprimir_inventario()
    #ventas
    print("productos vendidos")
    realizar_venta('55', 2)
    imprimir_inventario()
    #eliminar producto
    print("productos eliminados")
    eliminar_producto('222')
    imprimir_inventario()
