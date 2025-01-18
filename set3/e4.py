# Inputs
math_score = int(input("Enter your math score: "))
science_score = int(input("Enter your science score: "))
english_score = int(input("Enter your English score: "))

# Nested If/Else
if math_score >= 85:
    if science_score >= 80:
        if english_score >= 75:
            print("Placement: Advanced.")
        else:
            print("Placement: Intermediate.")
    else:
        print("Placement: Intermediate.")
else:
    print("Placement: Beginner.")


if not math_score >= 85:
    print("Placement: Beginner.")
elif not science_score >= 80:
    print("Placement: Intermediate.")
elif not english_score >= 75:
    print("Placement: Intermediate.")
else:
    print("Placement: Advanced.")
