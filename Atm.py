import sys
print("AKUMADAN RURAL BANK")
print("Welcome")

print("Insert your card here")
security_code = 2022
password_attempt = 1
input_password = ''
is_password_lock = False
your_amount = 1000

while security_code != input_password:
    if password_attempt <= 3:
        print ("Enter Your Code")
        input_password = int(input())
    
    else:
        is_password_lock = True
    password_attempt = password_attempt + 1
    
    if is_password_lock:
        print("Account is aborted due to exceed of limit")
        sys.exit()
    elif security_code != input_password:
        print("Wrong code....Please Try Again")        
    elif security_code == input_password:
        print("Login successful")
        break

while True:
    print("Select option")
    print("1.  Account Information.")
    print("2.  Making Withdrawals.")
    inquire_option = int(input())
    
    if inquire_option == 1:
        print("Current Balance: " + str(your_amount))
    elif inquire_option == 2:
        print("Select amount")
        print("1.  50 , 2. 100 , 3. 150 , 4. 300 , 5. 500")
        withdrawal_option = int(input("Enter amount option: "))
    
        if withdrawal_option ==1:
            print("1.  Confirm Or 2.  Abort")
            confirm1 = int(input())
            if confirm1 == 1:
                currentCash = your_amount - int(50)
                print("Current balance: " + str(currentCash))
                print("Thank You")
                break
            elif confirm1 == 2:
                print("The process has  been successfully aborted..... Thank You!!!")
                break
               
        elif withdrawal_option ==2:
            print("1.  Confirm Or 2.  Abort")
            confirm1 = int(input())
            if confirm1 == 1:
                currentCash = your_amount - int(100)
                print("Current balance: " + str(currentCash))
                print("Thank You")
                break
            elif confirm1 == 2:
                print("The process has been successfully aborted..... Thank You!!!")
                break
                
        elif withdrawal_option ==3:
            print("1.  Confirm Or 2.  Abort")
            confirm1 = int(input())
            if confirm1 == 1:
                currentCash = your_amount - int(150)
                print("Current balance: " + str(currentCash))
                print("Thank You")
                break
            elif confirm1 == 2:
                print("The process has been successfully aborted..... Thank You!!!")
                break
    
        elif withdrawal_option ==4:
            print("1.  Confirm Or 2.  Abort")
            confirm1 = int(input())
            if confirm1 == 1:
                currentCash = your_amount - int(300)
                print("Current balance: " + str(currentCash))
                print("Thank You")
                break
            elif confirm1 == 2:
                print("The process been has successfully aborted..... Thank You!!!")
                break
                
        elif withdrawal_option ==5:
            print("1.  Confirm Or 2.  Abort")
            confirm1 = int(input())
            if confirm1 == 1:
                currentCash = your_amount - int(500)
                print("Current balance: " + str(currentCash))
                print("Thank You")
                break
            elif confirm1 == 2:
                print("The process has been successfully aborted..... Thank You!!!")
                break
        else:
            print("Invalid digit")
            
    else:
        print("Invalid digit.... Please press 1 or 2  to continue!!!")