def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(count_words(book_text))

def get_book_text(path):
    with open(path) as book:
        return book.read()
    
def count_words(book_text):
    words = book_text.split()
    return(len(words))

main()