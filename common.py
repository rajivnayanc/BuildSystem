import json
def export(app_name):
    f = open("build.json", "r")
    bSystem = json.load(f)
    dependencies = bSystem[app_name]["dep"]
    output = ""
    print("Building File:", app_name)
    for dep in dependencies:
        f = open(dep+".txt","r")
        output += f.readline() + " "
        f.close()
    f = open(app_name+".txt","w")
    f.write(app_name+"->" +  output)
    f.close()