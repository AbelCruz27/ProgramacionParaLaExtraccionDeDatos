import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def boot_en_merado_libre(busqueda, cantidad):
    # Configurar el servicio de GeckoDriver
    service = Service(GeckoDriverManager().install())

    # Configurar opciones del navegador
    options = webdriver.FirefoxOptions()
    options.add_argument("--window-size=1000,1200")

    # Crear instancia del navegador
    driver = webdriver.Firefox(service=service, options=options)

    # Abrir Amazon
    driver.get("https://www.mercadolibre.com.mx/")

    # Esperar 10 segundos
    time.sleep(1)
    carga1 = driver.find_element(By.ID, "cb1-edit")
    time.sleep(1)
    carga1.send_keys(busqueda)
    time.sleep(1)
    boton1 = driver.find_element(By.CLASS_NAME,"nav-icon-search" )
    boton1.click()

    # Esperar a que se carguen los resultados
    time.sleep(1)

    data = {"nombre": [],"calificasion":[],"precios":[], "descuento":[]}

    for repeticion in range(cantidad):
        # Obtener el código fuente HTML de la página
        html = driver.page_source

        # Pasar el HTML a BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")

        # Encontrar todos los elementos que contienen los productos
        productos = soup.find_all('h2', class_='ui-search-item__title')
        calificasion=soup.findAll('span', class_='andes-visually-hidden')
        precio=soup.findAll('span', class_='andes-money-amount')
        descuentos=soup.findAll('span', class_='ui-search-price__discount')
        for producto, calificasiones, precios, descuento in zip(productos, calificasion, precio, descuentos):
            data["nombre"].append(producto.text)
            data["calificasion"].append(calificasiones.text)
            data["precios"].append(precios.text)
            data["descuento"].append(descuento.text)
            time.sleep(5)
            # Buscar el botón de "Siguiente" dentro del contenedor
        print("Esperando a que desaparezca el banner de cookies...")
        WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "div.cookie-consent-banner-opt-out")))
        print("Banner de cookies ha desaparecido.")

        try:
            boton_siguiente = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "andes-pagination__button--next"))
            )
            # Desplazar la página para que el botón "Siguiente" esté dentro del área visible
            driver.execute_script("arguments[0].scrollIntoView();", boton_siguiente)

            # Hacer clic en el botón "Siguiente"
            boton_siguiente.click()
        except:
            print("No se pudo hacer clic en el botón 'Siguiente'.")
            time.sleep(1)


    # Imprimir los nombres de los productos
    df = pd.DataFrame(data)
    print(df)
    df.to_csv("dataset/mercadolibre.csv")





if __name__ == "__main__":
    boot_en_merado_libre("nike mujer", 2)