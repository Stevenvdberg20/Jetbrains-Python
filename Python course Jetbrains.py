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

    action = input("Write action: (buy, fill, take)")
    if action == "buy":
        coffee_type = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
        if coffee_type == 1: # Espresso
            water -= 250
            coffee -= 16
            cup -= 1
            money += 4
            print(f"Espresso it is! Machine now contains {water} water, {coffee} coffee, {milk} milk, and {cup} cups.")
        if coffee_type == 2: # Latte
            water -= 350
            coffee -= 20
            milk -= 75
            cup -= 1
            money += 7     
            print(f"Latte done, machine now contains {water} water, {coffee} coffee, {milk} milk, and {cup} cups.")       
        if coffee_type == 3: # Cappucino
            water -= 200
            coffee -= 12
            milk -= 100
            cup -= 1
            money += 6
            print(f"Cappu picked, machine now contains {water} water, {coffee} coffee, {milk} milk, and {cup} cups.")          
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
    
    print("The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")    
    print(f"{coffee} of coffee beans")    
    print(f"{cup} of cups")    
    print(f"{money} of money")    
coffeeMaker()