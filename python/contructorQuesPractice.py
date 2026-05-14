#create a class student with constructor which takes three parameters 
# and calculate the average of three subjects marks

class student():
    def __init__(self, maths, science, biology):
        self.maths = maths
        self.science = science
        self.biology = biology

    def average(self):
        return (self.maths + self.science + self.biology) / 3
#here class ends now we will create an object of the class student
s1=student(80, 90, 85)
print('Each subject marks of student1: ',s1.maths, s1.science, s1.biology)
print('Average marks of student1: ', s1.average())