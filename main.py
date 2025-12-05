from stats import word_counter
from stats import character_counter
from stats import sort_chars


def main():
    book_as_string = get_book_text("books/frankenstein.txt")
    num_words = word_counter(book_as_string)
    num_characters = character_counter(book_as_string)
    sorted_chars = sort_chars(book_as_string)
    # count_words += len(split_words)
    # print(count_words)
    print(f"Found {num_words} total words")
    print(num_characters)


def get_book_text(file_path):
    with open(file_path) as f:       
       return f.read().lstrip("\ufeff")
  
main()
