people = []

for i in range(5):
  person ={}
  person["first_name"] = input("Enter your first name:")
  print(person["first_name"])
  person["last_name"] = input("Enter your last name:")
  print(person["last_name"])
  person["age"] = input("Enter your age:")
  print(person["age"])
  print(person)
  people.append(person)
for person in people:
  for k, v in person.items():
    print(f"{k}:{v}")
  print("\n")

