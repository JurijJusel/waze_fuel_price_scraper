import psycopg2
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env') 

db_params = {
    'host': os.getenv('DATABASE_HOST'),
    'port': int(os.getenv('DATABASE_PORT')),
    'database': os.getenv('DATABASE_NAME'),
    'user': os.getenv('DATABASE_USER'),
    'password': os.getenv('DATABASE_PASSWORD')
}

def db_connection(db_params):
    try:
        connect = psycopg2.connect(connect_timeout=10, **db_params)
        print(f"Connection to the '{db_params['database']}' database is successful.")
        return connect
    except psycopg2.OperationalError as err:
        error_message = str(err)
        if "not translate host name" in error_message:
            print("Failed to connect: Invalid host name")
        if "does not exist" in error_message:
            print("Wrong database name")
        elif "password authentication failed" in  error_message:
            print("Failed to connect: wrong user name or password")
        else:
            print(f"Failed connecting to the database: {error_message}")
    except Exception as err:
        print(f"An error connecting to the database:", err)