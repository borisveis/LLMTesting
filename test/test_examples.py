
from gpt4all import GPT4All
from src.utils import framework
from src.utils import config

model = GPT4All(config.model)

response_states = framework.chat("how many states are in US", 100)
expected_number_of_states_response = "There are 50 states"
# cosinesimularity = framework.cosine_similarity(responsestates,expected_number_of_states_response)
def test_cosinesimularity():
        assert framework.cosine_similarity_score(response_states, expected_number_of_states_response) > 0.5


# a positive test validating  reponse contains specific strings is included in the response(s)
def test_contains():

        assert (response_states.__contains__("United States") and (response_states.__contains__("50")
                                                                   or response_states.__contains__("fifty")))

#a positive test validating a specific string is not included in the respons(s)
def test_notcontains():
        prompt="what is robert half"
        rhiresponse = framework.chat(prompt, 100)
        notcontain="financial"

        assert (not rhiresponse.__contains__(notcontain))
