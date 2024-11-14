import string

def read_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return text

def clean_and_tokenize(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return words

def count_words(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def display_top_words(word_count, n):
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    for i, (word, count) in enumerate(sorted_word_count[:n], start=1):
        print(f"{i}. {word}: {count}")

def main():
    filename = "input.txt"  # Change this to the name of your input text file
    top_n = 10

    text = read_file(filename)
    words = clean_and_tokenize(text)
    word_count = count_words(words)
    print(f"Top {top_n} most frequent words:")
    display_top_words(word_count, top_n)

if __name__ == "__main__":
    main()