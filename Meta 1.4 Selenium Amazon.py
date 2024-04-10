import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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

    for i in range(cantidad_paginas):
        nombre_captura = f"captura{i}.png"
        navegador.save_screenshot(f"imagenes/{nombre_captura}")
        time.sleep(3)
        boton_siguiente = navegador.find_element(By.LINK_TEXT, "Siguiente")
        boton_siguiente.click()
        time.sleep(3)


if __name__ == "__main__":
    buscar_producto_amazon("zapatillas depotivas" ,5)

