class Person:
    
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hi I am {self.name}")
    

person = Person("Ajay Thakur")
print(person.name)
person.talk()

person1 = Person("Abhay Thakur ")
print(person1.name)
person1.talk()
