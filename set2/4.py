

while True:
    try:
        income  = float(input("Total yearly income: "))
        
        is_married  = bool(input("Are you married?: "))
        if is_married.lower() == "yes":
            is_married = True
        elif is_married.lower() == "no":
            is_married = False
        has_dependents  = bool(input("Are you dependant?: "))
        if has_dependents.lower() == "yes":
            has_dependents = True
        elif has_dependents.lower() == "no":
            has_dependents = False
        owns_business  = bool(input("Do you own a business?: "))
        if owns_business.lower() == "yes":
            owns_business = True
        elif owns_business.lower() == "no":
            owns_business = False
        break
    except:
        print("One or more inputs isn't a valid number/boolean")
tax = 0
if income < 30000:
    if not is_married:
        tax = 10
        print(f'Your tax is {tax}%')
    else:
        tax = 8
        print(f'Your tax is {tax}%')
elif income >= 30000 and income <= 100000:
    if has_dependents:
        if not is_married:
            tax = 15
            print(f'Your tax is {tax}%')
        else:
            tax = 12
            print(f'Your tax is {tax}%')
    else:
        tax = 18
        print(f'Your tax is {tax}%')
elif income > 100000:
    if owns_business:
        tax = 25
        print(f'Your tax is {tax}%')
    else:
        tax = 28
        print(f'Your tax is {tax}%')

