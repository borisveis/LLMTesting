import json
import testFramwork
from gpt4all import GPT4All
import config
model = GPT4All(config.model)
#
# # entries = os.listdir('.')
responsestates = testFramwork.chat("how many states are in US", 100)
print("response:"+responsestates)
numberofstates = "I think there are 50"
print("cosine simularity score:")
print(testFramwork.validate.cosine_similarity_score(responsestates,numberofstates))
