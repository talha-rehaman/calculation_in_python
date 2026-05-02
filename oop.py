# class person:
#     lastName = "Smith"
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
# p1 = person("John", 36)
# person.lastName = "Refsnes"
# print(person.lastName)
        
class person:
    def __init__(self,name):
        self.name = name
    def greet(self):
        print("Hello, my name is " + self.name)
p1 = person("John")
p1.greet()