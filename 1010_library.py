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
                if book.is_borrowed:
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