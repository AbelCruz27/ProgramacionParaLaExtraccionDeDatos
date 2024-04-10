import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

def buscar_producto_amazon(producto, cantidad_paginas):
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

    datos = {}

    for i in range(cantidad_paginas):
        soup = BeautifulSoup(navegador.page_source, "html5lib")
        productos = soup.find_all("div", class_="a-section a-spacing-medium a-spacing-top-small")
        for producto in productos:
            nombre = producto.find("a", class_="a-size-base-plus a-color-base a-text-normal").text
            rating = producto.find("span", class_="star-rating").text
            precio = producto.find("span", class_="a-offscreen").text
            fecha_entrega = producto.find("span", class_="a-size-small a-color-secondary").text
            datos.append({
                "nombre": nombre,
                "rating": rating,
                "precio": precio,
                "fecha_entrega": fecha_entrega
            })
        boton_siguiente = navegador.find_element(By.LINK_TEXT, "Siguiente")
        boton_siguiente.click()
        time.sleep(2)

    df = pd.DataFrame(datos)
    df.to_csv("Datasets/productos_amazon2.csv")


if __name__ == "__main__":
    buscar_producto_amazon("zapatillas deportivas", 1)


