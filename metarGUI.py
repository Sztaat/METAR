import requests
from bs4 import BeautifulSoup
from datetime import datetime
from tkinter import *


def metar():
    try:
        now = datetime.now()
        page_url = 'https://www.aviationweather.gov/metar/data?ids='+icao.get()+'&format=raw&date=&hours=0'
        page = requests.get(page_url)  
        soup = BeautifulSoup(page.content, 'html.parser')
        wynik = soup.find('code')
        rezultat1 = now.strftime("%d/%m/%Y, %H:%M")
        rezultat2 = wynik.text
        komunikat1 = Label(root, text=rezultat1)
        komunikat1.pack(pady=10)
        komunikat2 = Label(root, text=rezultat2)
        komunikat2.pack()
    except Exception:
        komunikat1 = Label(root, text="Brak danych METAR dla "+icao.get())
        komunikat1.pack(pady=10)
    
root = Tk()
root.title("METAR")
root.geometry()

naglowek = Label(root, text="Dane pogodowe ze strony www.aviationweather.gov", font=30, fg="blue")
naglowek.pack()

opis = Label(root, text="Wprowadź kod ICAO:", font=20, fg="black", bg="white")
opis.pack(pady=10)

icao = Entry(root, width=4)
icao.pack(pady=10)

click_button = Button(root, text="OK", width=8, command=metar)
click_button.pack()



root.mainloop()          
    

