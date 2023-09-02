import psycopg2
import json
from datetime import datetime
from connect_to_db import db_connection
from utils.file import create_json, read_json

json_file_path = "data/fuel.json"
connection = db_connection()


def check_tables_in_migration():
    migration_data = read_json('migration.json')
    table_names = [name.get("table_name") for name in migration_data]
    unique_table_names = sorted(list(set(table_names)))
    return unique_table_names
  
    
def query_existing_tables(cursor):
    cursor = connection.cursor()
    query = """
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_catalog = 'Fuel'
        AND table_schema = 'public'
    """
    cursor.execute(query)
    existing_tables = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return existing_tables


def query_create_stations_table(connection):
    try:
        cursor = connection.cursor()
        station_table_query = """
        CREATE TABLE stations(
        station_id SERIAL NOT NULL,
        station_name character varying(30) NOT NULL,
        address character varying(40) NOT NULL,
        created_date timestamp without time zone NOT NULL,
        updated_date timestamp without time zone,
        fk_fuel_id integer NOT NULL,
        fk_address_id integer NOT NULL,
        PRIMARY KEY(station_id),
        CONSTRAINT fk_station_fuel FOREIGN key(fk_fuel_id) REFERENCES fuel(fuel_id),
        CONSTRAINT fk_station_address FOREIGN key(fk_address_id) REFERENCES address(address_id)
        );"""
        cursor.execute(station_table_query)
        connection.commit()
        cursor.close()
        created_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = [{'created_date': created_date, 'table_name': 'stations', 'table_query': station_table_query}]
        create_json(data, 'migration.json')
        print("Table 'stations' created successfull!")
    except psycopg2.Error as err:
        print("Error creating 'stations' table:", err)


def query_create_fuel_table(connection):
    try:
        cursor = connection.cursor()
        fuel_table_query = """
        CREATE TABLE fuel(
        fuel_id SERIAL NOT NULL,
        web_updated_date timestamp without time zone NOT NULL,
        diesel numeric NOT NULL,
        a95 numeric NOT NULL,
        PRIMARY KEY(fuel_id)
        );"""
        cursor.execute(fuel_table_query)
        connection.commit()
        cursor.close()
        created_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = [{'created_date': created_date, 'table_name': 'fuel', 'table_query': fuel_table_query}]
        create_json(data, 'migration.json')
        print("Table 'fuel' created successfull!")
    except psycopg2.Error as err:
        print("Error creating 'fuel' table:", err)


def query_create_address_table(connection):
    try:
        cursor = connection.cursor()
        address_table_query = """
        CREATE TABLE address(
        address_id SERIAL NOT NULL,
        street character varying(40) NOT NULL,
        house_number character varying(10) NOT NULL,
        city character varying(30) NOT NULL,
        PRIMARY KEY(address_id)
         );"""
        cursor.execute(address_table_query)
        connection.commit()
        cursor.close()
        created_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = [{'created_date': created_date, 'table_name': 'address', 'table_query': address_table_query}]
        create_json(data, 'migration.json')
        print("Table 'address' created successfull!")
    except psycopg2.Error as err:
        print("Error creating 'address' table:", err)
        
        
def query_existing_station_id(connection, company, address):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT station_id FROM stations WHERE station_name = %s AND address = %s", (company, address))
        station_id_record = cursor.fetchone()
        cursor.close()
        return station_id_record
    except (Exception, psycopg2.DatabaseError) as err:
        print("Error get existing id:", err)
        return None
    

def query_update_date_for_existing_station_record(connection, company, address):
    try:
        cursor = connection.cursor()
        update_query = "UPDATE stations SET updated_date = %s WHERE station_name = %s AND address = %s"
        updated_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(update_query, (updated_date, company, address))
        connection.commit()
        cursor.close()
        print("Updated date for station existing record:", company, address, updated_date)
    except (Exception, psycopg2.DatabaseError) as err:
        print("Error updating existing record:", err)


