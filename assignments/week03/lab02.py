# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = int(input("Choose option: "))
        if choice == 1:
            print("Your Balance : " ,balance)
            break
        elif choice == 2:
            withdraw = float(input("Withdraw : "))
            if withdraw > 0:
             balance = balance - withdraw
             print("Your Balance : " ,balance)
            else:
                print("Error")
            break
        elif choice == 3:
            deposit = float(input("Deposit : "))
            if deposit > 0:
             balance = balance + deposit
             print("Your Balance : " ,balance)
            else:
             print("Error")
            break
        elif choice == 4:
            break
        else:
            print("Error")
        
        # Complete the menu logic here
        # Your code here:
else:
    print("Invalid PIN")
