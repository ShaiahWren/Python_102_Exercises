# Create a program that asks for several numbers from a user and then adds them up. You must use a List.

# After the user enters a number it prints all the numbers the user has entered and ask for another number to be entered.
# Let the user know if they enter 0 it will do the addition. Then when they push enter it does the addition and prints the results.
# (Challenge) You cannot use an if statement.
# (Extra Challange)The only variables allow are "number", "numbers", and "result" (IE only 3 variables allowed and they are all named those specific things)
# (Extra Extra) do not have the List print with the 0 at the end of the list.
# my_list = []
# i = 0

# while i < 7:
#     number = int(input("Enter number:\n"))
#     my_list.append(number)
#     print(my_list)
#     i += 1
   

# FOR LOOP 
# thisList = []


# for i in range(0,7):
#     askNum = int(input("Pick a number: "))
#     thisList.append(askNum)
#     print(thisList)

# for i in range(0,len(thisList)):
#     num = thisList[i]
    
# sum_of_list = sum(thisList)
# print(sum_of_list)

#DYlan
# for i in range(0,7):
#     askNum = int(input("Pick a number: "))
#     thisList.append(askNum)
#     print(thisList)
# addemup = input("Enter '0' to add the numbers up: ")
# try:
#     addemup = "0"
#     sum_of_list = sum(thisList)
#     print(sum_of_list)
# except:
#     print("welp, see ya...")


#CLINT answer
number = None
num_list = []
result = 0

while number != 0:
    try:
        number = int(input("Give me a number to add. (Pressing 0 will do the addition)."))
    except:
        print("You must give a valid number")
    num_list.append(number)
    print(num_list)

for number in number:
    result = sum(num_list)
    print(result)
print(result)