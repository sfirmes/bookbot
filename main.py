def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    letters_dict = get_letters_dict(book_text)
    
    letters_sorted_list = letters_dict_to_sorted_list(letters_dict)

    for item in letters_sorted_list:
        if not item['character'].isalpha():
            continue
        print(f"The '{item['character']}' character was found {item['num']} times")
    

def get_book_text(path):
    with open(path) as book:
        return book.read()
    

def get_letters_dict(book_text):
    characters = {}
    for character in book_text:
        lowered = character.lower()
        if lowered in characters:
            characters[lowered] +=1
        else:
            characters[lowered] = 1
    return(characters)

def letters_dict_to_sorted_list(letters_dict):
    sorted_list = []
    for character in letters_dict:
        sorted_list.append({"character": character, "num": letters_dict[character]})
    sorted_list.sort(reverse=True, key=sort_on_key)
    return(sorted_list)

'''def sort_on_key(which_key):
    which_key=["num"]
    return which_key'''

def sort_on_key(which_key):
    return which_key["num"]


main()