import os
import psycopg2
from cryptography.fernet import Fernet
from prettytable import PrettyTable
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def take_new_pwd():
   pwd = input("Enter new password : ")
   epwd = pwd.encode("utf-8")
   key = Fernet.generate_key()
   dkey = key.decode(encoding='UTF-8', errors='strict')
   f = Fernet(key)
   token = f.encrypt(epwd)
   etoken = token.decode(encoding='UTF-8', errors='strict')
   return [etoken, dkey]

def change_pwd(username):
    print("================================")
    print("||      Change Password       ||")
    print("================================\n")
    
    try:
        connection = psycopg2.connect(user="postgres",
                                    password=os.getenv('PASSWORD'),
                                    host="127.0.0.1",
                                    port="5432",
                                    database=username)

        cursor = connection.cursor()
        
        postgreSQL_select_Query1 = "select * from passwords";

        cursor.execute(postgreSQL_select_Query1)
        passwords = cursor.fetchall()
        if len(passwords)==0 :
            print("No passwords in your vault!")

        else:
           # print("Print each row and it's columns values")
            myTable1 = PrettyTable(["ID","Username", "Email", "Password", "Website/Organization"])
            for row in passwords:
                  
                  convert = row[3].encode("utf-8")
                  f = Fernet(row[4].encode("utf-8"))
                  token = f.decrypt(convert)
                  ftoken = token.decode(encoding='UTF-8', errors='strict')
                  myTable1.add_row([row[0], row[1], row[2], ftoken, row[5]])
                  
            print(myTable1)
            
            change_row = int(input("Enter the ID of row which contains the password you wanna update:- "))
            while change_row < 1 or change_row > len(passwords):
               print("Please enter valid ID")
               change_row = int(input("Enter the ID of row which contains the password you wanna update:- "))
            
            lst = take_new_pwd()
            cursor.execute("UPDATE passwords SET pwd = '{}' WHERE id = {};".format(lst[0], change_row))
            cursor.execute("UPDATE passwords SET key = '{}' WHERE id = {};".format(lst[1], change_row))
            connection.commit()
            print("\n*******************************************")
            print("Password Updated successfully for ID {}".format(change_row))
            print("*******************************************")
            
            postgreSQL_select_Query2 = "select * from passwords";

            cursor.execute(postgreSQL_select_Query2)
            passwords = cursor.fetchall()
            
            print("Updated Table :-")
            myTable2 = PrettyTable(["ID","Username", "Email", "Password", "Website/Organization"])
            for row in passwords:
                  
                  convert = row[3].encode("utf-8")
                  f = Fernet(row[4].encode("utf-8"))
                  token = f.decrypt(convert)
                  ftoken = token.decode(encoding='UTF-8', errors='strict')
                  myTable2.add_row([row[0], row[1], row[2], ftoken, row[5]])
                  
            print(myTable2)
            

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            
# retrieve_pwd()