import json
import os
import subprocess

# Open the JSON file
with open('config.json', 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)

model= data['testconfig']['model']
print("using model:"+model)
