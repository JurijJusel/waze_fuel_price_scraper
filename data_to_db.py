import psycopg2
import json
from datetime import datetime
from connect_to_db import db_connection

json_file_path = "data/fuel.json"
connection = db_connection()

def query_existing_station_id(connection, company):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT station_id FROM stations WHERE station_name = %s", (company,))
        station_id_record = cursor.fetchone()
        cursor.close()
        return station_id_record
    except (Exception, psycopg2.DatabaseError) as err:
        print("Error get existing id:", err)
        return None


def query_update_date_for_existing_station_record(connection, company):
    try:
        cursor = connection.cursor()
        update_query = "UPDATE stations SET updated_date = %s WHERE station_name = %s"
        updated_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(update_query, (updated_date, company))
        connection.commit()
        cursor.close()
        print("Updated date for existing record:", company, updated_date)
    except (Exception, psycopg2.DatabaseError) as err:
        print("Error updating existing record:", err)


def query_insert_new_staion_record(connection, company):
    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO stations (station_name, created_date) VALUES (%s, %s)"
        created_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(insert_query, (company, created_date))
        connection.commit()
        cursor.close()
        print("Inserted new record:", company, created_date)
    except (Exception, psycopg2.DatabaseError) as err:
        print("Error inserting new record:", err)
        
        
# def query_get_fuel_id(connection):
#     try:
#         cursor = connection.cursor()
#         cursor.execute("SELECT MAX(fuel_id) FROM fuel")  #"SELECT fuel_id FROM fuel"
#         fuel_id = cursor.fetchone()[0]
#         cursor.close()
#         return fuel_id
#     except (Exception, psycopg2.DatabaseError) as err:
#         print("Error getting inserted fuel_id:", err)
#         return None
        
        
def query_insert_fuel_data_record(connection, web_updated_date, diesel, a95):
    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO fuel (web_updated_date, diesel, a95) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (web_updated_date, diesel, a95))
        connection.commit()
        cursor.close()
        print("Inserted fuel data:", web_updated_date, diesel, a95)
    except (Exception, psycopg2.DatabaseError) as err:
        print("Error inserting fuel data:", err)


def split_address(input_string):
    address_split = input_string.split(', ')
    street_parts = address_split[0].split()
    if street_parts[-2].endswith('.'):
        street_name = ' '.join(street_parts[:-2]) + ' ' + street_parts[-2]
        street_number = street_parts[-1]
    else:
        street_name = ' '.join(street_parts[:-1])
        street_number = street_parts[-1]
    city = address_split[1]
    return street_name, street_number, city


def query_insert_address_data(connection, street, street_nm, city):
    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO address (street, street_nm, city) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (street, street_nm, city))
        connection.commit()
        cursor.close()
        print("Inserted address data:", street, street_nm, city)
    except (Exception, psycopg2.DatabaseError) as err:
        print("Error inserting address data:", err)

  
def json_data_to_db(connection, json_file):
    if not connection:
        return
    try:
        with open(json_file, 'r') as file:
            json_obj = json.load(file)     
       
        for item in json_obj:  
            company = item['company']
            address = item['address']
            street, street_nm, city = split_address(address)
            # print(f"{street} - {street_nm} - {city}")
            # try:
            station_id = query_existing_station_id(connection, company)
            query_insert_address_data(connection, street, street_nm, city)

            if station_id:
                query_update_date_for_existing_station_record(connection, company)
            else:
                query_insert_new_staion_record(connection, company)
                    
            # web_updated_date = item['fuel_updated_date']  # fuel table
            # diesel = float(item['diesel']) if item['diesel'] != '-' else 0
            # a95 = float(item['95']) if item['95'] != '-' else 0
            # query_insert_fuel_data_record(connection, web_updated_date, diesel, a95)
                    
            
                
        connection.close()
        print("Successful insert/update data to db")
    except (Exception, psycopg2.DatabaseError) as err:
        print("Error insert/update data to PostgreSQL:", err)
        
        
json_data_to_db(connection, json_file_path)





# def query_existing_record_id(connection, company, address):
#     try:
#         cursor = connection.cursor()
#         cursor.execute("SELECT id FROM stations WHERE station_name = %s AND address = %s", (company, address))
#         record_id = cursor.fetchone()
#         cursor.close()
#         return record_id
#     except (Exception, psycopg2.DatabaseError) as err:
#         print("Error retrieving existing id:", err)
#         return None

# def json_data_to_db(connection, json_file):
#     time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     if not connection:
#         return 
#     try:
#         cursor = connection.cursor()

#         with open(json_file, 'r') as file:
#             json_obj = json.load(file)      

#         for item in json_obj:  
#             company = item['company']
#             address = item['address']
#             existing_id = query_existing_record_id(connection, company, address)

#             if existing_id:
#                 query_update = "UPDATE stations SET updated_date = %s WHERE id = %s"
#                 updated_date = time_stamp  # datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#                 cursor.execute(query_update, (updated_date, existing_id[0]))
#             else:
#                 query_insert = "INSERT INTO stations (station_name, address, created_date) VALUES (%s, %s, %s)"
#                 created_date = time_stamp  # datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#                 cursor.execute(query_insert, (company, address, created_date))

#             connection.commit()
            
#         cursor.close()
#         connection.close()
#         print("Successful insert/update data to db.")
#     except (Exception, psycopg2.DatabaseError) as err:
#         print("Error insert/update data to PostgreSQL:", err)

# json_data_to_db(connection, json_file_path)


# def json-data_to_db(connection, json_file):
#     if not connection:
#         return
#     try:
#         cursor = connection.cursor()

#         with open(json_file, 'r') as file:
#             json_obj = json.load(file)      

#         for item in json_obj:  
#             company = item['company']
#             address = item['address']
#             created_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
#             insert_query = "INSERT INTO stations (station_name, address, created_date) VALUES (%s, %s, %s)"
#             data = (company, address, created_date)
            
#             cursor.execute(insert_query, data)
#             connection.commit()
            
#         cursor.close()
#         connection.close()
#         print("Successful insert data to PostgreSQL")
#     except (Exception, psycopg2.DatabaseError) as err:
#         print("Error insert data to PostgreSQL:", err)
