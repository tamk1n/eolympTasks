class User:
    def __init__(self, f_name, l_name, age):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
    
    def desc_user(self):
        print(f"This user's first name is {self.f_name} and last name is {self.l_name}. He is {self.age} years old.")

user0 = User("Tamkin","Tamrazli", 23)

user0.desc_user()
