import json
import testFramwork
import pytest
from gpt4all import GPT4All
import config
model = GPT4All(config.model)
#
# # entries = os.listdir('.')
responsestates = testFramwork.chat("how many states are in US", 100)
print("AI:"+responsestates)
numberofstatesprompt = "There are 50 states"
print("cosine simularity score:")
cosinesimularity = testFramwork.validate.cosine_similarity_score(responsestates,numberofstatesprompt)
print(testFramwork.validate.cosine_similarity_score(responsestates, numberofstatesprompt))
def test_cosinesimularity():
        print("cosinesimularity="+str(cosinesimularity))
        assert cosinesimularity>0.6


# test asserting an arbitrary cosine sumularity score. As is, this is only for demonstration and example.
# It doesn't necessarily test much
assert cosinesimularity > 0.5


# a positive test validating  reponse contains specific strings is included in the response(s)
def test_contains():

        assert (responsestates.__contains__("United States") and (responsestates.__contains__("50")
                                                                  or responsestates.__contains__("fifty")))

#a positive test validating a specific string is not included in the respons(s)
def test_notcontains():
        prompt="what is robert half"
        rhiresponse = testFramwork.chat(prompt, 100)
        notcontain="financial"

        assert (not rhiresponse.__contains__(notcontain))
