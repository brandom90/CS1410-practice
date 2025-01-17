# Inputs
age = int(input("Enter your age: "))
income = int(input("Enter your annual income: "))
credit_score = int(input("Enter your credit score: "))

# Nested If/Else
if age >= 18:
    if income >= 30000:
        if credit_score >= 700:
            print("Loan approved.")
        else:
            if credit_score >= 600:
                print("Loan approved with higher interest.")
            else:
                print("Loan denied due to low credit score.")
    else:
        print("Loan denied due to insufficient income.")
else:
    print("Loan denied due to age restriction.")