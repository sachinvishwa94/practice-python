class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.age)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.ram = 16
            self.cpu = "i5"

        def show(self):
            print(self.brand, self.ram, self.cpu)

s1 = Student('sachin',24)
s2 = Student("vishwa", 25)


s1.show()