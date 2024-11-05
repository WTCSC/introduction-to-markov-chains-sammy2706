import random
import re

text = "As the sun dipped below the horizon, the sky erupted into a canvas of deep oranges and purples. The quiet rustle of the leaves seemed louder in the stillness of the evening, each breeze carrying the scent of pine and damp earth. In the distance, the soft chirping of crickets filled the air, while the first stars began to twinkle, scattered like tiny diamonds across the darkening sky."
transitions = {}
# Adds spaces around punctuation marks for better grammar
cleaned_text = re.sub(r"([.,!?;])", r" \1 ", text)
# Splits the cleaned text into individual words
words = cleaned_text.split()
for i in range(len(words) - 1):
    current_word = words[i].lower() # Converts current word into lower case to make sure it knows what is capital or not
    next_word = words[i + 1]
    if current_word not in transitions:
        transitions[current_word] = []
    transitions[current_word].append(next_word)

def generate_text(start_word, num_words, transitions):
    current_word = start_word
    result = [current_word]
    result = [current_word.capitalize()]
    for _ in range(num_words - 1):
        if current_word in transitions:
            next_word = random.choice(transitions[current_word])
            result.append(next_word)
            current_word = next_word
        else:
            current_word = random.choice(list(transitions.keys())) # Selects random word from all keys
            result.append(current_word) # Adds the randomly chose word to the result list
    return " ".join(result) # Once the loop is done, it joins the list of words into a single string with spaces and returns results

# User interface
start_word = input("Enter a starting word: ").strip()
num_words = int(input("How many words would you like to generate? "))

generated_text = generate_text(start_word, num_words, transitions)
print("\nGenerated Text:")
print(generated_text)