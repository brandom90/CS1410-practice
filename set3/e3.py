# Inputs
age = int(input("Enter your age: "))
income = int(input("Enter your annual income: "))
credit_score = int(input("Enter your credit score: "))

# Nested If/Else

if not age >= 18:
    print("Loan denied due to age restriction.")
if age >= 18 and not income >= 30000:
    print("Loan denied due to insufficient income.")
if credit_score >= 700 and  income >= 30000 and age >= 18:
    print("Loan approved.")
if credit_score >= 600 and age >= 18 and income >= 30000 and credit_score >= 700:
    print("Loan approved with higher interest.")
else:
    print("Loan denied due to low credit score.")

       

    