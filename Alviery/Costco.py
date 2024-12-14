import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la página de Costco México (puedes cambiarla a la que te interese)
url = 'https://www.costco.com.mx/electrodomesticos'

# Enviar una solicitud GET para obtener el contenido de la página
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar los contenedores de productos (asegúrate de ajustar el selector)
productos = soup.find_all('div', class_='product-tile')  # Ajustar según la estructura HTML

# Crear listas para almacenar la información
nombres = []
precios = []
links = []

# Iterar sobre cada producto
for producto in productos:
    # Extraer el nombre del producto
    nombre = producto.find('a', class_='product-title').get_text(strip=True)
    nombres.append(nombre)

    # Extraer el precio del producto
    precio = producto.find('span', class_='price').get_text(strip=True)
    precios.append(precio)

    # Extraer el enlace al producto
    link = producto.find('a', class_='product-title')['href']
    links.append(f'https://www.costco.com.mx{link}')

# Crear un DataFrame de Pandas para organizar los datos
df = pd.DataFrame({
    'Nombre': nombres,
    'Precio': precios,
    'Link': links
})

# Guardar en un archivo CSV
df.to_csv('productos_costco.csv', index=False)

print(df)
