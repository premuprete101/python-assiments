Lab Assignment-1 Create a class Employee inherits it into another class Manager. Add methods to get input & print information of employees. Consider the attributes name, age, salary, address etc. process the information of 10 managers class Employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.salary = 0
        self.address = ""

    def get_input(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.salary = float(input("Enter Salary: "))
        self.address = input("Enter Address: ")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")
        print(f"Address: {self.address}")


class Manager(Employee):   # Inheriting Employee
    def __init__(self):
        super().__init__()
        self.department = ""

    def get_input(self):
        super().get_input()
        self.department = input("Enter Department: ")

    def display(self):
        super().display()
        print(f"Department: {self.department}")


# Processing 10 Managers
managers = []

for i in range(10):
    print(f"\nEnter details for Manager {i+1}")
    m = Manager()
    m.get_input()
    managers.append(m)

print("\n--- Manager Details ---")
for i, m in enumerate(managers):
    print(f"\nManager {i+1}:")
    m.display()


Lab Assignment-2 Create a Library Management System with the following mechanisms: a) Design classes for Book, Member, and Library. b) Implement methods for adding books, lending books to members, returning books, and displaying book information. C) Create a menu-driven interface for the library management system.

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        self.books.append(Book(book_id, title, author))
        print("Book added successfully!")

    def add_member(self):
        member_id = input("Enter Member ID: ")
        name = input("Enter Member Name: ")
        self.members.append(Member(member_id, name))
        print("Member added successfully!")

    def display_books(self):
        if not self.books:
            print("No books available.")
            return

        for book in self.books:
            status = "Available" if book.is_available else "Not Available"
            print(f"{book.book_id} | {book.title} | {book.author} | {status}")

    def lend_book(self):
        book_id = input("Enter Book ID to lend: ")
        member_id = input("Enter Member ID: ")

        book = next((b for b in self.books if b.book_id == book_id), None)
        member = next((m for m in self.members if m.member_id == member_id), None)

        if book and member:
            if book.is_available:
                book.is_available = False
                member.borrowed_books.append(book)
                print("Book issued successfully!")
            else:
                print("Book is not available.")
        else:
            print("Invalid Book ID or Member ID.")

    def return_book(self):
        book_id = input("Enter Book ID to return: ")
        member_id = input("Enter Member ID: ")

        member = next((m for m in self.members if m.member_id == member_id), None)

        if member:
            for book in member.borrowed_books:
                if book.book_id == book_id:
                    book.is_available = True
                    member.borrowed_books.remove(book)
                    print("Book returned successfully!")
                    return
            print("This member does not have this book.")
        else:
            print("Invalid Member ID.")


# Menu-driven system
library = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Display Books")
    print("4. Lend Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        library.add_book()
    elif choice == '2':
        library.add_member()
    elif choice == '3':
        library.display_books()
    elif choice == '4':
        library.lend_book()
    elif choice == '5':
        library.return_book()
    elif choice == '6':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")



