import os
import bcrypt, psycopg2
from psycopg2 import Error
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def get_ms_pwd():
   user_input = input('Enter master password for your vault creation :- ').encode('utf-8')
   
   hashed = bcrypt.hashpw(user_input, bcrypt.gensalt())
   hashed_ms_pwd = hashed.decode(encoding='UTF-8',errors='strict')
   # print(hashed)
   # print(type(hashed_ms_pwd))
   
   return hashed_ms_pwd;

def rem_work (username):
   try:
    connection = psycopg2.connect(user="postgres",
                                  password=os.getenv('PASSWORD'),
                                  host="127.0.0.1",
                                  port="5432",
                                  database= username)

    cursor = connection.cursor()
    # SQL query to create a new table
    create_table_query1 = '''CREATE TABLE master_password
          (ms_pwd VARCHAR (250) PRIMARY KEY NOT NULL); '''
    # Execute a command: this creates a new table
    cursor.execute(create_table_query1)
    connection.commit()
   #  print("Table created successfully in PostgreSQL ")
   
   # Executing a SQL query to insert data into  table
    master_password = get_ms_pwd()
    insert_query = """ INSERT INTO master_password (ms_pwd) VALUES ('{}')""".format(master_password)
    cursor.execute(insert_query)
    connection.commit()
    
    create_table_query2 = '''CREATE TABLE passwords
          (id BIGSERIAL PRIMARY KEY NOT NULL,
           username VARCHAR (100) NOT NULL,
           email VARCHAR (100),
           pwd VARCHAR (200) NOT NULL,
           key VARCHAR (200) NOT NULL,
           wesbite_org VARCHAR (75)); '''
    # Execute a command: this creates a new table
    cursor.execute(create_table_query2)
    connection.commit()

   except (Exception, Error) as error:
      print("Error while connecting to PostgreSQL", error)
   finally:
      if connection:
         cursor.close()
         connection.close()
         print("\n=============================================================================")
         print("Everything set! Now you can restart program and go with existing user!")
         print("=============================================================================\n")
   