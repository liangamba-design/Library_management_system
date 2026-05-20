from exceptions import BookUnavailableError

class Book:
    def __init__(self, book_id: str, title: str, author: str, isbn: str, publication_year: int, available: bool):
        self.__book_id: str = book_id
        self.__title: str = title
        self.__author: str = author
        self.__isbn: str = isbn
        self.__publication_year: int = publication_year
        self.__available: bool = available
    
    @property
    def book_id(self) -> str: 
        return self.__book_id
    
    @property
    def title(self) -> str:
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def author(self) -> str:
        return self.__author
    @author.setter
    def author(self, author: str):
        self.__author = author
    
    @property
    def isbn(self) -> str:
        return self.__isbn
    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn
    
    @property
    def publication_year(self) -> int:
        return self.__publication_year

    @property
    def available(self) -> bool:
        return self.__available

    def mark_as_borrowed(self) -> None:
        if not self.__available:
            raise BookUnavailableError(self.__title)
        self.__available = False
    
    def mark_is_returned(self) -> None:
        if self.__available:
            raise ValueError(f"'{self.__title}' is already returned.")
        self.__available = True