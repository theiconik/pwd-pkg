import os
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def user_db_create(username):
   try:
      # Connect to an existing database
      connection = psycopg2.connect(user="postgres",
                                    password=os.getenv('PASSWORD'),
                                    host="127.0.0.1",
                                    port="5432")

      connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
      # Create a cursor to perform database operations
      cursor = connection.cursor()
      #Preparing query to create a database
      sql = '''CREATE database {}'''.format(username);

      #Creating a database
      cursor.execute(sql)

   except Error:
      print("Username is already taken!")
   finally:
      if (connection):
         cursor.close()
         connection.close()