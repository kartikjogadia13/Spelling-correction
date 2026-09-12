import os

import pandas as pd
import spacy
from nltk.metrics.distance import edit_distance


nlp = spacy.blank("en")


folder = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(folder, "spelling_dataset.csv")


df = pd.read_csv(dataset_path)

print(df.head())

vocab = set()

for word in df["correct"]:
    word = word.lower()

    if word.isalpha():
        vocab.add(word)

print("Vocabulary size:", len(vocab))


def correct_word(word):
    """Find the closest correct word from the vocabulary."""
    word_lower = word.lower()

    if len(word_lower) <= 3:
        return word

    if word_lower in vocab:
        return word

    best_word = word
    best_distance = 100

    for correct in vocab:
        distance = edit_distance(word_lower, correct)

        if distance < best_distance:
            best_distance = distance
            best_word = correct

    if len(word_lower) <= 5 and best_distance <= 1:
        return best_word

    if len(word_lower) > 5 and best_distance <= 2:
        return best_word

    return word


def correct_sentence(sentence):
    """Correct the words in a complete sentence."""
    doc = nlp(sentence)
    result = []

    for token in doc:
        word = token.text

        if word.isalpha():
            word = correct_word(word)

        result.append(word)

    return " ".join(result)


sentence = input("Enter a sentence: ")
corrected = correct_sentence(sentence)

print("Original:", sentence)
print("Corrected:", corrected)
