import cloudscraper
import requests
import time
from bs4 import BeautifulSoup as soup, element
import pandas as pd
import numpy as np

zonaprop_titulo = []
zonaprop_ubicacion = []
zonaprop_precio = []
zonaprop_divisa = []
zonaprop_superficie = []
zonaprop_ambientes = []
zonaprop_dormitorios = []
zonaprop_baños = []
columnas = ['Titulo Publicacion', 'Ubicacion', 'Precio', 'Divisa', 'Superficie(M2)', 'Ambientes', 'Dormitorios', 'Baños']

paginas = [i for i in range(4)]
paginas.remove(1)
# print(paginas)

for i in paginas:
    if i == 0:
        scraper = cloudscraper.create_scraper(
            browser={
                'browser': 'firefox',
                'platform': 'windows',
                'mobile': False
            }
        )

        url = "https://www.zonaprop.com.ar/inmuebles-alquiler-posadas.html"
        response = scraper.get(url)

        sopa = soup(response.text, features='lxml')

        propiedades = sopa.find(id="react-posting-cards")
        lista_propiedades = propiedades.find_all('div', class_="postingCardContent")

        for propiedad in lista_propiedades:
            titulo_propiedad = propiedad.find('a', {'class' : 'go-to-posting'})
            if titulo_propiedad != None:
                titulo_propiedad = titulo_propiedad.text.upper()
            else:
                titulo_propiedad = propiedad.find('div', {'class' : 'mosaicTitle'}).text
            titulo_propiedad = titulo_propiedad.replace('\n','').upper()
            zonaprop_titulo.append(titulo_propiedad)
        
            ubicacion = propiedad.find('span', {'class' : ' postingCardLocationTitle '})
            if ubicacion != None:
                ubicacion = ubicacion.text.upper()
            else:
                ubicacion = propiedad.find('span', {'data-qa' : 'direccion'}).text.upper()
            ubicacion = ubicacion.replace('\n','')
            zonaprop_ubicacion.append(ubicacion)

            precio = propiedad.find('div', {'data-qa' : 'precio'}).text
            precio = precio.replace('\n','').strip()
            divisa = precio.split()[0]
            numero = precio.split()[1]
            numero = numero.split('+')[0]
            zonaprop_precio.append(numero)
            zonaprop_divisa.append(divisa)

            caracts = propiedad.find('ul', {'class' : 'postingCardMainFeatures'})
            caracts = caracts.text.replace('\n','').strip().replace(' ', '')

            try:    
                if 'm²' in caracts:
                    superficie = caracts.split('m²')[0]
                else:
                    superficie = 'No informa'
                zonaprop_superficie.append(superficie)
            except:
                zonaprop_superficie.append('No se pudo leer')

            try:
                if 'amb.' in caracts:
                    ambientes = caracts.split('m²')[1].split('amb')[0]
                elif 'ambientes' in caracts:
                    ambientes = caracts.split('m²')[1].split('ambientes')[0]
                else:
                    ambientes = 'No informa'
                zonaprop_ambientes.append(ambientes)
            except:
                zonaprop_ambientes.append('No se pudo leer')
            
            try:
                if 'dorm.' in caracts:
                    dormitorios = caracts.split('dorm')[0]
                    dormitorios = dormitorios[-1]
                else:
                    dormitorios = 'No informa'
                zonaprop_dormitorios.append(dormitorios)
            except:
                zonaprop_dormitorios.append('No se pudo leer')

            try:
                if 'baño' in caracts:
                    baños = caracts.split('baño')[0]
                    baños = baños[-1]
                elif 'baños' in caracts:
                    baños = caracts.split('baños')[0]
                    baños = baños[-1]
                else:
                    baños = 'No informa'
                zonaprop_baños.append(baños)
            except:
                zonaprop_baños.append('No se pudo leer')
    else:
        scraper = cloudscraper.create_scraper(
            browser={
                'browser': 'firefox',
                'platform': 'windows',
                'mobile': False
            }
        )

        # url = "https://www.zonaprop.com.ar/'inmuebles-posadas-pagina-" + str(pag) + ".html"
        url = 'https://www.zonaprop.com.ar/inmuebles-alquiler-posadas-pagina-' + str(i) + '.html'
        response = scraper.get(url)

        sopa = soup(response.text, features='html.parser')

        propiedades = sopa.find(id="react-posting-cards")
        lista_propiedades = propiedades.find_all('div', class_="postingCardContent")

        for propiedad in lista_propiedades:
            titulo_propiedad = propiedad.find('a', {'class' : 'go-to-posting'})
            if titulo_propiedad != None:
                titulo_propiedad = titulo_propiedad.text.upper()
            else:
                titulo_propiedad = propiedad.find('div', {'class' : 'mosaicTitle'}).text
            titulo_propiedad = titulo_propiedad.replace('\n','').upper()
            zonaprop_titulo.append(titulo_propiedad)

            ubicacion = propiedad.find('span', {'class' : 'postingCardLocationTitle'})
            if ubicacion != None:
                ubicacion = ubicacion.text.upper()
            else:
                ubicacion = propiedad.find('span', {'data-qa' : 'direccion'}).text.upper()
            ubicacion = ubicacion.replace('\n','')
            zonaprop_ubicacion.append(ubicacion)

            precio = propiedad.find('div', {'data-qa' : 'precio'}).text
            precio = precio.replace('\n','').strip()
            divisa = precio.split()[0]
            numero = precio.split()[1]
            numero = numero.split('+')[0]
            zonaprop_precio.append(numero)
            zonaprop_divisa.append(divisa)

            caracts = propiedad.find('ul', {'class' : 'postingCardMainFeatures'})
            caracts = caracts.text.replace('\n','').strip().replace(' ', '')

            try:    
                if 'm²' in caracts:
                    superficie = caracts.split('m²')[0]
                else:
                    superficie = 'No informa'
                zonaprop_superficie.append(superficie)
            except:
                zonaprop_superficie.append('No se pudo leer')

            try:
                if 'amb.' in caracts:
                    ambientes = caracts.split('m²')[1].split('amb')[0]
                elif 'ambientes' in caracts:
                    ambientes = caracts.split('m²')[1].split('ambientes')[0]
                else:
                    ambientes = 'No informa'
                zonaprop_ambientes.append(ambientes)
            except:
                zonaprop_ambientes.append('No se pudo leer')
            
            try:
                if 'dorm.' in caracts:
                    dormitorios = caracts.split('dorm')[0]
                    dormitorios = dormitorios[-1]
                else:
                    dormitorios = 'No informa'
                zonaprop_dormitorios.append(dormitorios)
            except:
                zonaprop_dormitorios.append('No se pudo leer')

            try:
                if 'baño' in caracts:
                    baños = caracts.split('baño')[0]
                    baños = baños[-1]
                elif 'baños' in caracts:
                    baños = caracts.split('baños')[0]
                    baños = baños[-1]
                else:
                    baños = 'No informa'
                zonaprop_baños.append(baños)
            except:
                zonaprop_baños.append('No se pudo leer')

zonaprop_precio = pd.DataFrame(zonaprop_precio)
zonaprop_divisa = pd.DataFrame(zonaprop_divisa)
zonaprop_titulo = pd.DataFrame(zonaprop_titulo)
zonaprop_ubicacion = pd.DataFrame(zonaprop_ubicacion)
zonaprop_superficie = pd.DataFrame(zonaprop_superficie)
zonaprop_ambientes = pd.DataFrame(zonaprop_ambientes)
zonaprop_dormitorios = pd.DataFrame(zonaprop_dormitorios)
zonaprop_baños = pd.DataFrame(zonaprop_baños)

scrapeado = pd.concat([zonaprop_titulo, zonaprop_ubicacion, zonaprop_precio, zonaprop_divisa, zonaprop_superficie, 
                       zonaprop_ambientes, zonaprop_dormitorios, zonaprop_baños], axis=1)
scrapeado.columns = columnas
scrapeado.to_excel('zonaprop_alquileres.xlsx')
