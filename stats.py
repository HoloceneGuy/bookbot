import string

def count_words(path_to_file):
    with open(path_to_file) as b:
        book_contents = b.read()
        word_list = book_contents.split()
        num_words = len(word_list)
    return num_words

def count_chars(path_to_file):
    char_dict = {}

    with open(path_to_file) as book:
        book_contents = book.read()
        book_chars = list(book_contents.lower())
        checking_chars = list(string.ascii_lowercase + " ")
        for character in book_chars:
            if character in checking_chars:
                char_dict.setdefault(character, 0)
                char_dict[character] += 1

    return char_dict

def sort_dictionaries(char_dict):
    listed_char_dicts = []
    for key in char_dict:
        counted_character = {"char":key, "num":char_dict[key]}
        listed_char_dicts.append(counted_character)

    return listed_char_dicts

#def sort_on(items):
#    return items["num"]

