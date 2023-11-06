def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(count_words(book_text))

def get_book_text(path):
    with open(path) as book:
        return book.read()
    
def count_words(text_line):
    words = text_line.split()
    return(len(words))

main()