import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def crear_navegador(url):
    driver = ChromeDriverManager()
    s = Service(driver.install())
    opc = Options()
    opc.add_argument("--window-size=1500,1200")
    navegador = webdriver.Chrome(service=s, options=opc)
    navegador.get(url)
    return navegador

def extraer_peliculas(url):
    navegador = crear_navegador("https://www.rottentomatoes.com/browse/movies_in_theaters/")
    time.sleep(20)

    seleccionador = navegador.find_element("span", class_="filter-chip")
    seleccionador_opciones = navegador.find_element("span", class_= "label label--small upper")

    for seleccionador in seleccionador_opciones[1:2]:
        seleccionador.click()

