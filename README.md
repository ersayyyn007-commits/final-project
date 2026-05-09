# Personal Expense Tracker

A simple and efficient Python-based application designed to help users track their daily expenses, categorize spending, and store data persistently using JSON.

## 🚀 Features
- **Add Expenses:** Input amount, category, and date for each transaction.
- **View History:** Display a formatted list of all recorded expenses.
- **Data Persistence:** All records are automatically saved to a `expenses.json` file.
- **Modular Structure:** Organized code into logical modules for better maintainability.

## 📁 Project Structure
The project follows a clean directory structure:
- `ExpenseTracker/` - Core package containing all logic.
  - `main.py` - Entry point of the application.
  - `manager.py` - Handles business logic and expense management.
  - `storage.py` - Manages JSON file I/O operations.
  - `expense.py` - Defines the Expense data model.
  - `expenses.json` - Local database for storing records.
- `.gitignore` - Prevents unnecessary files from being tracked.
- `README.md` - Project documentation.

## 📅 Weekly Progress
This project was developed over a 3-week period to demonstrate incremental growth:
- **Week 1:** Initial setup, project architecture design, and creation of the basic `Expense` model.
- **Week 2:** Implementation of the `Storage` system to handle data saving and loading via JSON.
- **Week 3:** Developed the `ExpenseManager` for core functionality and created a user-friendly CLI menu in `main.py`.

## 🛠️ How to Run
1. Ensure you have **Python 3.x** installed.
2. Clone the repository or download the files.
3. Open your terminal in the project root directory.
4. Run the application:
   ```bash
   python ExpenseTracker/main.py
