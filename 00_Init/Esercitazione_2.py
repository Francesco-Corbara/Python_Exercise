from typing import List


class Book:
    def __init__(self, title: str, author: str, year: int, publisher: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.pages = pages

    def reading_time(self) -> str:
        if self.pages < 100:
            return "1 hour"
        elif self.pages <= 200:
            return "2 hours"
        else:
            return "more than 2 hours"

    def __str__(self) -> str:
        return f"'{self.title}' by {self.author} ({self.year}) - {self.publisher}, {self.pages} pp."


class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self.books: List[Book] = []

    def add_book(self, new_book: Book) -> None:
        self.books.append(new_book)

    def search_by_title(self, title_query: str) -> List[Book]:
        results: List[Book] = []
        search_term = title_query.lower()
        for book in self.books:
            if search_term in book.title.lower():
                results.append(book)
        return results

    def search_by_author(self, author_query: str) -> List[Book]:
        results: List[Book] = []
        search_term = author_query.lower()
        for book in self.books:
            if search_term in book.author.lower():
                results.append(book)
        return results

    def total_books(self) -> int:
        return len(self.books)

    def __len__(self) -> int:
        return len(self.books)


class Loan:
    def __init__(self, book: Book, borrower: str) -> None:
        self.book = book
        self.borrower = borrower

    def __str__(self) -> str:
        return f"Loan: {self.book.title} -> {self.borrower}"


if __name__ == "__main__":
    my_library = Library("City Library")

    b1 = Book("1984", "George Orwell", 1949, "Secker & Warburg", 328)
    b2 = Book("Dune", "Frank Herbert", 1965, "Chilton Books", 412)
    b3 = Book("The Little Prince", "Antoine de Saint-Exupery", 1943, "Reynal & Hitchcock", 96)

    my_library.add_book(b1)
    my_library.add_book(b2)
    my_library.add_book(b3)

    print(f"Library: {my_library.name} | Total books: {my_library.total_books()}")

    found_books = my_library.search_by_author("orwell")
    print("Books found by author 'orwell':")
    for book in found_books:
        print(f"  * {book} (Estimated time: {book.reading_time()})")

    active_loan = Loan(b2, "Alex")
    print(active_loan)