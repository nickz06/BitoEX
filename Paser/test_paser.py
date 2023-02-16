import urllib
import requests
import pandas as pd
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
 
url = "https://www.bitopro.com/ns/fees"

response = requests.get(url)

soup = BeautifulSoup(response.text)

tables=soup.find('table',attrs={ "style" : "border-collapse: collapse; width: 100%; min-width: 900px;" })
table_body=tables.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    print (cells)
