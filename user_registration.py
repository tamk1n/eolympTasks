new_users = ["Tamkin", "Ramil", "Gasim", "Eyvaz"]
users=[]

while len(new_users) !=0:
  user = new_users.pop()
  users.append(user)

users.sort(reverse=True)
print(f" Registered users: {users}")