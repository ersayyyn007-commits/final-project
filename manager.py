from ExpenseTracker.expense import Expense
from ExpenseTracker.storage import Storage

class ExpenseManager:
    def __init__(self):
        self.storage = Storage()
        self.expenses = self.storage.load_data()

    def add_expense(self, amount, category, date):
        new_expense = Expense(amount, category, date)
        self.expenses.append(new_expense.to_dict())
        self.storage.save_data(self.expenses)
        print("\n✅ Шығын сәтті сақталды!")

    def show_expenses(self):
        if not self.expenses:
            print("\n📭 Тізім әлі бос.")
            return
        print("\n--- Барлық шығындар тізімі ---")
        for exp in self.expenses:
            print(f"📅 {exp['date']} | 📂 {exp['category']}: 💰 {exp['amount']} тг")