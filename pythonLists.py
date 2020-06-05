# han_description = ['stuck-up, 'half-witted', 'scruffy-looking', 'nerf herder']
# mylist = [1, 2, 3, 4, 5]


# lukes_real_hands = ["left"]
# like_jar_jar = []

# print(han_description[0])
# print(lukes_real_hands[0])
# print(people_who_like_jar[100]

# try:
#     print(people_who_like_jar)
# except ValueError:
# print(han_description[-1])
# print(han_description[1:3])

# #WHile loop through list (array)
# han_description = ['stuck-up, 'half-witted', 'scruffy-looking', 'nerf herder']
# list_size = len(han_description)
# index = 0
# print("Why you:")
# while index < len(hand_description)
#     print("%d, %s % (index+1, han_description[index]")
#     index += 1
# for descriptor in han_description:
#     print(descriptor)



# Create a program that lists your top 3 favorite foods.
# You can only write a single print statement.
# The list must have at least 5 items.

# fav_food = ["raspberries", "blueberries", "strawberries", "tomato", "spaghetti"]
# #print(fav_food[0:3])

# index = 0
# while index < len(fav_food):
#     print("%d, %s %(index+1, fav_food[index]")
#     index +- 1


# Create a program that prints out the results from a list.
# You can only have one viarable in the whole program
# It can only be on two lines

# print([])


# Create a program that lists your top 3 favorite foods.
# You can only write a single print statement.
# The list must have at least 5 items.

fav_food = ["raspberries", "blueberries", "strawberries", "tomato", "spaghetti"]
counter = 1
for descriptor in fav_food:
    # print(counter, '.' descriptor)
    print("%d. %s" % (counter, descriptor))
    length = len(fav_food)
    if counter < length:
        print("There next one up is %s" % fav_food[counter])
    
    counter += 1