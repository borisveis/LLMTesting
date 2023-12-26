import json
from gpt4all import GPT4All
import config
model = GPT4All(config.model)
#
# # entries = os.listdir('.')
# # print(entries)
# testconfig = config['testconfig']
print(model.generate("hello world. My name is Boris", max_tokens=100))
print(model.generate("how do you say hello in french", max_tokens=100))

print(model.generate("how old are you`", max_tokens=50))
