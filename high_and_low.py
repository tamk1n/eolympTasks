def high_and_low(numbers):
  numbersList = []
  newnum =""
  
  for i in range(0,len(numbers)): 
    if numbers[i] != " ":
      newnum +=numbers[i]
      if i ==len(numbers)-1:
        numbersList.append(int(newnum))
    elif numbers[i] == " ":
      numbersList.append(int(newnum))
      newnum =""
  
  numbersList.sort(reverse=True)

  return f"{numbersList[0]} {numbersList[len(numbersList)-1]}"
