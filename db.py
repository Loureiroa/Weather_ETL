import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

def get_or_create_city(cur, data):
    query = """
        INSERT INTO dim_city (city_id, city_name, country)
        VALUES (%s, %s, %s)
        ON CONFLICT (city_id) DO NOTHING
    """
    cur.execute(query, (data["city_id"], data["city_name"], data["country"]))
    return data["city_id"]

def insert_and_return_id(cur, table, columns, values):
    placeholders = ', '.join(['%s'] * len(values))
    col_str = ', '.join(columns)

    # Mapeamento do nome correto da PK para cada dimensão #
    pk_column = {
        "dim_coordinates": "coord_id",
        "dim_weather": "weather_id",
        "dim_temperature": "temp_id",
        "dim_wind": "wind_id",
        "dim_precipitation": "precipitation_id",
        "dim_time": "time_id"
    }.get(table, "id")  # default para "id" se não achar

    query = f"""
        INSERT INTO {table} ({col_str})
        VALUES ({placeholders})
        RETURNING {pk_column}
    """
    cur.execute(query, values)
    return cur.fetchone()[0]


def insert_weather_data(data):
    conn = get_connection()
    cur = conn.cursor()

    try:
        # Inserir ou garantir cidade
        city_id = get_or_create_city(cur, data)

        # Inserir dimensões e obter IDs
        coord_id = insert_and_return_id(cur, "dim_coordinates", ["latitude", "longitude"], [data["latitude"], data["longitude"]])
        weather_id = insert_and_return_id(cur, "dim_weather", ["main", "description", "icon"], [data["weather_main"], data["weather_description"], data["weather_icon"]])
        temp_id = insert_and_return_id(cur, "dim_temperature", ["temperature", "feels_like", "temp_min", "temp_max", "humidity", "pressure"],
                                       [data["temperature"], data["feels_like"], data["temp_min"], data["temp_max"], data["humidity"], data["pressure"]])
        wind_id = insert_and_return_id(cur, "dim_wind", ["speed", "direction"], [data["wind_speed"], data["wind_direction"]])
        prec_id = insert_and_return_id(cur, "dim_precipitation", ["rain_1h", "snow_1h"], [data["rain_1h"], data["snow_1h"]])
        time_id = insert_and_return_id(cur, "dim_time", ["timestamp", "sunrise", "sunset"], [data["timestamp"], data["sunrise"], data["sunset"]])

        # Inserir na tabela fato
        fact_query = """
            INSERT INTO weather_fact (
                city_id, coord_id, weather_id, temp_id,
                wind_id, precipitation_id, time_id,
                visibility, clouds
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(fact_query, (
            city_id, coord_id, weather_id, temp_id,
            wind_id, prec_id, time_id,
            data["visibility"], data["clouds"]
        ))

        conn.commit()
        print(f"[INFO] Dados normalizados inseridos para {data['city_name']}")

    except Exception as e:
        conn.rollback()
        print(f"[ERRO] Falha na inserção de dados: {e}")

    finally:
        cur.close()
        conn.close()
