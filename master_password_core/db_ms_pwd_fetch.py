import os
import psycopg2
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def db_ms_pwd(username) :
    connection = psycopg2.connect(user="postgres",
                                    password=os.getenv('PASSWORD'),
                                    host="127.0.0.1",
                                    port="5432",
                                    database= username)
    
    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT * from master_password"

    cursor.execute(postgreSQL_select_Query)
    records = cursor.fetchall()
    
    hashed_pwd = ""

    for row in records:
        hashed_pwd = row[0]
    
    return hashed_pwd
