from bs4 import BeautifulSoup
import requests

url = "https://dolarhoy.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")


valor = soup.find_all('div', class_='val')
precio_compra = valor[0].text
precio_venta = valor[1].text


print(":::::::::::::::DOLAR BLUE HOY::::::::::::::::::::")
print("Compra:"+(precio_compra))
print("")
print("Venta:"+(precio_venta))
print(":::::::::::::::::::::::::::::::::::::::::::::::::")
