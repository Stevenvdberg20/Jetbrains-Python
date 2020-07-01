# Save the input in this variable
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

    if av_total >= cups:
        print(f"Yes, I can make this shit ez. I can even make {av_total - cups} more.")
    else:
        print(f"Nope, can only make {int(av_total)} cups.")

coffee()