'''from logic import *

add(2,6)
sub(10,6)
div(4,5)
mul(6,3)
'''


from logic import *

acc_num = int(input("Enter the account number: "))
pin = int(input("Emter the pin: "))

if login(acc_num,pin):
    print("Wellcome to atm the ATM")

    while True:
        print("[c]heck Balance")
        print("[D]eposit")
        print("[W]ithdraw")
        print("[V]iew history")
        print("[E]xit")

        ch = input("Enter the choice: ").upper()
        if ch=='C':
            check_balance()
        elif ch=='D':
            deposit()
        elif ch=='W':
            withdraw()
        elif ch=='v':
            viewtrascation()
        elif ch=='E':
            print("Thankyou")
            break
        else:
            print("Enter valid input")
