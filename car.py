class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def describe_car(self):
        long_name = f"{self.name} {self.model} {self.year}"
        return long_name
    
    def odometer_reader(self):
        print(f"This car's odometer reader is {self.odometer_reading}")

    def update_odometer(self, mil):
        self.mil = mil
        if mil >= self.odometer_reading:
            self.odometer_reading = self.mil
        else:
            print("You can't roll odometer back")
        new_mil = f"Car's odometer reader has been updated to {self.odometer_reading}"
        return new_mil

new_car0 = Car("Volkswagen", "Jetta", 1999)

new_car0.odometer_reading =2000

print(new_car0.describe_car())
new_car0.odometer_reader()
print(new_car0.update_odometer(3000))

