from datetime import date
from book import Book
from member import Member

class Loan:
    def __init__(self, loan_id: str, member: Member, book: Book, loan_date: date = None, return_date: date = None):
        self.__loan_id: str = loan_id
        self.__member: Member = member
        self.__book: Book = book
        self.__loan_date: date = loan_date if loan_date else date.today()
        self.__return_date: date = return_date

    @property
    def loan_id(self) -> str:
        return self.__loan_id

    @property
    def member(self) -> Member:
        return self.__member

    @property
    def book(self) -> Book:
        return self.__book

    @property
    def loan_date(self) -> date:
        return self.__loan_date

    @property
    def return_date(self) -> date:
        return self.__return_date

    def finalize_loan(self) -> None:
        self.book.mark_as_borrowed()
        self.__loan_date = date.today()

    def return_book(self) -> None:
        self.book.mark_is_returned()
        self.__return_date = date.today()

    def __str__(self) -> str:
        status = "Returned" if self.return_date else "Active"
        return (f"Loan ID: {self.loan_id}\n"
                f"Member: {self.member.name} (ID: {self.member.member_id})\n"
                f"Book: {self.book.title}\n"
                f"Loan Date: {self.loan_date}\n"
                f"Return Date: {self.return_date if self.return_date else 'Not returned'}\n"
                f"Status: {status}")