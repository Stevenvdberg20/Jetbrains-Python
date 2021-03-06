# Save the input in this variable
def digitList():
    ticket = int(input())
    digit_list = [int(digit) for digit in str(ticket)]

    # Add up the digits for each half
    half1 = digit_list[0] + digit_list[1] + digit_list[2]
    half2 = digit_list[3] + digit_list[4] + digit_list[5]
    # Thanks to you, this code will work
    if half1 == half2:
        print("Lucky")
    else:
        print("Ordinary")

# Coffee machine
def coffee():
    water = int(input("ML water left in tank: ")) # 200ml per cup
    milk = int(input("ML milk left in tank:")) # 50ml per cup
    beans = int(input("Grams of beans left: ")) # 15g per cup
    cups = int(input("How many cups you need: "))

    av_water = int(water / 200)
    av_milk = int(milk / 50)
    av_beans = int(beans / 15)
    av_total = min([av_beans, av_milk, av_water])

    if av_total == cups:
        print(f"Yes, I can make that amount of coffee.")
    if av_total > cups:
        print(f"Yes, I can make that amount of coffee (and even {av_total - cups} more than that)")
    else:
        print(f"Nope, can only make {int(av_total)} cups.")

def reccom():
    age = abs(int(input("Age: ")))
    if age <= 16:
        print("Lion King")
    if age > 16 and age <= 25:
        print("Trainspotting")
    if age > 25 and age <= 40:
        print("Matrix")
    if age > 40 and age <= 60:
        print("Pulp Fiction")
    if age > 60:
        print("Breakfast at Tiffany's")

def change_city(new_user_city):
    old_user_city = new_user_city
    print(old_user_city)


user_city = "Istanbul"
#change_city("Paris")

coffee = 120
water = 400
cup = 9
milk = 540
money = 550

def coffeeMaker():
    global coffee
    global water
    global cup
    global milk
    global money
    print("The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")    
    print(f"{coffee} of coffee beans")    
    print(f"{cup} of cups")    
    print(f"{money} of money \n")    

    while True:
        action = input("Write action: (buy, fill, take, remaining, exit)")
        if action == "buy":
            coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
            print("I have enough resources, making you a coffee!")
            if int(coffee_type) == 1: # Espresso
                if water >= 250 and coffee >= 16 and cup >= 1:
                    water -= 250
                    coffee -= 16
                    cup -= 1
                    money += 4
                    #print(f"Espresso it is! Machine now contains {water} water, {coffee} coffee, {milk} milk, and {cup} cups.")
                elif water < 250:
                    print(f"Sorry, not enough water!")
                elif coffee < 16:
                    print("Sorry, not enough coffee beans!")
                elif cup < 1:
                    print("Sorry, not enough cups!")
            elif int(coffee_type) == 2: # Latte
                if water >= 350 and coffee >= 20 and milk >= 75 and cup >= 1:
                    water -= 350
                    coffee -= 20
                    milk -= 75
                    cup -= 1
                    money += 7     
                    #print(f"Latte done, machine now contains {water} water, {coffee} coffee, {milk} milk, and {cup} cups.")
                elif water < 350:
                    print(f"Sorry, not enough water!")
                elif coffee < 20:
                    print("Sorry, not enough coffee beans!")
                elif milk < 75:
                    print("Sorry, not enough milk!")
                elif cup < 1:
                    print("Sorry, not enough cups!")       
            elif int(coffee_type) == 3: # Cappucino
                if water >= 200 and coffee >= 12 and milk >= 100 and cup >= 1:
                    water -= 200
                    coffee -= 12
                    milk -= 100
                    cup -= 1
                    money += 6
                    #print(f"Cappu picked, machine now contains {water} water, {coffee} coffee, {milk} milk, and {cup} cups.")   
                elif water < 200:
                    print(f"Sorry, not enough water!")
                elif coffee < 12:
                    print("Sorry, not enough coffee beans!")
                elif milk < 100:
                    print("Sorry, not enough milk!")
                elif cup < 1:
                    print("Sorry, not enough cups!")
            elif coffee_type == "back":
                break         
        if action == "fill":
            water_refill = abs(int(input("Water refill?")))
            milk_refill = abs(int(input("Milk refill?")))
            coffee_refill = abs(int(input("Coffee refill?")))
            cup_refill = abs(int(input("Cup refill?")))

            water += water_refill
            milk += milk_refill
            coffee += coffee_refill
            cup += cup_refill
            #print(f"{water_refill} water, {milk_refill} milk, {coffee_refill} coffee, and {cup_refill} cups added!")
        if action == "take":
            print(f"I gave you ${money} \n")
            money = 0
        if action == "remaining":
            print("The coffee machine has:")
            print(f"{water} of water")
            print(f"{milk} of milk")    
            print(f"{coffee} of coffee beans")    
            print(f"{cup} of cups")    
            print(f"{money} of money")         
        if action == "exit":
            break
      
coffeeMaker()

def catNames():
    cafe_list = []
    cats_list = []
    while True:
        cafe = input()
        if cafe != "MEOW":
            cafe_split = str.split(cafe) # Maakt van cafe een list waarbij elk woord een nieuw item is in de list
            cafe_list.append(cafe_split[0]) # Add cafe name to list
            cats_list.append(int(cafe_split[1])) # Add # of cats to separate list
        else:
            cafe_index = cats_list.index(max(cats_list)) # Goes through cats_list, finds the max, and returns the index of that max
            print(cafe_list[cafe_index]) # Use index of highest cat number to find cafe name and print it
            break

#catNames()

def primeCheck():
    while True:
        num = int(input())
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    print("This number is not prime")
                    break
            else:
                print("This number is prime")
        else:
            print("This number is not prime")
            
#primeCheck()

Sknals