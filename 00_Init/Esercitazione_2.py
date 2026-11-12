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
        if self.pages <= 200:
            return "2 hours"
        return "more than 2 hours"

    def __str__(self) -> str:
        return f"{self.title} - {self.author} ({self.year}), {self.pages} pages"


class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self.catalog = []

    def add_book(self, book_item: Book) -> None:
        self.catalog.append(book_item)

    def search_by_title(self, query: str) -> List[Book]:
        term = query.lower()
        return [item for item in self.catalog if term in item.title.lower()]

    def search_by_author(self, query: str) -> List[Book]:
        term = query.lower()
        return [item for item in self.catalog if term in item.author.lower()]

    def total_books(self) -> int:
        return len(self.catalog)

    def __len__(self) -> int:
        return self.total_books()


class Loan:
    def __init__(self, book: Book, borrower: str) -> None:
        self.book = book
        self.borrower = borrower

    def __str__(self) -> str:
        return f"{self.borrower} borrowed: {self.book.title}"


if __name__ == "__main__":
    local_lib = Library("School Library")

    local_lib.add_book(Book("The Lord of the Rings", "J.R.R. Tolkien", 1954, "Allen & Unwin", 1178))
    local_lib.add_book(Book("Steel Ball Run", "Hirohiko Araki", 2004, "Shueisha", 240))
    local_lib.add_book(Book("The Baron in the Trees", "Italo Calvino", 1957, "Einaudi", 288))

    print(f"Total books: {local_lib.total_books()}")
    print("Search results for author 'tolkien':")
    for item in local_lib.search_by_author("tolkien"):
        print(f"- {item} | reading time: {item.reading_time()}")

    current_loan = Loan(local_lib.catalog[0], "Mark")
    print(current_loan)