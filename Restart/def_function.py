from operator import concat


class Data():
    def __init__(self, Name, Age, Gender):
        print("Enter the name: {}", self.name)
        print("Enter age: {}", self.age)
        print("Male of Female? : {} ", self.gender)

Human = concat.Data()
print(Human)