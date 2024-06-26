from random import randint

bal = []
account = []

def createAccount():
    accs = randint(100000, 999999)
    account.append(accs)
    def_bal = 0
    bal.append(def_bal)
    print(f"Account Created: {accs} \nBalance: {def_bal}")

def cont():
    ctn = input("Continue? Y/N: ").lower()
    if ctn == 'y':
        main()
    elif ctn == 'n':
        exit()
    else:
        print("Invalid Input, only Y/N")
        cont()

def login(get_index):
    pin = int(input("Enter 6 Digit PIN: "))
    if pin not in account:
        print("Invalud Account! Try Again")
    else:
        index = account.index(pin)
        get_index(index)

def deposit(get_index):
    ammount = int(input("Enter Ammount: "))
    if ammount < 100:
        print("Deposit Only 100 Above")
    else:
        bal[get_index] += ammount
        print(f"Your Balance Now: {bal[get_index]}")

def checkBalance(get_index):
    print(f"\n{account[get_index]} Your Balance is: {bal[get_index]}\n")

def withdraw(get_index):
    ammount = int(input("Enter Ammount: "))
    if ammount < 100:
        print("Withdraw Only 100 Above")
    else:
        print(f"You Withdraw: {ammount}")
        bal[get_index] -= ammount
        print(f"Your Balance Now: {bal[get_index]}")

def deleteAcc(get_index):
    pin = int(input("Confirm PIN to Delete: "))
    if pin not in account:
        print("Invalid Account")
    else:
        bal.pop(get_index)
        account.pop(get_index)
        print(f"PIN {pin} has been deleted")

def main():
    
    print(f"Account: {account} balance: {bal}")
    print("""
        ---WELCOME TO MyBANK---
        1 : Create Account
        2 : Check Balance
        3 : Deposit
        4 : Withdraw
        5 : Delete Account
        0 : Exit
    """)
    option = input("Select Option: ")

    if option == '1':
        createAccount()
        main()
    elif option == '2':
        login(checkBalance)
        cont()
    elif option == '3':
        login(deposit)
        cont()
    elif option == '4':
        login(withdraw)
        cont()
    elif option == '5':
        login(deleteAcc)
        cont()
    elif option == '0':
        print("Thank You!")
        exit()
    else:
        print("Invalid Option")
main()

