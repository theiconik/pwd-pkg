import os
import psycopg2
from cryptography.fernet import Fernet
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def save_pwd(username):
    print("================================")
    print("||   Add Password to Vault    ||")
    print("================================\n")
    
    try:
        connection = psycopg2.connect(user="postgres",
                                    password=os.getenv('PASSWORD'),
                                    host="127.0.0.1",
                                    port="5432",
                                    database= username)

        cursor = connection.cursor()
        
        username = input("Enter username: ")
        email = input("Enter email: ")
        pwd = input("Enter password: ")
        
        epwd = pwd.encode("utf-8")
        key = Fernet.generate_key()
        dkey = key.decode(encoding='UTF-8', errors='strict')
        f = Fernet(key)
        token = f.encrypt(epwd)
        etoken = token.decode(encoding='UTF-8', errors='strict')
        
        website_org = input("Enter website/ organization: ")
        
        # Executing SQL query to insert data into  table
        insert_query = """ INSERT INTO passwords (username, email, pwd, key, wesbite_org) VALUES ('{}', '{}', '{}', '{}', '{}');""".format(
            username, email, etoken , dkey, website_org)
        cursor.execute(insert_query)
        connection.commit()
        print("\n*******************************************")
        print("Password saved successfully")
        print("*******************************************")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            
# save_pwd()
