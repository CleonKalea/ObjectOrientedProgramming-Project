class Book:
    def __init__(self, title, author, genre, book_id):
        self.title = title
        self.author = author
        self.genre = genre
        self.book_id = book_id

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id: 
                print(f"\n --> Book with book_id {book_id} has been removed.")
                self.books.remove(book)
                return
            
        raise ValueError("Error removing book with index {book_id}. Book doesn't exist.")

    def search_book(self, search_query):

        for book in self.books:
            if (search_query.lower() in book.title.lower()) or \
                (search_query.lower() in book.author.lower()) or \
                (search_query.lower() in book.genre.lower()):
                
                print("\nSearch Result :")
                print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}")
                return
        raise ValueError(f"There's no book associated with {search_query}")

    def display_books(self):
        print("\nList of All Library's Books : ")
        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book.title}, {book.author}, {book.genre}, {book.book_id}")

if __name__ == "__main__":
    library = Library()

    book1 = Book("A Tale of Two Cities", "Charles Dickens", "Historical Fiction", 1)
    book2 = Book("The Little Prince", "Antoine de Saint-Exupery", "Fantasy", 2)
    book3 = Book("The Alchemist", "Paulo Coelho", "Fantasy", 3)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    library.search_book("Charles Dickens")
    
    library.display_books()

    try:
        library.remove_book(1)
    except ValueError as e:
        print(e)

    library.display_books()

