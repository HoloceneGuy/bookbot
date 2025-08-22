import string

def count_words(text):
    char_list = text.split()
    num_words = len(char_list)
    return num_words

def count_chars(text):
    char_dict = {}

    for character in text:
        lowered = character.lower() #
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict

### Old way still using a raw path to the book and converting to the text within the function
#def count_chars(path_to_file):
#    char_dict = {}
#
#    with open(path_to_file) as book:
#        book_contents = book.read()
#        book_chars = list(book_contents.lower())
#        checking_chars = list(string.ascii_lowercase + " ")
#        for character in book_chars:
#            if character in checking_chars:
#                char_dict.setdefault(character, 0)
#                char_dict[character] += 1
#
#    return char_dict

def sort_on(items):
    return items["num"]

def sort_dictionaries(char_dict):
    listed_char_dicts = []
    for key in char_dict:
        counted_character = {"char":key, "num":char_dict[key]}
        listed_char_dicts.append(counted_character)
    
    listed_char_dicts.sort(reverse=True, key=sort_on)

    return listed_char_dicts
