Links and documentation
· https://gpt4all.io/index.html

https://github.com/borisveis/LLMTesting

Installation
Download and install GPT4all from  link above.
Follow on screen instructions to install bre-built model such as Mistral OpenOrca and/or Falcon GPT4all
Open application and confirm basic functionality by entering a greeting like "hello" into the prompt at the bottom of the application.
Prepare Python environment
Clone and/or fork my github repo

https://github.com/borisveis/LLMTesting
pip install -r ./requirements.txt
Included in requirements.txt:

pip install GPT4All
pip install sklearn
pip install sentence-transformers
pip install TfidfVectorizer
pip install sentence_similarity
pip install cmake
gpt4all must remain running for the Python SDK to work.

Testing strategies:

There are many strategies for testing and validating LLMs depending on their intended use case. I've implemented a cosine similarity method in the testFramwork module to test the simularity of a known value to the LLM's response. There are countless other strategies to test LLMs. Going through them is outside the scope of this article.

Here's one source I've found useful

https://www.packtpub.com/article-hub/testing-large-language-models-llms



As initial conditions of each environment are unique, please let me know if you find these instructions inaccurate or incomplete for your specific environment.

Configure model to use in src/utils/config.json
    note, model must be installed in the GPT4all default directory. 