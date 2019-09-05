class Student:
    # school = static variable
    school = "Lala Land"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

 #avg(self) is Instance Method as we are calling instance variables from instance method
    def avg(self):
        return (self.m1+self.m2+self.m3)/3


#instanec type mutator method which is used to change the values of variable
    def set_m1(self, value):

        self.m1 = value

    # (classmethod is a DECORATOR)
    @classmethod
    def info(cls):
        return cls.school

    #Decorator for staic method
    @staticmethod
    def its_static_method():
        print("Staic method will not take self nor cls as parameter")

s1 = Student(45,76,87)
s2 = Student(43,79,47)
print(Student.its_static_method())