import os
import psycopg2
from cryptography.fernet import Fernet
from prettytable import PrettyTable
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def retrieve_pwd(username):
    print("================================")
    print("||          Vault             ||")
    print("================================\n")
    
    try:
        connection = psycopg2.connect(user="postgres",
                                    password=os.getenv('PASSWORD'),
                                    host="127.0.0.1",
                                    port="5432",
                                    database=username)

        cursor = connection.cursor()
        
        print("1 -> Show all passwords")
        print("2 -> Show passwords from a username")
        print("3 -> Show passwords from an email")
        print("4 -> Show passwords from a website/organization")
        choice = int(input("Enter the number corresponding to your choice of action :- "))
        
        postgreSQL_select_Query = "";
        if choice == 1:
            postgreSQL_select_Query = "select * from passwords"
        elif choice == 2:
            username = input("Enter your username for the password you lookin for: ")
            postgreSQL_select_Query = "select * from passwords where username = '{}'".format(username)
        elif choice == 3:
            email = input("Enter your email for the password you lookin for: ")
            postgreSQL_select_Query = "select * from passwords where email = '{}'".format(email)
        elif choice == 4:
            web = input("Enter the website/ organization for the password you lookin for: ")
            postgreSQL_select_Query = "select * from passwords where wesbite_org= '{}'".format(web)
        else:
            print("Invalid query number!")

        cursor.execute(postgreSQL_select_Query)
        passwords = cursor.fetchall()
        if len(passwords)==0 :
            print("No record found for that query!")

        # print("Print each row and it's columns values")
        else:
            myTable = PrettyTable(["Username", "Email", "Password", "Website/Organization"])
            for row in passwords:
                
                convert = row[3].encode("utf-8")
                f = Fernet(row[4].encode("utf-8"))
                token = f.decrypt(convert)
                ftoken = token.decode(encoding='UTF-8', errors='strict')
                myTable.add_row([row[1], row[2], ftoken, row[5]])
                
            print(myTable)
            

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            
# retrieve_pwd()