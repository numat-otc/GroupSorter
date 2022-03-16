#import random
import time

def GenerateID():
    FirstName   = input("enter first names (1xxxx 2xxxx): ")
    LastName    = input("enter surname (xxxxx): ")
    BirthDate   = input("enter birthdate (dd/mm/yyyy): ")
    Gender      = input("enter gender (M/F or U -unidentified or O -other): ")
    PIN         = input("enter secure pin (8 digits): ")


while True:
    while True:
        try:
            print("─"*8)
            print("ID creation and en/decrypt test")
            print("─"*8)
            print("Options:")
            print("1) Generate New ID")
            print("2) ---")
            print("3) ---")
            print("4) ---")
            print("─"*8)
            select = int(input())
            break
        except:
            print("Error, you must enter a valid number"); time.sleep(1)
    if select==1:
        GenerateID()
    else:
        pass


