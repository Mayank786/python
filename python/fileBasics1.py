#how to read line by line from file
file = open('/workspaces/codespaces-jupyter/python/fileReading.txt', 'r')
for line in file:
    print(line)
file.close()

#another way to read line by line
with open('/workspaces/codespaces-jupyter/python/fileReading.txt', 'r') as file:
    line1=file.readline()
    line2=file.readline()
    print(line1)
    print(line2)

   # to see the number of lines in file
    with open('/workspaces/codespaces-jupyter/python/fileReading.txt', 'r') as file:
        data=file.readlines() #readlines method se file ke sare lines ek list me store ho jate hai
        print('number of lines in file:', len(data)) #then we used len function to count the number of lines in list