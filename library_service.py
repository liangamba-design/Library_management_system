from book import Book
from member import Member
from loan import Loan
from exceptions import BookNotFoundError, MemberNotFoundError

class LibraryService:
    def __init__(self):
        self.books = []
        self.members = []
        self.loans = []

    def add_book(self, book: Book):
        self.books.append(book)

    def add_member(self, member: Member):
        self.members.append(member)

    def find_book(self, book_id: str) -> Book:
        for b in self.books:
            if b.book_id == book_id:
                return b
        raise BookNotFoundError(book_id)

    def find_member(self, member_id: str) -> Member:
        for m in self.members:
            if m.member_id == member_id:
                return m
        raise MemberNotFoundError(member_id)

    def borrow_book(self, member_id: str, book_id: str) -> Loan:
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        loan_id = f"L{len(self.loans)+1:03d}"
        new_loan = Loan(loan_id, member, book)
        new_loan.finalize_loan()
        self.loans.append(new_loan)
        return new_loan

    def return_book(self, loan_id: str):
        for ln in self.loans:
            if ln.loan_id == loan_id:
                ln.return_book()
                return
        raise ValueError("Loan not found.")

    def get_all_books(self):
        return self.books

    def get_all_members(self):
        return self.members

    def get_all_loans(self):
        return self.loans