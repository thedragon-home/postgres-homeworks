"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2

def load_data_from_csv(db_host, db_name, db_user, db_password, csv_files):
    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )

    try:
        with conn.cursor() as cur:
            for table_name, csv_file in csv_files.items():
                with open(csv_file) as file:
                    header = next(file)
                    reader = csv.reader(file)
                    for row in reader:
                        if table_name == 'employees':
                            query = "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)"
                        elif table_name == 'customers':
                            query = "INSERT INTO customers VALUES (%s, %s, %s)"
                        elif table_name == 'orders':
                            query = "INSERT INTO orders VALUES (%s, %s, %s, %s, %s)"
                        cur.execute(query, row)
        conn.commit()
    finally:
        conn.close()

if __name__ == "__main__":
    # Загрузка данных из переменных окружения
    db_host = ('localhost')
    db_name = ('north')
    db_user = ('postgres')
    db_password = ('12345')

    csv_files = {
        'employees': 'north_data/employees_data.csv',
        'customers': 'north_data/customers_data.csv',
        'orders': 'north_data/orders_data.csv'
    }

    load_data_from_csv(db_host, db_name, db_user, db_password, csv_files)
