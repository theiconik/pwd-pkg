import os
import bcrypt, psycopg2
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def change_ms_pwd():
   user_input = input('Enter the new password: ').encode('utf-8')
   
   hashed = bcrypt.hashpw(user_input, bcrypt.gensalt())
   hashed_ms_pwd = hashed.decode(encoding='UTF-8',errors='strict')
   # print(hashed)
   # print(type(hashed_ms_pwd))
   
   return hashed_ms_pwd;



def update_db_ms_pwd(username):
    print("================================")
    print("||   Change Master Password   ||")
    print("================================\n")
    
    try:
        connection = psycopg2.connect(user="postgres",
                                    password=os.getenv('PASSWORD'),
                                    host="127.0.0.1",
                                    port="5432",
                                    database= username)

        cursor = connection.cursor()
        
        changed = change_ms_pwd()
        
        cursor.execute("UPDATE master_password SET ms_pwd = '{}';".format(changed))
        connection.commit()
        print("\n*******************************************")
        print("Master Password Updated successfully")
        print("*******************************************")

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
    return


# update_db_ms_pwd()

   