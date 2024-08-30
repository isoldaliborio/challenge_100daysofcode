import random

#Lottery

# Write a program that simulates a lottery. The program should have a list of seven numbers that represent a lottery ticket. It should then generate seven random numbers. After comparing the two sets of numbers, the program should output a prize based on the number of matches:
# ● £20 for three matching numbers
# ● £40 for four matching numbers
# ● £100 for five matching numbers
# ● £10000 for six matching numbers
# ● £1000000 for seven matching numbers

ticket = [5, 10, 22, 30, 47, 76, 98]
drawn_numbers = random.sample(range(100),7)
# drawn_numbers = [5, 10, 22, 30, 47, 76, 99]
print(drawn_numbers)

count = 0
for number in drawn_numbers:
    if number in ticket:
        count = count + 1

prizes = {
    3: 20,
    4: 40,
    5: 100,
    6: 10000,
    7: 100000,
}

if count < 3:
    print("You matched {} numbers so you dont have prize".format(count))
    exit()

prize = prizes[count]
print("You matched " + str(count) + " and your prize is: £" + str(prize))



# This is the first solution that I think before:

# if count < 3:
#     print("You matched {} numbers so you dont have prize".format(count))
# elif count == 3:
#     print("You matched {} numbers and your prize is £20".format(count))
# elif count == 4:
#     print("You matched {} numbers and your prize is £40".format(count))
# elif count == 5:
#     print("You matched {} numbers and your prize is £100".format(count))
# elif count == 6:
#     print("You matched {} numbers and your prize is £10000".format(count))
# elif count == 7:
#     print("You matched {} numbers and your prize is £100000".format(count))
# else:
#     print("You matched {} numbers so you dont have prize".format(count))