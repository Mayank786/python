#create a class called laptop with attributes brand, price and RAM. 
#Then create two objects of the class laptop and assign values to the attributes of each object. Finally, print the attributes of each object.

#creating a class
class laptop:
    brand = "default"
    price = 50000 #These are class variables also called attributes and they are shared by all the objects of the class
    RAM = "default"

#creating objects of the class
laptop1=laptop()
laptop1.brand="Dell"
laptop1.price=60000 #here the value of price is changed as it overrides the class variable price for the object laptop1. This is called instance variable and it is specific to the object laptop1.
laptop1.RAM="16GB"

laptop2=laptop()
laptop2.brand="HP"
laptop2.price=55000 #here the value of price is changed as it overrides the class variable price for the object laptop2. This is called instance variable and it is specific to the object laptop2.
laptop2.RAM="8GB"

print('details of laptop1: ',laptop1.brand, laptop1.price, laptop1.RAM)
print('details of laptop2: ',laptop2.brand, laptop2.price, laptop2.RAM)