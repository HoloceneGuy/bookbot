from stats import count_chars, count_words, sort_dictionaries

def main():
    path_to_book = "books/frankenstein.txt"
    text = get_book_text(path_to_book)
    num_chars = count_chars(text)
    num_words = count_words(text)
    sorted_dict = sort_dictionaries(num_chars)
    print_report(path_to_book, num_chars, num_words, sorted_dict)

def get_book_text(path_to_file):
    with open(path_to_file) as b:
        book_contents = b.read()
    return book_contents

def print_report(path_to_book, num_chars, num_words, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for listed_dictionary in sorted_dict:
        if listed_dictionary["char"].isalpha():
            print(f"{listed_dictionary["char"]}: {listed_dictionary["num"]}")
    print("============= END ===============")

main()
