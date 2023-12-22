from gpt4all import GPT4All
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
print(model.generate("hello world", max_tokens=100))
print(model.generate("how do you say hello in french", max_tokens=100))
print(model.generate("how old are you`", max_tokens=50))
