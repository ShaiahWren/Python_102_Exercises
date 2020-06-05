#nested if

first_name = "Shaiah"
last_name = "Wren"

if first_name == "Shaiah":
    print("My name is %s" % first_name)

    if len(last_name) < 8:
        print("My last name is %s" % last_name)
    elif last_name == "Wren":
        print("Yo I already said my last name.")
    else:
        print("I don't know where I am.")

    