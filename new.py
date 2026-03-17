from datetime import date

class person:

    def __init__(self, name ,country, date_of_birth):
        self.name =name
        self.country =country
        self.date_of_birth =date_of_birth

    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age
        

person1 = person("ayush","India",date(1962, 7, 12))
person2 = person("Shweta Maddox", "Canada", date(1982, 10, 20))
person3 = person("Elizaveta Tilman", "USA", date(2000, 1, 1))



print(person1)
print("name:",  person1.name)
print("country :",person1.country)
print("date of birth :",person1.date_of_birth)
print("age is :", person1.calculate_age())