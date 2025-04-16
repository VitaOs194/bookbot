import sys
from stats import get_num_words, count_characters, chars_to_sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)

    print("=======BOOKBOT=======")
    print(f"Analyzing book found at {path}...")

    word_count = get_num_words(text)
    print(f"Found {word_count} total words")

    char_count = count_characters(text)
    sorted_chars = chars_to_sorted_list(char_count)

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")

main()

