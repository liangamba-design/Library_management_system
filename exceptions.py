class BookNotFoundError(Exception):
    def __init__(self, book_id: str):
        super().__init__(f"Book Not Found: No book with ID '{book_id}' exists.")


class MemberNotFoundError(Exception):
    def __init__(self, member_id: str):
        super().__init__(f"Member Not Found: No member with ID '{member_id}' exists.")


class BookUnavailableError(Exception):
    def __init__(self, title: str):
        super().__init__(f"Book Unavailable: '{title}' is already borrowed.")


class InvalidMenuInputError(Exception):
    def __init__(self, input_val: str):
        super().__init__(f"Invalid Input: '{input_val}' is not a valid option. Please enter 1-8.")