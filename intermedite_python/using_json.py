import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

with open("pres.json", "w") as json_write:
    json.dump(data, json_write)

json_string = json.dumps(data, indent=2)

print(json_string)

json_obj = json.loads(json_string)
print(json_obj)

with open("pres.json", "r") as json_read:
    json_obj = json.load(json_read)

print(json_obj)
