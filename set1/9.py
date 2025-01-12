
while True:
    try:
        price = int(input("Give me a price for your item: "))
        
        if price > 0:
           price = int(price)
           break
    except:
        print("Input a valid price")

if price > 100:
    newPrice = price - (price * .1)
    print(f'Youre discounted price is {newPrice}')
else:
    print("Not eligable for a discount")