def query_insert_new_staion_record(connection, company, address, address_id, fuel_id):
    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO stations (station_name, address, created_date, fk_address_id, fk_fuel_id) VALUES (%s, %s, %s, %s, %s)"
        created_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(insert_query, (company, address, created_date, address_id, fuel_id))
        connection.commit()
        cursor.close()
        print("Inserted new station record:", company, address, created_date, address_id, fuel_id)
    except (Exception, psycopg2.DatabaseError) as err:
        print("Error inserting new record:", err)
        
           
def query_get_fuel_id(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT MAX(fuel_id) FROM fuel")  
        fuel_id = cursor.fetchone()[0]
        cursor.close()
        return fuel_id
    except (Exception, psycopg2.DatabaseError) as err:
        print("Error getting inserted fuel_id:", err)
        return None
    

def query_get_address_id(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT MAX(address_id) FROM address")  
        address_id = cursor.fetchone()[0]
        cursor.close()
        return address_id
    except (Exception, psycopg2.DatabaseError) as err:
        print("Error getting inserted address_id:", err)
        return None

    
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
        

def query_update_fuel_data_record(connection, fuel_id, web_updated_date, diesel, a95):
    try:
        cursor = connection.cursor()
        update_query = "UPDATE fuel SET web_updated_date = %s, diesel = %s, a95 = %s WHERE fuel_id = %s"
        cursor.execute(update_query, (web_updated_date, diesel, a95, fuel_id))
        connection.commit()
        cursor.close()
        print("Updated fuel data:", web_updated_date, diesel, a95)
    except (Exception, psycopg2.DatabaseError) as err:
        print("Error updating fuel data:", err)
        
        
def split_address(input_string):
    address_split = input_string.split(', ')
    street_parts = address_split[0].split()
    if street_parts[-2].endswith('.'):
        street_name = ' '.join(street_parts[:-2]) + ' ' + street_parts[-2]
        house_number = street_parts[-1]
    else:
        street_name = ' '.join(street_parts[:-1])
        house_number = street_parts[-1]
    city = address_split[1]
    return street_name, house_number, city


def query_insert_address_data(connection, street, house_number, city):
    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO address (street, house_number, city) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (street, house_number, city))
        connection.commit()
        cursor.close()
        print("Inserted address data:", street, house_number, city)
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
            street, house_number, city = split_address(address)
            station_id = query_existing_station_id(connection, company, address)
            
            web_updated_date = item['fuel_updated_date']  
            diesel = float(item['diesel']) if item['diesel'] != '-' else 0
            a95 = float(item['95']) if item['95'] != '-' else 0
                 
            if station_id:
                fuel_id = query_get_fuel_id(connection)
                query_update_fuel_data_record(connection, fuel_id, web_updated_date, diesel, a95)
                query_update_date_for_existing_station_record(connection, company, address)
            else:
                query_insert_fuel_data_record(connection, web_updated_date, diesel, a95)
                query_insert_address_data(connection, street, house_number, city)
                fuel_id = query_get_fuel_id(connection)
                address_id = query_get_address_id(connection)
                query_insert_new_staion_record(connection, company, address, address_id, fuel_id)  

            connection.commit()       
        print("Successful insert/update data to db")
    except (Exception, psycopg2.DatabaseError, psycopg2.Error, psycopg2.DataError) as err:
        print("Error data_to_db insert/update data to PostgreSQL:", err)
    finally:
        connection.close()
   
        
def run_create_tables(connection): 
    try:  
        cursor = connection.cursor()
        existing_tables = query_existing_tables(cursor)
        migration_tables = check_tables_in_migration()
        if not migration_tables:
            query_create_fuel_table(connection)
            query_create_address_table(connection)
            query_create_stations_table(connection)
        else:    
            for table_name in migration_tables:
                if table_name not in existing_tables:
                    function_name = f"query_create_{table_name}_table"
                    create_function = globals().get(function_name)
                    create_function(connection)
                else:
                    print(f"Table '{table_name}' already exist.")
    except Exception as e:
        print("An error create tables occurred:", e)
    finally:
        cursor.close()


run_create_tables(connection)
json_data_to_db(connection, json_file_path)

