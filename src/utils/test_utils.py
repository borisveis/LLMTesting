from src.utils import framework


def test_cos_sim():
    assert framework.cosine_similarity_score("abc","abc")==1