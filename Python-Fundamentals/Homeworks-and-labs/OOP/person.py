class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age


jack = Person("Jack", 20)
peter = Person("Peter", 12)

print(peter.name)
print(peter.age)