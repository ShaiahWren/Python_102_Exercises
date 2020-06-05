# description = ["loving", "kind", "nerf herder", "funny"]

# print(description)

# description[2] = "Who's a nerf herder?"
# description[3] = "Master Pilot"
# print(description)

# REMOVE AND REPLACE
# description = ["Dolt", "Slow", "Easy-going", "Good friend"]
# print(description)

# modifications = ["Great", "Perfect", "Loving"]

# print(description[1:3])

# description[1:3] = modifications

# print(description[1:3])

# ADD TO LIST
description = ["Dolt", "Slow", "Easy-going", "Good friend"]
print(description)

modifications = ["Great", "Perfect", "Loving"]

print(description[1:3])

description[1:3] = modifications

print(description[1:3])

#DELETE LAST ITEM
del description[len(description)-1]
print(description)

description.append("Cool-looking")
print(description)

#ADD LIST TO LIST

extra = "Jolly", "Fatigued"
description.extend(extra)
print(description)

description.extend(["Jolly", "Fatigued"])


#LISTS
parts = [
    "arm",
    "leg",
    "Knee",
    "Shoulder",
    "foot",
    "ankle",
]
print(parts)

#POP
removed_part = description.pop(0)
print(removed_part)
print(description)

