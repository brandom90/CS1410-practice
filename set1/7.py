import random

while True:
    try:
        hand = input("Rock Paper or Scissors? : ")
        if hand.lower() == "rock" or "paper" or "scissors":
           break
    except:
        print("type one of those 3 choices")

botHandInt = random.randint(1, 3)
botHand = ""


if botHandInt == 1:
    botHand = "Rock"
elif botHandInt == 2:
    botHand = "Paper"
else:
    botHand = "Scissors"

if hand.upper() == botHand:
    print("Its a Tie")
if hand.lower() == "rock":
    if botHand == "Paper":
        print("You Lose")
    else:
        print("You Win")
if hand.lower() == "paper":
    if botHand == "Scissors":
        print("You Lose")
    else:
        print("You Win")
if hand.lower() == "scissors":
    if botHand == "Rock":
        print("You Lose")
    else:
        print("You Win")