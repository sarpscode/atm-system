import sys
print("AKUMADAN RURAL BANK")
print("Welcome")

print("Insert your card here")
security_code = 2022
password_attempt = 1
input_password = ''
is_password_lock = False
your_amount = 500

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
        withdrawal_option = input("Enter amount option: ")
    
    