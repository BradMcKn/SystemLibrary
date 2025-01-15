#second step defining User Class
#had issues with the import removed the import 
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
#allows the user to borrow a book
    def borrow_book(self, book):
        message = book.borrow_book()
        if message == "Book is borrowed.":
            self.borrowed_books.append(book)
        return message
#allows the user to return the book
    def return_book(self, book):
        if book in self.borrowed_books:
            message = book.return_book()
            if message == "Book is returned, thank you!":
                self.borrowed_books.remove(book)
            return message
        return "This book was not borrowed by the user."
#allows the user to see what books they borrowed had issues wwith th return had to add self.borrwed_books to class
    def view_borrowed_books(self):
        return [str(book) for book in self.borrowed_books]

    def __str__(self):
        return f"{self.name} (user_id: {self.user_id})"
