#Final step main bring it all together.
# imported from user and catalog orginaly had just import book.py, user.py. catalog.py but ran into issues.
#had to drop the import book.py and added catalog impor add book, search display book, and find book.
from user import User
from catalog import add_book_to_catalog, search_and_display_books, find_book
import catalog

# had to add this due to issues with storing objects mainly the add and removel of users.
user_db = {}

# allows the prompt to create new user and user id
def create_new_user():
    name = input("Please enter your name: ")
    user_id = input("Please create your user ID: ")
    if user_id in user_db:
        print(f"User ID '{user_id}' already exists. Please choose a different user ID.")
    else:
        user_db[user_id] = User(name, user_id)
        print(f"User '{name}' with ID '{user_id}' created successfully.")

# this list out user that are created on the library.
def list_users():
    if not user_db:
        print("No users found.")
    else:
        print("List of users:")
        for user_id, user in user_db.items():
            print(f"  - {user}")

# allows the removal of a user
def remove_user():
    user_id = input("Enter the user ID to remove: ")
    if user_id in user_db:
        del user_db[user_id]
        print(f"User with ID '{user_id}' removed successfully.")
    else:
        print(f"User with ID '{user_id}' does not exist.")

# check book out
def check_out_book():
    user_id = input("Enter your user ID: ")
    if user_id in user_db:
        user = user_db[user_id]
        search_term = input("Enter the title of the book you want to check out: ").lower()
        book = find_book(search_term, search_by="title")
        if book:
            message = user.borrow_book(book)
            print(message)
        else:
            print("Sorry, we couldn't find a book with that title.")
    else:
        print(f"User ID '{user_id}' does not exist.")

# return a book
def return_book():
    user_id = input("Enter your user ID: ")
    if user_id in user_db:
        user = user_db[user_id]
        search_term = input("Enter the title of the book you want to return: ").lower()
        book = find_book(search_term, search_by="title")
        if book:
            message = user.return_book(book)
            print(message)
        else:
            print("Sorry, we couldn't find a book with that title.")
    else:
        print(f"User ID '{user_id}' does not exist.")

# main menue to allow users to interact and select an option.
def main():
    while True:
        print("\nOptions:")
        print("1. Add a book to the catalog")
        print("2. Search for a book")
        print("3. Check out a book")
        print("4. Return a book")
        print("5. View borrowed books")
        print("6. Create a new user")
        print("7. List all users")
        print("8. Remove a user")
        print("9. Quit")
        choice = input("Select an option: ")

        if choice == "1":
            add_book_to_catalog()
        elif choice == "2":
            search_and_display_books()
        elif choice == "3":
            check_out_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            user_id = input("Enter your user ID: ")
            if user_id in user_db:
                user = user_db[user_id]
                borrowed_books = user.view_borrowed_books()
                if borrowed_books:
                    print("Borrowed books:")
                    for book in borrowed_books:
                        print(f"  - {book}")
                else:
                    print("No books currently borrowed.")
            else:
                print(f"User ID '{user_id}' does not exist.")
        elif choice == "6":
            create_new_user()
        elif choice == "7":
            list_users()
        elif choice == "8":
            remove_user()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
