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
