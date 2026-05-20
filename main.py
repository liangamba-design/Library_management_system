from library_service import LibraryService
from book import Book
from member import Member
from exceptions import BookNotFoundError, MemberNotFoundError, BookUnavailableError, InvalidMenuInputError

library = LibraryService()


def display_menu():
    print("\n===== LIBRARY SYSTEM =====")
    print("1. Add New Book")
    print("2. Add New Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View All Books")
    print("6. View All Members")
    print("7. View All Loans")
    print("8. Exit")
    print("===========================")


def main():
    while True:
        display_menu()
        try:
            choice = input("Enter choice (1-8): ")
            if not choice.isdigit() or int(choice) not in [1,2,3,4,5,6,7,8]:
                raise InvalidMenuInputError(choice)
            choice = int(choice)

            if choice == 1:
                print("\n--- Add New Book ---")
                book_id = input("Enter Book ID: ")
                title = input("Enter Book Title: ")
                author = input("Enter Author Name: ")
                isbn = input("Enter ISBN: ")
                year = int(input("Enter Publication Year: "))
                available_input = input("Is it available? (yes/no): ").strip().lower()
                available = True if available_input == "yes" else False
                new_book = Book(book_id, title, author, isbn, year, available)
                library.add_book(new_book)
                print("✅ Book added successfully!")

            elif choice == 2:
                print("\n--- Add New Member ---")
                member_id = input("Enter Member ID: ")
                name = input("Enter Full Name: ")
                email = input("Enter Email: ")
                phone = input("Enter Phone Number: ")
                new_member = Member(member_id, name, email, phone)
                library.add_member(new_member)
                print("✅ Member added successfully!")

            elif choice == 3:
                print("\n--- Borrow Book ---")
                m_id = input("Enter Member ID: ")
                b_id = input("Enter Book ID: ")
                loan = library.borrow_book(m_id, b_id)
                print("✅ Book borrowed successfully!")
                print(loan)

            elif choice == 4:
                print("\n--- Return Book ---")
                loan_id = input("Enter Loan ID: ")
                library.return_book(loan_id)
                print("✅ Book returned successfully!")

            elif choice == 5:
                print("\n--- Book List ---")
                books = library.get_all_books()
                if not books:
                    print("No books registered.")
                else:
                    for b in books:
                        status = "✅ Available" if b.available else "❌ Borrowed"
                        print(f"ID: {b.book_id} | Title: {b.title} | Author: {b.author} | Year: {b.publication_year} | Status: {status}")

            elif choice == 6:
                print("\n--- Member List ---")
                members = library.get_all_members()
                if not members:
                    print("No members registered.")
                else:
                    for m in members:
                        print(f"ID: {m.member_id} | Name: {m.name} | Email: {m.email} | Phone: {m.phone}")

            elif choice == 7:
                print("\n--- Loan List ---")
                loans = library.get_all_loans()
                if not loans:
                    print("No loan records found.")
                else:
                    for ln in loans:
                        print("------------------------")
                        print(ln)

            elif choice == 8:
                print("Exiting... Goodbye!")
                break

        except InvalidMenuInputError as e:
            print(f"❌ {e}")
        except MemberNotFoundError as e:
            print(f"❌ {e}")
        except BookNotFoundError as e:
            print(f"❌ {e}")
        except BookUnavailableError as e:
            print(f"❌ {e}")
        except ValueError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()