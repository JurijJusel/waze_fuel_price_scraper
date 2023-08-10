import psycopg2
import json


json_file_path = "data/fuel.json"
 
db_params = {
    'host': '127.0.0.1',
    'port': 5432,
    'database': 'Fuel',
    'user': 'postgres',
    'password': 'asdfgh'
}

    
def from_json_to_db(json_file):
    try:
        connection = psycopg2.connect(**db_params) 
        cursor = connection.cursor()

        with open(json_file, 'r') as file:
            json_obj = json.load(file)      

        for item in json_obj:
            diesel_value = float(item['diesel']) if item['diesel'] != '-' else 0
            a95_value = float(item['95']) if item['95'] != '-' else 0
          
            cursor.execute(
                "INSERT INTO fuel_prices (company, address, fuel_updated_date, diesel, a95) VALUES (%s, %s, %s, %s, %s)", 
                (item['company'],
                    item['adress'],
                    item['fuel_updated_date'],
                    diesel_value,
                    a95_value)
                )
            
        # Commit the changes and close the cursor and connection
        connection.commit()
        cursor.close()
        connection.close()
        print("Successful to insert data to db")
    except (Exception, psycopg2.DatabaseError) as err:
        print("Error insert data to postgresSQL:", err)

 
from_json_to_db(json_file_path)
 
   # try:
#     connection = psycopg2.connect(**db_params)
#     print("Connected to PostgreSQL successfully.")
# except (Exception, psycopg2.DatabaseError) as error:
#     print("Error:", error)
     
# try:
#     connection = psycopg2.connect(
#         database="fuel_prices",
#         host='localhost',
#         port=5432,
#         user="postgres",
#         password="asdfgh")
#     print("Connected to PostgreSQL successfully.")
# except (Exception, psycopg2.DatabaseError) as error:
#     print("Error:", error)
    