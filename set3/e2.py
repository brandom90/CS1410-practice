# Inputs
customer_type = input("Are you a 'member' or 'guest'? ").lower()
years = int(input("How many years have you been a member? ")) if customer_type == "member" else 0
first_time = input("Is this your first visit? (yes/no): ").lower() if customer_type == "guest" else ""

# Nested If/Else
if customer_type == "member":
    if years >= 5:
        print("You get a 20% discount.")
    else:
        if years >= 2:
            print("You get a 10% discount.")
        else:
            print("You get a 5% discount.")
elif customer_type == "guest":
    if first_time == "yes":
        print("You get a 5% discount.")
    else:
        print("No discount for repeat guests.")
else:
    print("Invalid customer type.")