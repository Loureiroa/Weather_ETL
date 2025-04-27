import requests
from config import API_KEY

def get_weather_data(city):
   # Obter dados meteorológicos da API OpenWeather.#
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=pt_br"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança exceção para erros HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter dados para {city}: {e}")
        return None