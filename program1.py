#WAP to create a person class. Include attributes like name,country and date of birth. Implement a method to determine the person's age.
class Person:
    def __init__(self, name, country, birthdate):
        self.name = name
        self.country = country
        self.birthdate = birthdate  
    def calculate_age(self):
        today_year = 2024  
        birth_year = int(self.birthdate.split('-')[0])
        age = today_year - birth_year
        return age
name = input("Enter name: ")
country = input("Enter country: ")
birthdate = input("Enter date of birth (YYYY-MM-DD): ")

person1 = Person(name, country, birthdate)
print(f"\nName: {person1.name}")
print(f"Country: {person1.country}")
print(f"Birthdate: {person1.birthdate}")
print(f"Age: {person1.calculate_age()} years")
