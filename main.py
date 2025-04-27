import time
from config import CITIES, FETCH_INTERVAL
from api import get_weather_data
from transform import transform_weather_data
from db import insert_weather_data

def run_etl():
    for city in CITIES:
        print(f"[INFO] Coletando dados de {city}...")
        raw_data = get_weather_data(city)
        transformed = transform_weather_data(raw_data)
        if transformed:
            insert_weather_data(transformed)

if __name__ == "__main__":
    while True:
        print("[INFO] Iniciando ciclo ETL...")
        run_etl()
        print(f"[INFO] Aguardando {FETCH_INTERVAL // 60} minutos...")
        time.sleep(FETCH_INTERVAL)
