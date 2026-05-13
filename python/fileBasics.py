
#To open file in read mode
file = open('/workspaces/codespaces-jupyter/python/Test.txt', 'r') 
# To read the data in file and store it in variable
data=file.read()
data=data.lower()
#print(data)
if 'thanks' in data:
    print('thanks is present in file')
else:    print('thanks is not present in file')
#To close the file
file.close()
