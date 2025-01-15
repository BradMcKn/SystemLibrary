# Third step  had to add a catalog with known books but needed to import book module here.
from book import Book

# Book catalog list of books by my favorite author as preset primamters to be able to be looked up in the search section
book_catalog = [
    Book("The Way of Kings", "Brandon Sanderson", "9780765326354"),
    Book("Words of Radiance", "Brandon Sanderson", "9780765326355"),
    Book("Oathbringer", "Brandon Sanderson", "9780765326356"),
    Book("Rhythm of War", "Brandon Sanderson", "9780765326357"),
    Book("Wind and Truth", "Brandon Sanderson", "9780765326358")
]

# allows the user to search for a book in the catalog by title, author, and isbn. added this because in real world most people may not know one of the three felt it would be easier to
# add a search for all three.
def find_book(search_term, search_by="title"):
    for book in book_catalog:
        if search_by == "title" and book.title.lower() == search_term.lower():
            return book
        elif search_by == "author" and book.author.lower() == search_term.lower():
            return book
        elif search_by == "isbn" and book.isbn == search_term:
            return book
    return None

# allows the user to search by author name, added .lower to make search easier so it is not cap sensitive
def find_books_by_author(author_name):
    books_by_author = []
    for book in book_catalog:
        if book.author.lower() == author_name.lower():
            books_by_author.append(book)
    return books_by_author

# defining the add_book_to_catalog() allows the user to add a book to catalog they will need to provied title, author, and isbn
def add_book_to_catalog():
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    isbn = input("Enter the book ISBN: ")
    new_book = Book(title, author, isbn)
    book_catalog.append(new_book)
    print(f"Book '{title}' by {author} added to the catalog.")

# def search allows the user to input the search and it to display output of book and availability
def search_and_display_books():
    search_by = input("Search by (title, author, isbn): ").lower()
    search_term = input("Enter search term: ")

    if search_by == "author":
        books = find_books_by_author(search_term)
        if books:
            print(f"Books by {search_term}:")
            for book in books:
                print(f"  - {book.title} (ISBN: {book.isbn}) - "
                      f"{'Available' if book.available else 'Not Available'}")
        else:
            print(f"Sorry, we couldn't find any books by {search_term}.")
    else:
        book = find_book(search_term, search_by)
        if book:
            print(f"{book.title} - {'Available' if book.available else 'Not Available'}")
        else:
            print(f"Sorry, we couldn't find a book with that {search_by}.")
