import json
pathToFile = "C:\\Users\\nikki\\Downloads\\student.json"
with open(pathToFile, "r") as file:
    jsonStr = file.read()
data = json.loads(jsonStr)
rename = data["name"] = "Nicole"
with open(pathToFile, "w") as file:
    file.write(rename)