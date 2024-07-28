#Python DataBase 1.0
import time
import os

def save_to_db(file, message):
    f = open(file, "w")
    print("!! Warning Python DataBase NOT use SQL !!")
    print("Thanks For Using MY Library!")
    time.sleep(2)
    f.write(message)
    print("Success")
    f.close()
def create_db(namedb):
    db = namedb
    pdb = open(f"{namedb}" + ".txt", "w")
    pdb.write("Your DataBase Has Created!")
    print(f"DataBase {db} has created!")
    print("You can Change text in your DataBase")
    pdb.close()