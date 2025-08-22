from stats import count_chars, count_words, sort_dictionaries

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
   
    num_chars = count_chars("books/frankenstein.txt")
    #print(num_chars)
    
    num_words = count_words("books/frankenstein.txt")
    #print(f"{num_words} words found in the document")

    sorted_dict = sort_dictionaries(num_chars)
    print(sorted_dict)

    #book = get_book_text("books/frankenstein.txt")
    #print(book)

main()
