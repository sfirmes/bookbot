def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    letters_dict = get_letters_dict(book_text)
    print(letters_dict)

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

main()