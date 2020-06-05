#Create a program that asks for a number between 10 - 101. 
#If the user enters anything that is not a number, or is less than 10 or greater than 101 throw some sort of insult.
#If the number is 42 print a very positive message.
#If the number -1 disregaurd the first point and print a message about being a smart person.
#Any other print a message that includes the number given.

#My answer
number_input = input("Give me a number between 10 - 101")
if number_input < 10 or number_input > 101:
    if number_input == -1:
        print('You are super smart!!')
    else:
        print('%s is no good, try a number between 10 and 101' % number_input)

    
if number_input == 42:
    print("Great answer!")

#Clint answer
number = input("Please give a number between 10 and 101 \n")

try:
    number = int(number)
except ValueError:
    print('This is wrong yo.')
    exit()
if number == -1:
    print("Clever!")

if number < 10 or number > 101:
    print('This is not in the instructions!')
    exit()
elif number == 42:
    print('You have read hitchhikers!')
else: 
    print('You followed instructions. %s was your number.' % number)



#Create a program that ask for 2 numbers and then divides the first number from the second number.
#Handle any possible errors without using any 'if'.
#If the result is a valid option, print "The result is X" where X is the value.
#Otherwise give an error that describes the issue.
#(challange) Still without using if. Let the user know which value is causing and exemption.
#(Extra Challange) Still without using ifs, If the first or second value is not a valid integer, have the program keep asking UNTIL the user supplies a valid integer. (think about the bolded word)


#Clint answer
number_one = int(input("Give me a number\n"))
number_two = int(input("Give me another number\n"))
try:
    number_one = int(input("Give me a number\n"))
    number_two = int(input("Give me another number\n"))
except ValueError:
    print('You entered a text')
    exit()
print(number_one/number_two)


