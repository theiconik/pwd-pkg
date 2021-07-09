import csv
import os
import psycopg2
from cryptography.fernet import Fernet
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def csv_export(username):
   # File path and name.
   filePath = os.getcwd() + "/"
   fileName = 'pwd_pkg_passbook.csv'

   # Database connection variable.
   connect = None

   # Check if the file path exists.
   if os.path.exists(filePath):

      try:

         # Connect to database.
         connection = psycopg2.connect(user="postgres",
                                    password=os.getenv('PASSWORD'),
                                    host="127.0.0.1",
                                    port="5432",
                                    database=username)

      except psycopg2.DatabaseError as e:

         # Confirm unsuccessful connection and stop program execution.
         print("Database connection unsuccessful.")
         quit()

      # Cursor to execute query.
      cursor = connection.cursor()

      # SQL to select data from the table.
      sqlSelect = "SELECT * FROM passwords"

      try:

         # Execute query.
         cursor.execute(sqlSelect)

         # Fetch the data returned.
         results = cursor.fetchall()
         passwords_list = []
         for row in results:
            passwords_list.append(list(row))

         # Extract the table headers.
         headers = [i[0] for i in cursor.description]

         # Open CSV file for writing.
         csvFile = csv.writer(open(filePath + fileName, 'w', newline=''),
                              delimiter=',', lineterminator='\r\n',
                              quoting=csv.QUOTE_ALL, escapechar='\\')

         # Add the headers and data to the CSV file.
         csvFile.writerow(headers)
         for row in passwords_list:  
            convert = row[3].encode("utf-8")
            f = Fernet(row[4].encode("utf-8"))
            token = f.decrypt(convert)
            ftoken = token.decode(encoding='UTF-8', errors='strict')
            row[3] = ftoken 
            csvFile.writerow(row)

         # Message stating export successful.
         print("******************************************************************")
         print("Data export successful.")
         print("The CSV was successfully exported to {}".format(filePath))
         print("******************************************************************")

      except psycopg2.DatabaseError as e:

         # Message stating export unsuccessful.
         print("Data export unsuccessful.")
         quit()

      finally:

         # Close database connection.
         connection.close()

   else:

      # Message stating file path does not exist.
      print("File path does not exist.")
      
# csv_export()