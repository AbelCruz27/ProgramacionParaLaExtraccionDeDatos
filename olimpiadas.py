import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def olimpiadas_extraer():
    driver = ChromeDriverManager()
    s = Service(driver.install())
    opc = Options()
    opc.add_argument("--window-size=1000,1200")
    navegador = webdriver.Chrome(service=s, options=opc)
    navegador.get("https://www.olympedia.org/statistics/medal/country")

    cmbYear = navegador.find_element(By.NAME, "edition_id")
    cmbGender = navegador.find_element(By.NAME, "athlete_gender")

    gender_options = cmbGender.find_elements(By.TAG_NAME, "option")
    yearsGroups = cmbYear.find_elements(By.TAG_NAME, "optgroup")
    year_List = yearsGroups[0].find_elements(By.TAG_NAME, "option")

    datos = {
        "country":[],
        "gender":[],
        "year":[],
        "gold":[],
        "silver":[],
        "bronze":[],
        "total":[]
    }

    for gender in gender_options[1:2]:
        gender.click()
        for year in year_List[-1:-6:-1]:
            year.click()
            time.sleep(2)
            soup = BeautifulSoup(navegador.page_source, "html5lib")
            tabla = soup.find("table", attrs={"class":"table table-striped"})
            list_rows = tabla.findAll("tr")
            for row in list_rows[1:]:
                valores = row.findAll("td")
                datos["country"].append(valores[0].text)
                datos["gender"].append(gender.text)
                datos["year"].append(year.text)
                datos["gold"].append(valores[2].text)
                datos["silver"].append(valores[3].text)
                datos["bronze"].append(valores[4].text)
                datos["total"].append(valores[5].text)

    df = pd.DataFrame(datos)
    df.to_csv("Datasets/olimpiadas.csv")


    time.sleep(5)
    navegador.close()

if __name__ == "__main__":
    olimpiadas_extraer()

