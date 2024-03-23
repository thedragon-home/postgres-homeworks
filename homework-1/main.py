"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import os, csv

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="12345"
)

#Подключение к базе данных
try:
    for filename in os.listdir('north_data'):
        with psycopg2.connect(
            host="localhost",
            database="north",
            user="postgres",
            password="12345"
        ) as conn:

            with conn.cursor() as cur:
                with open(f'north_data\\{filename}') as file:
                    header = next(file)
                    reader = csv.reader(file)
                    for row in reader:
                        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", row)
finally:
    conn.close()


