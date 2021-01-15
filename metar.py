import requests
from bs4 import BeautifulSoup
from datetime import datetime

now = datetime.now()


def metar(icao):
    page_url = 'https://www.aviationweather.gov/metar/data?ids='+icao+'&format=raw&date=&hours=0'
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    wynik = soup.find('code')
    print(now.strftime("%d/%m/%Y, %H:%M"),"METAR dla",wynik.text)

x = "y"
while x == "y":
    icao = input('Podaj kod ICAO: ')
    metar(icao)
    x = input("Następny? y/n: ")
