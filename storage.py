import json
import os

class Storage:
    EXPENSES_FILE = "expenses.json"
    BUDGET_FILE = "budget.json"
    GOALS_FILE = "goals.json"

    @classmethod
    def load_expenses(cls):
        if not os.path.exists(cls.EXPENSES_FILE):
            return []
        try:
            with open(cls.EXPENSES_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Егер ішіндегі дерек объект түрінде болса, оны Expense-ке айналдыру үшін
                # main.py немесе manager.py өзі өңдейді, бірақ бізге тізім қайтару керек
                from expense import Expense
                expenses_list = []
                for item in data:
                    expenses_list.append(Expense(
                        amount=item.get('amount'),
                        category=item.get('category'),
                        date=item.get('date'),
                        comment=item.get('comment', '')
                    ))
                return expenses_list
        except Exception:
            return []

    @classmethod
    def save_expenses(cls, expenses):
        data = []
        for exp in expenses:
            data.append({
                "amount": exp.amount,
                "category": exp.category,
                "date": exp.date,
                "comment": exp.comment
            })
        with open(cls.EXPENSES_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @classmethod
    def load_budget_limit(cls):
        if not os.path.exists(cls.BUDGET_FILE):
            return 0.0
        try:
            with open(cls.BUDGET_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return float(data.get('limit', 0.0))
        except Exception:
            return 0.0

    @classmethod
    def save_budget_limit(cls, limit):
        with open(cls.BUDGET_FILE, 'w', encoding='utf-8') as f:
            json.dump({"limit": limit}, f, ensure_ascii=False, indent=4)

    @classmethod
    def load_saving_goals(cls):
        if not os.path.exists(cls.GOALS_FILE):
            return []
        try:
            with open(cls.GOALS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return []

    @classmethod
    def save_saving_goals(cls, goals):
        with open(cls.GOALS_FILE, 'w', encoding='utf-8') as f:
            json.dump(goals, f, ensure_ascii=False, indent=4)
