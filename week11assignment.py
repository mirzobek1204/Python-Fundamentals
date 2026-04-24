from dataclasses import dataclass,field
from contextlib import contextmanager
class BookError(Exception):
    pass
@dataclass
class Book:
    title: str
    genre: str
    pages: int
    _status: str = field(init=False,default="NEW")
    def __post_init__(self):
        if self.pages <= 0:
            raise BookError(f"Invalid pages for {self.title}")
        
    @property
    def is_long(self):
        return self.pages > 300
    
    def __str__(self):
        return f"{self.title} ({self.genre}, {self.pages}p) [{self._status}]"
    
    def __gt__(self,other):
        if not isinstance(other,Book):
            return NotImplemented
        return self.pages > other.pages
    
class ShelfScanner:
    def __init__(self,books,genres):
        self.books = books
        self.genres = genres
        self._cursor = 0
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._cursor >= len(self.books):
            raise StopIteration
        book = self.books[self._cursor]
        self._cursor += 1
        if book.genre in self.genres:
            book._status = "AVAILABLE"
        else:
            book._status = "UNAVAILABLE"
        return book
    
def shelf_report(scanner):
    available = 0
    unavailable = 0
    for book in scanner:
        if book._status == "AVAILABLE":
            available += 1
        else:
            unavailable += 1
        yield str(book)
    yield f"Report: {available} available, {unavailable} unavailable"

@contextmanager
def library_session(name):
    print(f">>> Session: {name}")
    shelf = []
    try:
        yield shelf
    except BookError as e:
        print(f"!!! Error: {e}")
    finally:
        print(f"<<< Closed: {name} ({len(shelf)} books)")
        
with library_session("Morning") as shelf:
    shelf.append(Book("The Great Gatsby", "Fiction", 281))
    shelf.append(Book("Moby Dick", "Fiction", 635))
    shelf.append(Book("A Brief History of Time", "Science", 212))

    for line in shelf_report(ShelfScanner(shelf, ("Fiction", "History"))):
        print(line)

    print(shelf[1] > shelf[0])

print()

with library_session("Evening") as shelf:
    shelf.append(Book("1984", "Fiction", -50))

    
