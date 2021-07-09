import os
import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def check_user(username):
   flag = 1
   try:
      # Connect to an existing database
      connection = psycopg2.connect(user="postgres",
                                    password=os.getenv('PASSWORD'),
                                    host="127.0.0.1",
                                    port="5432",
                                    database= username)

   except Error:
      flag = 0
   finally:
      if flag == 0 :
         return 0
      if (connection):
         connection.close()
         return 1