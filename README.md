# Weather_ETL
Projetei e implementei um pipeline ETL que coleta dados da API OpenWeather, realiza transformação estruturada e armazena em um banco PostgreSQL modelado com Snowflake Schema.
O projeto segue boas práticas de Engenharia de Dados e está preparado para análises avançadas de clima e expansão futura para BI e ML.

## ⚙️ Tecnologias

- Python (requests, psycopg2, dotenv)
- PostgreSQL
- OpenWeather API

## 🗂️ Diagrama ER (Entidade-Relacionamento)
![Schema](https://github.com/user-attachments/assets/7c02e74e-70de-43e3-99ad-4bd3ddcb7acf)

 ## 🔄 Como funciona o ETL

1. **Extração:** Coleta dados do clima das cidades: São Paulo, Rio de Janeiro, Brasilia, Salvador e Fortaleza a cada 30 minutos.
2. **Transformação:** Converte os dados em um formato estruturado e compatível com o banco.
3. **Carga:** Insere nas tabelas normalizadas do banco PostgreSQL.

## 📝 Principais views

 - Temperatura média diária por cidade 
 - Comparação de condições climáticas entre cidades 
 - Análise de tendências mensais
 - Alertas de condições extremas
 - Dashboard com condições atuais

## 🔐 Segurança e Gerenciamento de Acesso

- Separação de usuários: um para leitura (`weather_reader`), outro para inserção (`weather_etl`)
- Armazenamento seguro de credenciais no `.env`
- Boas práticas de permissão no PostgreSQL

## ⏭️ Próximos passos
- Agendamento com Airflow
- Particionamento de Tabelas
- Dashboard Web (Streamlit)
