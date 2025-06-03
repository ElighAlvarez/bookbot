from stats import get_word_count
from stats import get_char_counts

def get_book_text(file_path):
    book_text = ""
    with open(file_path) as f:
        book_text = f.read()
    return book_text

def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(text)
    char_counts = get_char_counts(text)
    print(f"{word_count} words found in the document")
    print(char_counts)

main()
