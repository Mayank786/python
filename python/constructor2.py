
class student():
        def __init__(self, name, age):
        #now we are passing two parameters name and age to the constructor. 
        # The __init__ method takes self as the first parameter, which is a reference to the current instance of the class. 
        # The name and age parameters are used to initialize the attributes of the class. 
        # The self parameter is used to access the attributes of the class and initialize them with the values passed as parameters.    
            self.name = name
            self.age = age

s1=student('Radhe', 20) 
s2=student('Shyam', 22)
print('details of student1: ',s1.name, s1.age)
print('details of student2: ',s2.name, s2.age)