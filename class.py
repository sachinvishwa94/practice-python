class person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def my_function(self):
        print("my name is", self.name, "and my age is", self.age, "whereas I live in", self.address)


p1 = person("Sachin Vishwakarma", 25, 'Patna')
p1.my_function()
p2 = person("python", "30", "computers")
p2.my_function()
