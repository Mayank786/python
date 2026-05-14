#This program demonstrate how constructors are made and when then object is created they're called automatically.

class student():
    schoolName = "ABC School"
    def __init__(self):
        print("Constructor is called")
        print(self.schoolName)

s1=student() #when we create an object of the class student, the constructor is called and the message "Constructor is called" is printed. The constructor is a special method that is called when an object of the class is created. It is used to initialize the attributes of the class. In this case, the constructor initializes the attribute schoolName with the value "ABC School". 
        #the constructor is defined using the __init__ method. The __init__ method is a special method that is called when an object of the class is created. It is used to initialize the attributes of the class. In this case, the __init__ method initializes the attribute schoolName with the value "ABC School". The __init__ method takes self as a parameter, which is a reference to the current instance of the class. 
        # The self parameter is used to access the attributes and methods of the class.

s2=student() #when we create another object of the class student, the constructor is called again and the message "Constructor is called" is printed again. This shows that the constructor is called every time an object of the class is created.
print('school name of student1: ',s1.schoolName) #the school name of student1 is printed as "ABC School" as it is initialized in the constructor.

#self parameter is nothing but the object itself. It is used to access the attributes and methods of the class. It is a convention to use self as the name of the first parameter of the __init__ method, but you can use any name you want. The self parameter is automatically passed to the __init__ method when an object of the class is created. It is used to access the attributes and methods of the class. In this case, the self parameter is used to access the attribute schoolName and initialize it with the value "ABC School".