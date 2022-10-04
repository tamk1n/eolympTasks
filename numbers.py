filename = 'numbers.txt'

with open(filename) as file_object:
  numbers = file_object.readlines()
  numbers1 = []
  for item in numbers:
    item = item.rstrip()
    numbers1.append(item)
  #print(numbers1)
  new_nums = []

for i in range(0, len(numbers1)):
  for j in range(i+1, len(numbers1)):
    if numbers1[i] == numbers1[j]:
      new_nums.append(numbers1[i])
print(new_nums)

 #for digit in numbers:
  #if int(digit) % 2 != 0:
    #print(digit.rstrip())
