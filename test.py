import importlib
import json
f = open("static/controls.json")
data = json.load(f)
import static.constants as constant

def qwe():
    importlib.reload(constant)
    

print(data["FULLSCREEN_SCALE"], constant.BUTTON_HEIGHT, sep=" - ")
print("------------")


if data["fullscreen"]:
    data["FULLSCREEN_SCALE"] = 2.5
else:
    data["FULLSCREEN_SCALE"] = 1
data["fullscreen"] = not data["fullscreen"]

with open("static/controls.json", "w") as jsonFile:     # чтобы было удобно
    json.dump(data, jsonFile)

qwe()

print(data["FULLSCREEN_SCALE"], constant.BUTTON_HEIGHT, sep=" - ")
