import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv
from bs4 import BeautifulSoup

def buscar_producto_amazon(producto,cantidad_paginas):
    driver = ChromeDriverManager()
    s = Service(driver.install())
    opc = Options()
    opc.add_argument("--window-size=1500,1200")
    navegador = webdriver.Chrome(service=s, options=opc)
    navegador.get("https://www.amazon.com.mx/")
    time.sleep(20)
    buscador = navegador.find_element(By.ID, "twotabsearchtextbox")
    buscador.send_keys(producto)
    time.sleep(3)
    boton_buscar = navegador.find_element(By.ID, "nav-search-submit-button")
    boton_buscar.click()
    time.sleep(3)

    lista_productos = []

    for i in range(cantidad_paginas):
        # Diccionario para almacenar los datos del producto
        producto_info = {}

        # Extracción del nombre del producto
        nombre_producto = navegador.find_element(By.CSS_SELECTOR, "span.a-size-medium.a-color-base.product-title").text
        producto_info["nombre"] = nombre_producto

        # Extracción del precio del producto
        precio_producto = navegador.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
        producto_info["precio"] = precio_producto

        # Extracción de la fecha de entrega
        fecha_entrega = navegador.find_element(By.CSS_SELECTOR, "span.a-expedited-shipping-slot").text
        producto_info["fecha_entrega"] = fecha_entrega

        # Extracción del rating del producto
        rating_producto = navegador.find_element(By.CSS_SELECTOR, "span.a-icon-alt").text
        producto_info["rating"] = rating_producto

        # Almacenamiento del diccionario en una lista
        lista_productos.append(producto_info)

        # Captura de pantalla (opcional)
        nombre_captura = f"captura{i}.png"
        navegador.save_screenshot(f"imagenes/{nombre_captura}")
        time.sleep(3)

        # Clic en el botón "Siguiente"
        boton_siguiente = navegador.find_element(By.LINK_TEXT, "Siguiente")
        boton_siguiente.click()
        time.sleep(3)


    # Creación del archivo CSV
    with open("productos.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # Encabezado del archivo
        writer.writerow(["Nombre", "Precio", "Fecha de entrega", "Rating"])
        # Escritura de los datos en el archivo
        for producto in lista_productos:
            writer.writerow([producto["nombre"], producto["precio"], producto["fecha_entrega"], producto["rating"]])

if __name__ == "__main__":
    buscar_producto_amazon("zapatillas depotivas", 1)
