from gpt4all import GPT4All
import src.utils.config as config
model = GPT4All(config.model)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def chat(prompt, maxtokens):
    return model.generate(prompt, max_tokens=100)
def cosine_similarity_score(sentence1, sentence2):
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([sentence1, sentence2])
        similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
        return similarity
