import sys
# import os
sys.path.append('master_password_core')
sys.path.append('password_manager_core')
sys.path.append('new_user')

from new_user.user_database import user_db_create
from new_user.rem_work import rem_work
from check_user import check_user
from master_password_core.ms_pwd_auth import auth
from master_password_core.change_ms_pwd import update_db_ms_pwd
from password_manager_core.save_pwd import save_pwd
from password_manager_core.retrieve_pwds import retrieve_pwd
from password_manager_core.change_pwd import change_pwd
from password_generator import passwordGenerator
from strength_checker import printStrongNess
from csv_export import csv_export
# import zipfile


print("                              __              __                   ")
print("                             /\ \            /\ \                  ")
print("        _____   __  __  __   \_\ \      _____\ \ \/'\      __      ")
print("       /\ '__`\/\ \/\ \/\ \  /'_` \    /\ '__`\ \ , <    /'_ `\    ")
print("       \ \ \L\ \ \ \_/ \_/ \/\ \L\ \   \ \ \L\ \ \ \\`\ /\ \L\ \   ")
print("        \ \ ,__/\ \___x___/'\ \___,_\   \ \ ,__/\ \_\ \_\ \____ \  ")
print("         \ \ \/  \/__//__/   \/__,_ /    \ \ \/  \/_/\/_/\/___L\ \ ")
print("          \ \_\                           \ \_\            /\____/ ")
print("           \/_/                            \/_/            \_/__/  ")

print("\n====================");
print("1 -> New User")
print("2 -> Existing User")
print("====================")

entry = int(input("Enter choice number:- "))
if entry == 1 :
   print("\n================================")
   print("||    New User Registration   ||")
   print("================================\n")
   username = input("Enter unique username:- ")
   while check_user(username) == 1:
      print("Username ALREADY TAKEN!")
      username = input("Enter unique username:- ")
   user_db_create(username)
   rem_work(username)
   
elif entry == 2 :
   # we'll do something here
   print("\n================================")
   print("||     Existing User Login    ||")
   print("================================\n")
   username = input("Enter username:- ")
   while check_user(username) != 1:
      print("Username INVALID!")
      username = input("Enter username :- ")
   
   master_password = ""
   while auth(username) != 1:
      print("Master Password INCORRECT")
      
   while True:
      print("\n==================================================================")
      print("1 -> Change your master password")
      print("2 -> Store a new password in vault")
      print("3 -> Open vault")
      print("4 -> Generate a password")
      print("5 -> Check Strength of a password")
      print("6 -> Export vault passwords (CSV)")
      print("7 -> Update a vault password")
      print("0 -> Quit")
      print("==================================================================")

      choice = int(input("\nEnter the number corresponding to your choice of action :- "))
      if choice == 0:
         break;
      
      while choice < 0 or choice > 7 :
         print("Please enter a valid choice number!")
         choice = int(input("Enter the number corresponding to your choice of action :- "))
         
      if choice == 1:
         if auth(username) == 1:
            update_db_ms_pwd(username);
         else:
            print("\n*******************************************")
            print("Wrong master password!")
            print("*******************************************")
            
      elif choice == 2:
         save_pwd(username)
               
      elif choice == 3:
         retrieve_pwd(username)
         
      elif choice == 4:
         passwordGenerator()
         
      elif choice == 5:
         print("================================")
         print("|| Password Strength Checker  ||")
         print("================================")
         input_string = input("Enter password to check strength: ")
         printStrongNess(input_string)
      
      elif choice == 6:
         if auth(username) == 1:
            csv_export(username)
            # with zipfile.ZipFile("pwd_pkg.zip", "w") as my_zip:
            #    my_zip.write("pwd_pkg_passbook.csv")
            #    my_zip.setpassword(propass.encode("utf-8"))
               
            # os.remove("pwd_pkg_passbook.csv")  
         else:
            print("\n*******************************************")
            print("Wrong master password!")
            print("*******************************************")
            
      else:
        change_pwd(username) 
   
else:
   sys.exit("Cool!")
   
