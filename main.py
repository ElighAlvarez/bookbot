from stats import get_word_count
from stats import get_char_counts
from stats import sort_counts
import sys

def get_book_text(file_path):
    book_text = ""
    with open(file_path) as f:
        book_text = f.read()
    return book_text



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    word_count = get_word_count(text)
    char_counts = get_char_counts(text)
    sorted_counts = sort_counts(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Word Count ----------")
    for char_dict in sorted_counts:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["count"]}")
    print("============= END ===============")

main()
