from stats import word_counter

def main():
    count_words = 0
    book_as_string = get_book_text("books/frankenstein.txt")
    num_words = word_counter(book_as_string)
    # count_words += len(split_words)
    # print(count_words)
    print(f"Found {num_words} total words")


def get_book_text(file_path):
    with open(file_path) as f:
       return f.read()
  
main()
