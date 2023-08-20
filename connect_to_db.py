import psycopg2


db_params = {
    'host': '127.0.0.1',
    'port': 5432,
    'database': 'Fuel',
    'user': 'postgres',
    'password': 'asdfgh'
}


def db_connection():
    try:
        connect = psycopg2.connect(**db_params)
        print(f"Connection to the '{db_params['database']}' database is successful.")
        return connect
    except (Exception, psycopg2.DatabaseError) as err:
        print(f"Error connecting to '{db_params['database']}' database PostgreSQL:", err)

