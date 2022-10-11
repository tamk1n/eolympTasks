import json 

filename = "username.json"

try:
  with open(filename) as f:
    username = json.load(f)
except FileNotFoundError:
  username = input("Please, enter your username:")
  with open(filename, "w") as f:
    json.dump(username, f)
    print(f"We will remember your username, {username}")
else:
  print(f"Welcome back, {username}")
    