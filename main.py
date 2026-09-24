import json
import random
import string
from pathlib import Path
from tokenize import String

class Bank:
    dataBase = 'data.json'
    data = []

    try:
        if Path(dataBase).exists():
            with open(dataBase) as fs:
                data = json.load(fs.read())
        else:
            print("no such file exists")        
    except Exception as err:
        print(f"an exception occurred: {err}")

    @staticmethod
    def __update():
        with open(Bank.dataBase, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountGenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spChar = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spChar
        random.shuffle(id)
        return "".join(id)



    def __createAccount(self):
        info={
            "name": input("Enter your name:"),
            "age": int(input("Enter your age:")),
            "email": input("Enter your email:"),
            "pin": int(input("Enter your 4 number pin:")),
            "account no": Bank.__accountGenerate(),
            "balance": 0
        }

        if info["age"] < 18 or len(str(info['pin'])) != 4:
            print("You are not eligible to create an account")
        else:
            print("Account created successfully")
            for i in info:
                print(f"{i}: {info[i]}")
            print("please note down your account number for future reference")


            Bank.data.append(info)
            Bank.__update()

    def __deposit(self):
        account = input("Enter your account number:")
        pin = int(input("Enter your pin:"))
        amount = int(input("Enter the amount to deposit:"))

        for i in Bank.data:
            if i["account no"] == account and i["pin"] == pin:
                i["balance"] += amount
                print(f"Amount deposited successfully. New balance is {i['balance']}")
                Bank.__update()
                return
        print("Invalid account number or pin")

    def __withdrawal(self):
        account = input("Enter your account number:")
        pin = int(input("Enter your pin:"))
        amount = int(input("Enter the amount to withdraw:"))

        for i in Bank.data:
            if i["account no"] == account and i["pin"] == pin:
                if i["balance"] >= amount:
                    i["balance"] -= amount
                    print(f"Amount withdrawn successfully. New balance is {i['balance']}")
                    Bank.__update()
                    return
                else:
                    print("Insufficient balance")
                    return
        print("Invalid account number or pin")


    def __details(self):
        account = input("Enter your account number:")
        pin = int(input("Enter your pin:"))

        for i in Bank.data:
            if i["account no"] == account and i["pin"] == pin:
                print(f"Name: {i['name']}")
                print(f"Age: {i['age']}")
                print(f"Email: {i['email']}")
                print(f"Account Number: {i['account no']}")
                print(f"Balance: {i['balance']}")
                return
        print("Invalid account number or pin")

    def __updateDetails(self):
        account = input("Enter your account number:")
        pin = int(input("Enter your pin:"))

        for i in Bank.data:
            if i["account no"] == account and i["pin"] == pin:
                print("What do you want to update?")
                print("press 1 for name")
                print("press 2 for age")
                print("press 3 for email")
                check = int(input("Enter your choice:"))
                if check == 1:
                    i["name"] = input("Enter your new name:")
                elif check == 2:
                    i["age"] = int(input("Enter your new age:"))
                elif check == 3:
                    i["email"] = input("Enter your new email:")
                else:
                    print("Invalid choice")
                    return
                print("Details updated successfully")
                Bank.__update()
                return
        print("Invalid account number or pin")


    def __deleteAccount(self):
        account = input("Enter your account number:")
        pin = int(input("Enter your pin:"))

        for i in Bank.data:
            if i["account no"] == account and i["pin"] == pin:
                Bank.data.remove(i)
                print("Account deleted successfully")
                Bank.__update()
                return
        print("Invalid account number or pin")
    

user = Bank()
print("press 1 for creating an account")
print("press 2 for Deposit")
print("press 3 for Withdrawal")
print("press 4 for details")
print("press 5 for updating details")
print("press 6 for deleting account")

check = int(input("Enter your choice: "))

if check ==1:
    user.__createAccount()

if(check == 2):
    user.__deposit()

if(check == 3):
    user.__withdrawal()

if(check == 4):
    user.__details()

if(check == 5):
    user.__updateDetails()

if(check == 6):
    user.__deleteAccount()