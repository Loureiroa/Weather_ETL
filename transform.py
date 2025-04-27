from datetime import datetime

def transform_weather_data(data):
    if not data:
        return None
    
    timestamp = datetime.fromtimestamp(data["dt"])

    return {
        # Chave natural (usada como PK em dim_city)
        "city_id": data["id"],
        "city_name": data["name"],
        "country": data["sys"]["country"],

        # Coordenadas geográficas
        "latitude": data["coord"]["lat"],
        "longitude": data["coord"]["lon"],

        # Clima
        "weather_main": data["weather"][0]["main"],
        "weather_description": data["weather"][0]["description"],
        "weather_icon": data["weather"][0]["icon"],

        # Temperatura e pressão
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "temp_min": data["main"]["temp_min"],
        "temp_max": data["main"]["temp_max"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],

        # Vento
        "wind_speed": data["wind"]["speed"],
        "wind_direction": data["wind"].get("deg", 0),  # nem sempre vem

        # Nuvens e visibilidade
        "clouds": data["clouds"]["all"],
        "visibility": data.get("visibility", 0),  # opcional

        # Tempo
        "timestamp": datetime.fromtimestamp(data["dt"]),
        "sunrise": datetime.fromtimestamp(data["sys"]["sunrise"]),
        "sunset": datetime.fromtimestamp(data["sys"]["sunset"]),

        # Precipitação (chuva e neve)
        "rain_1h": data.get("rain", {}).get("1h", 0),
        "snow_1h": data.get("snow", {}).get("1h", 0),
        
        # Novos campos de granularidade (facilitar agrupamentos, filtros e análises)
        
        "date": timestamp.date(),
        "time": timestamp.time(),
        "day_of_week": timestamp.strftime("%A"),
        "month": timestamp.month,
        "year": timestamp.year
    }
