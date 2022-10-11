letter = input("Enter pipe letter:")
letter = letter.upper()

fir  = input("Enter first number:")
r1 = int(fir)
sec = input("Enter second number:")
r2 = int(sec)

filename = "irc.txt"
with open(filename, "w") as file_object:
  while r1 < r2+1:
    print(f"{letter}{r1},")
    file_object.write(f"{letter}{r1},")
    r1+=1

  
