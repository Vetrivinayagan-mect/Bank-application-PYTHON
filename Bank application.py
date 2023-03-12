import math
print("Welcome to online bank Application!!!")
def signin():
    global username #name of the user
    global pin #password
    global cb
    username=str(input("Create the Username: "))
    pin = str(input("Create the pin: "))
    if len(pin) == 6:
        pin = pin
    else:
        print("A pin consist of 6 digits")
        newpin = str(input("Create the pin: "))
        if len(newpin) != 6:
            print("The pin has to be in 6 digits ")
            signin()
        else:
            pin = newpin
    print("Thanks for creating a account")

def forgotpin():
    recoverpin = str(input("Please creat a new pin: "))
    if len(recoverpin) != 6:
        print("The pin has to be in 6 digits")
        forgotpin()
    else:
        print("The new has been created.Please Log in using new Pin ")
        pin = recoverpin
        login()

def depositinterest(p,r,t):
    # A = P e^(r*t) is the formula for calculatig the compound interest
    p = float(p)
    r = float(r)
    t = float(t)
    rt = r * t
    e = math.exp(rt)
    a = p * e #future value of investment
    return a

def login():
    name1 = str(input("Please enter your username: "))
    pin1 = str(input("Please enter the Pin: "))
    if name1 == username and pin1 == pin:
        print("welcome to the online banking application"+" "+name1)
        print("Please choose the menu down here: ")
        listmenu = ["1-Deposit","2-Withdraw","3-Transfer","4-Check Balance","5-Deposit interest rate","6-Calculate the compound interest"]
        for b in listmenu:
            print(b)
        choose = int(input("Please enter your choose: "))
        d = 0 #deposit
        w = 0 #withdraw
        cb = 0 #currentbalance
        if choose == 1:
            d = int(input("Enter the amount of your deposit: "))
            cb = d + cb
            print("your current balance is"+" "+str(cb))
        elif choose == 2:
            w = int(input("Enter the amount you want to withdraw: "))
            if w > cb:
                print("Your current balance is not sufficient for transcation")
                login()
            else:
                cb=cb-w
                print(str(w)+" "+"has been withdraw from your account"+" ")
                print("Your current balance is "+str(cb))
        elif choose == 3:
            dest = str(input("Please enter the account number of your destination in digit: "))
            if len(dest) == 8:
                amount = int(input("Enter the amount you want to transfer: "))
                if amount > cb:
                    print("Your current balance is not sufficient for transaction ")
                else: 
                    cb = cb - amount
                    print("Your transcation of amount "+str(amount)+" "+"has been transferd to "+str(dest))
                    print("Your current balance is "+str(cb))
            else:
                print("your transcation has been rejected because destination number is invalid ")
        elif choose == 4:
            print("Your current balance is "+str(cb))
        elif choose == 5:
            if d > 50000:
                rate = 3
            elif d >30000:
                rate = 2
            else:
                rate = 1.5
            print("Your current deposit interest rate is "+str(rate)+"%")
        elif choose == 6:
            listoption = ["1-Calculate your compound interest based on your deposit","2-Calculate your compound interst based on your current balance"]
            for n in listoption:
                print(n)
            choice = int(input("Please enter the option above: "))
            if choice == 1:
                timing = str(input("How many years you want to invest your money"))
                if d>50000:
                    ratex = 3/100
                elif d>30000:
                    ratex = 2/100
                else:
                    rate = 1.5/100
                print("Your current balance in "+"timing "+"years will be")
                print(depositinterest(money,ratex,timing))
            elif choice == 2:
                timing1 = str(input("How many years you want to invest your money"))
                money = str(input("Please enter the amount of money you would like to deposit"))
                money - int(money)
                if d>50000:
                    ratex = 3/100
                elif d>30000:
                    ratex = 2/100
                else:
                    rate = 1.5/100
                print("Your current balance in "+"timing "+"years will be")
                print(depositinterest(money,ratex,timing))
        else:
            print("Option is invalid, back to main menu")
            login()
            
    else:
        print("Enter of your username or pin is wrong, Did you creat your account ")
        list1 = ["1-yes","2-no"]
        for i in list1:
            print(i)
        inp = int(input("Enter your choice: "))
        if inp == 1:
            list2 = ["1-Do u want to again log in","2-You forgot your account"]
            for e in list2:
                print(e)
            theanswer = str(input("Please enter your choice "))
            theanswer = int(theanswer)
            if theanswer == 1:
                login()
            elif theanswer == 2:
                forgotpin()
            else:
                print("Option is not available ")
        elif inp == 2:
            print("Please creat your account ")
            signin()

def mainmenu():
    optionname = ["1- sign in","2- login"] 
    for k in optionname:
        print(k)
    option1 = int(input("Enter the your choice: "))
    if option1 == 1:
        signin()
    elif option1 ==2:
        login()
    else:
        print("Option is invalid")
        mainmenu()
    exit()
def exit():
    answer = str(input("Do you still want to conduct transaction? Yes or No: "))
    if answer == "yes" or answer == "Yes":
        login()
    elif answer == "No" or answer =="no":
        print("Thank you for using this app")
    else:
        print("Option is not valid")
        mainmenu()



 
