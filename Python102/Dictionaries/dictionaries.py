#simple Key Values
names_and_force_side = {
    "Luke" #key:"light"#value
}

name_and_animaltype = {  #THis is a dictionary
    "Buttercup":"cat"
    "Faith":"dog"
    "Tessa":"horse"
    "Ru":"Goat"
}
print(names_and_animaltype)


fav_foods = {   #this is a dictionary
    "coffee":["water", "coffee", "cream"]
    "roasted chicken": {   #dictionary within a dictionary
        "chicken":"dark meat", 
        "herb mix":["sage", "thyme", "salt", "pepper"], 
        "olive oil":"light" }
    "pizza":["mushrooms", "pineapple", "pine nuts", "cheese":["goat cheese", "feta", "mozzerella"]]
}



#access item in dictionary
print(fav_foods["coffee"][0]) #this prints "water"

#make a dictionary that has a dictionary inside

#if else
if "coffee" in fav_foods:
    print("Coffee is delicious.")
else:
    print("No coffee here.")

#label items
fav_foods["coffee"]["chicken"] = "All eaten"

fav_fav = fav_foods[0]
print(fav_fav)

#Replace an item in dictionary
fav_fav["coffee"] = "tea"