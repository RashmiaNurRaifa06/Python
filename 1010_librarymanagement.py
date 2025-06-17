class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} [{status}]"
    
class Library:
    def __init__(self):
        self.books = []
    def add_book(self,title,author):
        self.books.append(Book(title,author))
        print(f"Book '{title} by {author} added.")
        
    def list_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for idx,book in enumerate(self.books,1):
            print(f"{idx}. {book}")
        
    def borrow_book(self,book_number):
        if 1 <= book_number <= len(self.books):
            book = self.books[book_number - 1]
            if not book.is_borrowed:
                book.is_borrowed = True
                print(f"You borrowed '{book.title}'.")
            else:
                print("Book is already borrowed.")
        else:
            print("Invalid book number.")
                
    def return_book(self,book_number):
        if 1 <= book_number <= len(self.books):
            book = self.books[book_number - 1]
            if book.is_borrowed:
                book.is_borrowed = False
                print(f"You returned '{book.title}'.")
            else:
                print("Book was not borrowed.")
        else:
            print("Invalid book number.")
        
    def search_books(self,keyword):
        found = False
        for idx,book in enumerate(self.books,1):
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                print(f"{idx}. {book}")
                found = True
        if not found:
            print("No books found matching your search.")
                
    def remove_book(self,book_number):
        if 1 <= book_number <= len(self.books):
            removed = self.books.pop(book_number - 1)
            print(f"Removed '{removed.title}' by {removed.author}.")
        else:
            print("Invalid book number.")
                
def main():
    library = Library()
    initial_books = [
        ("Harry Potter and the Philosopher's Stone", "J.K Rowling"),
        ("Harry Potter and the Chamber of Secrets", "J.K Rowling"),
        ("Harry Potter and the Prisoner of Azkaban", "J.K Rowling"),
        ("Harry Potter and the Goblet of Fire", "J.K Rowling"),
        ("Harry Potter and the Order of the Pheonix", "J.K Rowling"),
        ("Harry Potter and the Half-Blood Prince", "J.K Rowling"),
        ("Harry Potter and the Deathly Hallows", "J.K Rowling"),
        ("Harry Potter and the Cursed Child", "J.K Rowling"),
        ("Diary of the Wimpy Kid", "Jeff Kinney"),
        ("Slappy New Year", "R.L Stine"),
        ("Little Shop of Hamsters", "R.L Stine"),
    ]
    
    for title,author in initial_books:
        library.add_book(title,author)
        
    while True:
        print("\nLibrary Management System")
        print("1.Add books")
        print("2.List books")
        print("3.Borrow books")
        print("4.Return books")
        print("5.Search books")
        print("6.Remove books")
        print("7.Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(title,author)
        elif choice == '2':
            library.list_books()
        elif choice == '3':
            library.list_books()
            try:
                book_number = int(input("Enter the number of the book you want to borrow: "))
                library.borrow_book(book_number)
            except ValueError:
                print("Invalid input.")
        elif choice == '4':
            library.list_books()
            try:
                book_number = int(input("Enter the number of the book you want to return: "))
                library.return_book(book_number)
            except ValueError:
                print("Invalid input.")
        elif choice == '5':
            keyword = input("Enter title or author name to search: ")
            library.search_books(keyword)
        elif choice == '6':
            library.list_books()
            try:
                book_number = int(input("Enter the number of the book you want to remove: "))
                library.remove_book(book_number)
            except ValueError:
                print("Invalid input.")
        elif choice == '7':
            print("Exiting Library Management System.....")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()                