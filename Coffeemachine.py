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

    while True:
        action = input("Write action: (buy, fill, take, remaining, exit)")
        if action == "buy":
            coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
            print("I have enough resources, making you a coffee!")
            if coffee_type == "1":
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
            if coffee_type == "2": # Latte
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
            if coffee_type == "3": # Cappucino
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
                continue        
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