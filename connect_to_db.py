import psycopg2
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='file.env')

def db_connection():
    db_params = {
        'host': os.getenv('DB_HOST'),
        'port': int(os.getenv('DB_PORT')),
        'database': os.getenv('DB_DATABASE'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD')
    }
    try:
        connect = psycopg2.connect(**db_params)
        print(f"Connection to the '{db_params['database']}' database is successful.")
        return connect
    except (Exception, psycopg2.DatabaseError) as err:
        print(f"Error connecting to '{db_params['database']}' database:", err)

