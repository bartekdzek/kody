# RESULT TO VIEW ON PAGE https://pixe.la/v1/users/bartek5924/graphs/graph1.html

import requests
from datetime import datetime

# Definiujemy podstawowy endpoint Pixela API
pixela_endpoint = "https://pixe.la/v1/users"

# Ustawiamy nazwy użytkownika i token, które będą używane do autoryzacji
USERNAME = "bartek5924"
TOKEN = ""
GRAPH_ID = "graph1"

# Tworzymy parametry dla użytkownika Pixela
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",  # Zgadzamy się na warunki korzystania z usługi
    "notMinor": "yes",             # Potwierdzamy, że jesteśmy pełnoletni
}

# Tworzymy konto użytkownika na Pixela
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Definiujemy endpoint dla tworzenia wykresu
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Konfigurujemy ustawienia nowego wykresu
graph_config = {
    "id": GRAPH_ID,
    "name": "Hours of programming",  # Nazwa wykresu
    "unit": "hours",                 # Jednostka pomiaru
    "type": "float",                 # Typ danych na wykresie
    "color": "ajisai",               # Kolor wykresu
}

# Tworzymy nagłówki autoryzacyjne dla żądań HTTP
headers = {
    "X-USER-TOKEN": TOKEN,
}

# Tworzymy nowy wykres
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Definiujemy endpoint do dodawania danych do wykresu
pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# Pobieramy dzisiejszą datę
today = datetime.now()

# Tworzymy dane do wysłania na wykres
pixela_data = {
    "date": today.strftime("%Y%m%d"),  # Format daty w formacie YYYYMMDD
    "quantity": input("How many hours did you code today?"),  # Pobieramy ilość godzin kodowania od użytkownika
}

# Wysyłamy dane do wykresu
response = requests.post(url=pixela_creation_endpoint, json=pixela_data, headers=headers)
print(response.text)

# EDYCJA DANYCH
# Definiujemy endpoint do edycji danych na wykresie
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# Nowe dane do zaktualizowania
new_pixel_data = {
    "quantity": "3.5"  # Aktualizujemy ilość godzin kodowania
}

# Aktualizujemy dane na wykresie
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# USUWANIE DANYCH
# Definiujemy endpoint do usuwania danych z wykresu
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# Usuwamy dane z wykresu
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)