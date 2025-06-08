# Purpose: To read the words2 file an converts all words to lowercase
# and then writes them to a new dictionary whose keys are the lowercase letters
# and values are lists of words starting with that letter.

f = "words2.txt"
word_dict = {}

# Open the file and read the words into a list
def read_words():
    words = []
    with open(f, "r") as file:
        for line in file:
            line = line.replace("\n", "")
            words.append(line)
    return words

# List the words in alphabetical order and print to screen in a numbered list
def list_words(words):
    for i, word in enumerate(sorted(words)):
        print(f"{i}.{word}")
    print()

# Write the words to a dictionary in alphabetical order aligned in two columns and print to screen
# e.x. a - ['apple', 'ant', 'apricot'] do not duplicate
def write_words(words):
    words_dict = {}
    words = sorted(words)  # Sort the words in alphabetical order
    for word in words:
        word = word.lower().strip()
        key = word[0]  # Get the first letter of the word
        key = key.lower() # Ensure the key is lowercase
        if key in words_dict:
            if word not in words_dict[key]: # Check for the key and if the word is already in the dictionary
                words_dict[key].append(word) 
        elif key not in words_dict:
            if word not in words_dict: # Check if the word is not in the dictionary of the key and add it if it is not
                words_dict[key] = [word]
    for key in sorted(words_dict.keys()):
        print(f"{key} - {words_dict[key]}") # Print to console


def main():
    words = read_words()  # Read the words from the file
    list_words(words)  # List the words in alphabetical order
    write_words(words)  # Write the words to a dictionary and print them

if __name__ == "__main__":
    main()
