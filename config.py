import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente de um arquivo .env
load_dotenv()

# Configurações da API
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITIES = ["Sao Paulo,BR", "Rio de Janeiro,BR", "Brasilia,BR", "Salvador,BR", "Fortaleza,BR"]

# Configurações do banco de dados
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", "5432")

# Configurações de tempo #
FETCH_INTERVAL = 1800  # 30 minutos em segundos