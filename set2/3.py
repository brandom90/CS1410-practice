


while True:
    try:
        total_amount  = float(input("Total price of shopping cart items "))
        
        total_items  = int(input("Number of items on cart: "))
        
        is_member  = bool(input("Is the customer is a member: "))
        if is_member.lower() == "yes":
            is_member = True
        elif is_member.lower() == "no":
            is_member = False

        is_first_time_buyer  = bool(input("Is this your first time purchase: "))
        if is_first_time_buyer.lower() == "yes":
            is_first_time_buyer = True
        elif is_first_time_buyer.lower() == "no":
            is_first_time_buyer = False
        break
    except:
        print("One input isn't a valid number/boolean")

finalPrice = 0
if total_amount > 200:
    if is_member:
        finalPrice = total_amount - (total_amount*.2)
        print(f'You recieved a 20% discount, your price is now {finalPrice}')
    else:
        finalPrice = total_amount - (total_amount*.1)
        print(f'You recieved a 10% discount, your price is now {finalPrice}')
elif total_amount >= 100 and total_amount <=200:
    finalPrice = total_amount - (total_amount*.05)
    if total_items > 5:
        if finalPrice >= 10:
            finalPrice -= 10
        else:
            finalPrice = 0
        print(f'You recieved a 5% discount, with an additional deducted 10 dollars, your price is now {finalPrice}')
    else:
        print(f'You recieved a 5% discount, your price is now {finalPrice}')
elif total_amount < 100:
    finalPrice = total_amount
    if is_first_time_buyer:
        if finalPrice >= 5:
            finalPrice -= 5
        else:
            finalPrice = 0
        print(f'You recieved a 5 dollar discount, your price is now {finalPrice}')
else:
    print("Not eligable for a discount")

