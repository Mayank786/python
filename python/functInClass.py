#This is an example of a class with a method inside it. 
# The method is called calc and it takes two parameters a and b, which have default values of 2 and 3 respectively. 
# The method returns the sum of a and b. The result of the calculation is stored in the variable result
#  which is a class variable. We create two instances of the fruit class
#  f1 and f2, with different names and colors. 
# Finally, we print the details of both fruits and the result of the calculation.

class fruit ():
    def __init__(self, name, color):
     self.name = name
     self.color = color
     #creating a method inside the class
    
    def calc(a=2, b=3):
        return a+b
    result = calc()

f1=fruit("apple", "red")
f2=fruit("banana", "yellow")
print('details of fruit1: ',f1.name, f1.color)
print('details of fruit2: ',f2.name, f2.color)
print('the result of the calculation is: ', fruit.result)