from bs4 import BeautifulSoup
import requests

url = "https://www.lanacion.com.ar/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
content_titles = soup.find_all('h2', "com-title")
print( ":::::::::::::::::::::::::::: TITULARES LA NACION :::::::::::::::::::::::::::::::::::")
for tit in content_titles:
    sub = tit.find_all('a')
print(sub[0].attrs.get('title'))
print("https://www.lanacion.com.ar/"+sub[0].attrs.get('href'))
print("")