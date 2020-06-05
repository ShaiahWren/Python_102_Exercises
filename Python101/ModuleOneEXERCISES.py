#Ex 1
#user_name = input("What is your name? ")
#print("Hello, %s!" % user_name)

#Ex 2
# name = input("What is your name?\n")
# string_length = len(name)
# greet = "Hello, %s" % name
# print(greet.upper())
# print("Your name has ", str(string_length), " letters in it." )

#Ex 3
# print("Please fill in the blanks below: \n_____(name)'s favorite food is _____(food))\n")
# name = input("Enter a name\n")
# print("%s"  % name)
# food = input("Enter a food\n")
# print("%s's favorite food is %s" % (name, food))

#Ex 4
# day = int(input("Day (0-6? "))
# if day == 0:
#     print("Sunday")
# elif day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# else:
#     print("That is not a number between 1 - 6")

# #Ex 5
# day = int(input("Day (0-6? "))
# if day == 0 or day == 6:
#     print("Sleep in")
# elif day >= 2 and day <= 5:
#     print("Go to work")
# else:
#     print("That is not a number between 1 - 6")

# #Ex. 6
# cel_num = input("Enter number in Celcius\n")
# far_num = int(cel_num) / 5 * 9 + 32
# far_symbol = "F"
# print(far_num, far_symbol)

# #Ex. 7
# counting = 1
# while counting <= 10:
#     print(counting)
#     counting += 1

#Ex. 8
# counting = 1
# user_num = input("Please inter a number between 1 and 10\n")
# while counting <= 10:
#     if int(user_num) < 1 or int(user_num) > 10:
#         print("That was not the instructions")
#         exit()
#     else:
#         print(counting)
#         counting += 1

# #Ex. 9
# print("*****\n")
# print("*****\n")
# print("*****\n")
# print("*****\n")
# print("*****\n")

# #Ex. 10
#My answer

# square_length = input("Please enter square length:\n")
# square_size = int(square_length) * int(square_length)
# print(square_size)


#Online answer
# side = int(input("Please Enter any Side of a Square: "))

# print("Square Number Pattern") 

# for i in range(side):
#     for i in range(side):
#         print('*', end = ' ')
#     print()

# MEDIUM

# Ex. 1


# try:
#     bill_amount = float(input(("Total bill amount?\n")))
# except ValueError:
#     print("Please enter a valid number.")
# service = (input("Enter service quality: good, fair, or bad\n")) 
# bad_service = float((bill_amount) * .1)
# bad_total = (bad_service) + bill_amount

# good_service = float((bill_amount) * .2)
# good_total = (good_service) + bill_amount

# fair_service = float((bill_amount) * .15)
# fair_total = (fair_service) + bill_amount

# if service == "good":
#     print("Tip amount:", '${:,.2f}'.format(good_service))
#     print("Total amount:", '${:,.2f}'.format(good_total))
# elif service == "bad":
#     print("Tip amount:", '${:,.2f}'.format(bad_service))
#     print("Total amount:", '${:,.2f}'.format(bad_total))
# elif service == "fair":
#     print("Tip amount:", '${:,.2f}'.format(fair_service))
#     print("Total amount:", '${:,.2f}'.format(fair_total))
# else:
#     print("Please enter good, bad, or fair")

#Ex. 2

# bill_amount = float(input(("Total bill amount?\n")))
# service = (input("Enter service quality: good, fair, or bad\n")) 
# split = int(input("Split how many ways?\n"))

# bad_service = float((bill_amount) * .1)
# bad_total = (bad_service) + bill_amount
# bad_split = bad_total / split

# good_service = float((bill_amount) * .2)
# good_total = (good_service) + bill_amount
# good_split = good_total / split

# fair_service = float((bill_amount) * .15)
# fair_total = (fair_service) + bill_amount
# fair_split = fair_total / split

# if service == "good":
#     print("Tip amount:", '${:,.2f}'.format(good_service))
#     print("Total amount:", '${:,.2f}'.format(good_total))
#     print("Amount per person:", '${:,.2f}'.format(good_split))
# elif service == "bad":
#     print("Tip amount:", '${:,.2f}'.format(bad_service))
#     print("Total amount:", '${:,.2f}'.format(bad_total))
#     print("Amount per person:", '${:,.2f}'.format(bad_split))
# elif service == "fair":
#     print("Tip amount:", '${:,.2f}'.format(fair_service))
#     print("Total amount:", '${:,.2f}'.format(fair_total))
#     print("Amount per person:", '${:,.2f}'.format(fair_split))
# else:
#     print("Please enter good, bad, or fair")


# Ex. 3
# try:
#     coins_wanted = input("Do you want coins?\n")
# except ValueError:
#     print("Must answer yes or no")

# coins = 0
# more_coins = "yes"

# while more_coins == "yes":
    
#     if coins_wanted == "yes":
#         coins += 1
#         print("You have %s coins." % coins)
#         more_coins = input("Do you want more coins?\n")
#         print(more_coins)
#     elif coins_wanted != "yes":
#         print("Bye")
#         exit()
#     if more_coins != "yes":
#         print("Bye")
#         exit()
#     else:
#         print("Enter yes or no")
    
        

# LARGE
# Ex. 4
# #My answer
# secret_number = 5
# greet = "I am thinking of a number between one and ten.\n"
# print(greet)
# ask_num = int(input("What is the number?\n"))

# while secret_number != ask_num:
    
    
#     if ask_num == secret_number:
#         print("Yes, You win")
#         exit()
#     if ask_num != secret_number:
#         ask_num = int(input("What is the number?\n"))
#         print("No, You Lose")
#         print(ask_num)
#     if int(ask_num) < 1 or int(ask_num) > 10:
#         print("Please enter a number between 1 and 10")
#     else:
#         print(ask_num)


   
user = input("Username:\n")
password = ""

while True:
    password = input("Password:\n")
    valid = True
    if len(password) < 6:
        valid = False
        print("Too short.")
    elif len(password) > 12:
        print("Too long.")
        valid = False
    if valid == True:
        break

confirm_password = ""
while True:
    confirm_password = input("Confirm password:\n")
    if confirm_password == password:
        print("Success!")
        break
    else:
        print("Passwords must match.\n")



#"%.2f" %  ##dollar sign