def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(path_to_file):
    with open(path_to_file) as b:
        book_contents = b.read()
        word_list = book_contents.split()
        num_words = len(word_list)
    return num_words


def main():
    num_words = count_words("books/frankenstein.txt")
    print(f"{num_words} words found in the document")

    #book = get_book_text("books/frankenstein.txt")
    #print(book)

main()
