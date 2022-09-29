str = input("Enter your word:")

count =1
for x in str:
  if count % 2 != 0:
    print(x)
  count = count+1