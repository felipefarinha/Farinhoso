# Date and time structure
from datetime import datetime

date_and_time = datetime.now()
date_and_time_text = date_and_time.strftime('%d/%m/%Y | %H:%M')

# Import of libraries
from bs4 import BeautifulSoup
import requests
import csv



# Request structure
headers = {'Mozilla/5.0'}

url_base = 'https://lista.mercadolivre.com.br/'

product_name = input('Digite um produto para pesquisa de item')

response = requests.get(url_base + product_name, '_NoIndex_True')

website = BeautifulSoup(response.text, 'html.parser')



# Csv init
csv_file = open('raspagem_de_dados.csv', 'w', newline='')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['id', 'Data e hora da consulta', 'Título', 'Preço', 'Link'])



# Web Scrapping Initializing
products = website.findAll('div', attrs={'class': 'ui-search-result__wrapper'})



id = 0
for product in products:

    title = product.find('h2', attrs={'class': 'ui-search-item__title'}).get_text()

    price = product.find('span', attrs={'class': 'price-tag ui-search-price__part'}).get_text()

    link = product.find('a', attrs={'class': 'ui-search-link'})

    index = price.find('R$')


    #index_nums = print(index)
    formated_price = price[index:]


    print('\n Data e hora da consulta: {} \n Título do produto: {} \n Preço do produto: {} \n link do produto: {}'
          '\n'.format(date_and_time_text, title, formated_price, link['href']))
    csv_writer.writerow([id, date_and_time_text, title, formated_price, link['href']])
    id += 1
csv_file.close()













