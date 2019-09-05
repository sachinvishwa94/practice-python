class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_function(self):
        print(self.name, self.age)


class Student(Person):

    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.year = year

    def Studentname(self):

        print('hello', self.name,"welcome", self.year, "at age of", self.age)


x = Student("sachin", 25, 2019)
x.Studentname()

y = Student('construal', 24, 2018)
y.Studentname()

z = Student("sachin", 25, 2018)
z.Studentname()
