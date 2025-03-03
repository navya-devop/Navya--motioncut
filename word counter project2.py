from collections import Counter
import re
def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower()) 
    return len(words), Counter(words)
if __name__ == "__main__":
    input_text = input("Enter the text: ")
    total_words, word_frequency = count_words(input_text)
    print(f"The total number of words in the given text is: {total_words}")
def count_letters(text):
    letter_count = 0
    for char in text:
        if char.isalpha():
            letter_count += 1
    return letter_count
if __name__ == "__main__":
    total_letters = count_letters(input_text)
    print(f"The total number of letters in the given text is: {total_letters}")
