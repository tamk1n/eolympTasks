import itertools
def get_pins(observed):
  a = []
  new = []
  for x in str(observed):
    if x == "0":
      new.extend(["0","8"])
      a.append(new)
    elif x == "1":
      new.extend(["1","2","4"])
      a.append(new)
    elif x == "2":
      new.extend(["1","2","3","5"])
      a.append(new)
    elif x == "3":
      new.extend(["2","3","6"])
      a.append(new)
    elif x == "4":
      new.extend(["1","4","5","7"])
      a.append(new)
    elif x == "5":
      new.extend(["2","4","5","6","8"])
      a.append(new)
    elif x== "6":
      new.extend(["3","5","6","9"])
      a.append(new)
    elif x == "7":
      new.extend(["4","7","8"])
      a.append(new)
    elif x == "8":
      new.extend(["0","5","7","8","9"])
      a.append(new)
    elif x == "9":
      new.extend(["6","8","9"])
      a.append(new)
    new =[]
      
  b = list(itertools.product(*a))

  newa=[]
  for tuple in b:
    new = "".join(tuple)
    newa.append(new)
  return newa

print(get_pins(369))
      


    