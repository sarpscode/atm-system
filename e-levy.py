percentage = 1.5/100
amount_attempt = 1
amount = ""
border_line_block = False
low_amount = 100

print("E-Levy System")
print ("You are welcome!!!")
while True :
    if amount_attempt <= 100:
        print("Please Enter Your Amount")
        amount = float(input())
        
    else:
        border_line_block = True
    amount_attempt = amount_attempt + int(amount)
        
    if border_line_block == True:
        tax = percentage * amount
        print("Your E-Levy is: GHs " + str(tax) + "...... Thank You")
        break
    elif amount_attempt < 100:
        print("Your E-Levy is GHs 0.00")
       
    elif amount > low_amount:
        tax = percentage * amount
       