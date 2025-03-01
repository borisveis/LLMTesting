import json
import os
import subprocess

# Get the directory of the current file (utils.py)
current_dir = os.path.dirname(__file__)

# Construct the full path to config.json
config_path = os.path.join(current_dir, 'config.json')

# Load the config file
with open(config_path, 'r') as file:
    import json
    config = json.load(file)

model= config['testconfig']['model']
print("using model:"+model)
