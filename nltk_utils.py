import os
import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize

# Setup for custom nltk_data directory
NLTK_DATA_PATH = os.path.join(os.path.dirname(__file__), "nltk_data")
os.makedirs(NLTK_DATA_PATH, exist_ok=True)
nltk.data.path.append(NLTK_DATA_PATH)

# Ensure punkt tokenizer is available
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', download_dir=NLTK_DATA_PATH)

stemmer = PorterStemmer()

def tokenize(sentence):
    """
    Split sentence into array of words/tokens
    A token can be a word or punctuation character, or number
    """
    return word_tokenize(sentence)

def stem(word):
    """
    Stemming = find the root form of the word
    Examples:
    words = ["organize", "organizes", "organizing"]
    words = [stem(w) for w in words]
    -> ["organ", "organ", "organ"]
    """
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, words):
    """
    Return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    """
    sentence_words = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words:
            bag[idx] = 1
    return bag
