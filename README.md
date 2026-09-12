# Spelling Correction Mini Project

A simple Python program that corrects spelling mistakes in a word or sentence using a small CSV dataset.

## Features

- Reads correct spellings from a CSV dataset
- Accepts a sentence from the user
- Finds the closest correct spelling using edit distance
- Prints the original and corrected sentence

## Technologies Used

- Python
- Pandas
- spaCy
- NLTK

## Files

- `spelling_correction.py` - Main Python program
- `spelling_dataset.csv` - Dataset containing incorrect and correct spellings

## Installation

Install the required libraries in the VS Code terminal:

```bash
pip install pandas spacy nltk
```

## How to Run

1. Open the project folder in VS Code.
2. Open the VS Code terminal.
3. Run the following command:

```bash
python spelling_correction.py
```

4. Type a sentence when the program asks for input.

## Example

```text
Enter a sentence: I recieve a seperate adress
Original: I recieve a seperate adress
Corrected: I receive a separate address
```

## Note

This is an academic mini project created to demonstrate basic natural language processing and spelling correction in Python.
