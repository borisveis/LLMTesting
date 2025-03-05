from src.utils import framework, config


# framework methods
def test_cos_sim():
    assert framework.cosine_similarity_score("abc", "abc") == 1
    assert framework.cosine_similarity_score("my name is Mike", "my name is Don") < 1


def test_chat():
    prompt1 = "how many states in usa?"
    response = framework.chat(prompt1, 10)
    assert response.__contains__("50 states")
        # config methods
    print(config.get_default_model_name())
    assert config.get_default_model_name() is not None
