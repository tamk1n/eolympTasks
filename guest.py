filename = "guests.txt"

with open(filename, "a") as file_object:
    while True:
        name = input("Please enter your name:")
        if name == "q":
            break
        else:
            print(name)
            file_object.write(f"{name}\n")
    
