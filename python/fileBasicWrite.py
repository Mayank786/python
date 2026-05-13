file=open('/workspaces/codespaces-jupyter/python/report.txt','a')
file.write(' Hello World ab jo bhi likhoge wo add raha')
file.close()
# we can also use with statement to write/read file using with keyword
with open('/workspaces/codespaces-jupyter/python/report.txt','r') as file: #file ko read mode me open kiya
    content = file.read()
    print(content)
#with ke use se file automatically close ho jata hai jab hum uska kaam khatam kar lete hai
    