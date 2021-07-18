import json
f = open("build.json", "r")
bSystem = json.load(f)

output = '''
import json
app_name="{}"
f = open("build.json", "r")
bSystem = json.load(f)

dependencies = bSystem[app_name]["dependency"]

output = ""
print("Building File:", app_name)

for dep in dependencies:
    f = open(dep+".txt","r")
    output += f.readline() + " "
    f.close()
    
f = open(app_name+".txt","w")
f.write(app_name)
f.close() 
'''
for file in bSystem.keys():
    f = open(file+".py","w")
    f.write(output.format(file))
    f.close()