import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def login_facebook():
    driver = ChromeDriverManager()
    s = Service(driver.install())
    opc = Options()
    opc.add_argument("--window-size=1500,1200")
    navegador = webdriver.Chrome(service=s, options=opc)
    navegador.get("https://www.facebook.com")
    time.sleep(80)
    txtEmail = navegador.find_element(By.NAME, "email")
    txtPass = navegador.find_element(By.NAME, "pass")
    btnLogin  = navegador.find_element(By.NAME, "Login")
    time.sleep(50)
    txtEmail.send_keys("correo@gmail.com")
    time.sleep(7)
    txtPass.send_keys("Contraseña")
    time.sleep(9)
    btnLogin.click()
    navegador.save_screenshot("imagenes/test.png")
    time.sleep(60)
    navegador.close()

if __name__ == "__main__":
    login_facebook()