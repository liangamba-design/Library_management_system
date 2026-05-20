# Library_management_system
Library Management System built using Python and Object-Oriented Programming (OOP). This project supports core functionalities such as adding books and members, borrowing and returning books, and viewing records.

Description

This project is a console-based Library Management System developed using Python and Object-Oriented Programming (OOP) principles. It allows users to manage books, members, and borrowing transactions efficiently.

The system follows a structured flowchart and applies encapsulation using getters and setters, along with custom exception handling for better error management.

🚀 Features 📖 Add Book 👤 Add Member 🔄 Borrow Book ✅ Return Book 📚 View Books 👥 View Members 📋 View Loans (with status: Active / Closed) ❌ Exit System

🧠 OOP Concepts Applied

Encapsulation – private attributes with getters/setters Abstraction – service layer (LibraryService) Modularity – separated into multiple files Exception Handling – custom error classes

🏗️ Project Structure library-system/ │ ├── book.py ├── member.py ├── loan.py ├── library_service.py ├── custom_exceptions.py └── main.py

▶️ How to Run Make sure Python is installed Open terminal in the project folder Run: python main.py ⚙️ System Flow

The program follows a menu-driven system:

User selects an option System processes request Displays result or error Returns to menu

📊 Loan Status System Active → Book is currently borrowed Closed → Book has been returned

✨ Notes The system prevents borrowing unavailable books Ensures proper tracking of book availability Maintains. make another one like this 


