import json
import testFramwork
from gpt4all import GPT4All
import config
model = GPT4All(config.model)
#
# # entries = os.listdir('.')
responsestates = testFramwork.chat("how many states are in US", 100)
print("response:"+responsestates)
numberofstates = "There are 50 states"
print("cosine simularity score:")
cosinesimularity = testFramwork.validate.cosine_similarity_score(responsestates,numberofstates)
print(testFramwork.validate.cosine_similarity_score(responsestates,numberofstates))
def test_cosinesimularity():
        print("cosinesimularity="+str(cosinesimularity))
        assert cosinesimularity > 0.5