#first step 
#defining book class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
#return string of book
    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
#marks if the book is borrowed if its available if book is borrowed should return message "Book is already checked out!"
    def borrow_book(self):
        if self.available:
            self.available = False
            return "Book is borrowed."
        return "Book is already checked out!"
#marks book as returned if book was never borrowed "Book was not borrowed. Please try again."
    def return_book(self):
        if not self.available:
            self.available = True
            return "Book is returned, thank you!"
        return "Book was not borrowed. Please try again."
