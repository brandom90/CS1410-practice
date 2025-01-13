

while True:
    try:
        income = float(input("What is your income?: "))

        credit_score  = int(input("What is your Credit score (300-850)?"))
        if 300 <= credit_score <= 850:
            continue

        has_collateral    = input("Do you have collateral? ").strip().lower()
        if has_collateral   == "yes":
            has_collateral   = True
        elif has_collateral   == "no":
            has_collateral   = False
        else:
            print("Please enter 'yes' or 'no'.")
            continue
        loan_amount = float(input("Request your loan amount. "))
        if loan_amount > 0:
            continue
        else:
            print("amount has to be greater than 0")
        break
    except:
        print("Invalid input/s")


if credit_score > 750:
    if income > 50000:
        print("loan approved, with a 5 percent interest rate.")
    else:
        print("loan approved, with a 7 percent interest rate.")
elif 600 <= credit_score <= 750:
    if has_collateral:
        print("loan approved, with a 10 percent interest rate.")
    else:
         print("loan not approved.")
elif credit_score < 600:
    print("loan not approved.")