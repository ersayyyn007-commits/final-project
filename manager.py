import functools
from ExpenseTracker.expense import Expense
from ExpenseTracker.storage import Storage

def track_system(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[CORE LOG] Running internal operation: '{func.__name__}'")
        return func(*args, **kwargs)
    return wrapper

class ExpenseManager:
    def __init__(self):
        self.storage = Storage()
        
        # 🔥 ЖАҢА ФУНКЦИЯ: Сайт іске қосылған сайын ескі деректерді жою (Файлдарды тазалау)
        self.clear_database_on_start()
        
        # Тазаланғаннан кейінгі жаңа бос деректерді жүктеу
        self.expenses = self.storage.load_data()
        self.budget_limit = self.storage.load_budget()
        self.goals = self.storage.load_goals()

    # ЖАҢА ӘДІС: Файлдарды бос тізім етіп қайта жазады
    def clear_database_on_start(self):
        self.storage.save_data([])   # expenses.json тазартады
        self.storage.save_goals([])  # goals.json тазартады
        print("[SYSTEM INFO] Ескі транзакциялар мен мақсаттар автоматты түрде жойылды!")

    @track_system
    def add_expense(self, amount: float, category: str, date: str, comment: str):
        new_expense = Expense(amount, category, date, comment)
        self.expenses.append(new_expense.to_dict())
        self.storage.save_data(self.expenses)

    @track_system
    def set_new_budget(self, new_limit: float):
        self.budget_limit = new_limit
        self.storage.save_budget(new_limit)

    def smart_search(self, query: str) -> list:
        query = query.lower()
        return [exp for exp in self.expenses if query in exp['category'].lower() or query in exp['comment'].lower()]

    def add_goal(self, title: str, target: float, saved: float):
        goal = {"title": title.strip(), "target": float(target), "saved": float(saved)}
        self.goals.append(goal)
        self.storage.save_goals(self.goals)

    @track_system
    def get_advanced_analytics(self) -> dict:
        total = sum(float(exp['amount']) for exp in self.expenses)
        categories = [exp['category'] for exp in self.expenses]
        unique_cats = set(categories)
        
        category_percentages = {}
        if total > 0:
            for cat in unique_cats:
                cat_total = sum(float(exp['amount']) for exp in self.expenses if exp['category'] == cat)
                category_percentages[cat] = round((cat_total / total) * 100, 1)

        status = "Normal"
        remaining = self.budget_limit - total
        if total > self.budget_limit: status = "Danger"

        advice = "Сіздің қаржылық жағдайыңыз тұрақты. Бақылауды осылай жалғастырыңыз! 👍"
        if total > self.budget_limit:
            advice = "🛑 Дабыл! Сіз белгіленген лимиттен асып кеттіңіз. Осы айда үнемдеу режимін қосуды ұсынамын!"
        elif total > (self.budget_limit * 0.8):
            advice = "⚠️ Сақ болыңыз! Шығындарыңыз лимиттің 80%-ына жетті. Бос шығындарды азайтыңыз."
        elif len(self.expenses) > 10 and total < (self.budget_limit * 0.5):
            advice = "🌟 Керемет нәтиже! Көптеген транзакция жасалса да, бюджеттің жартысынан азын жұмсадыңыз. Нағыз экономист!"

        processed_goals = []
        for g in self.goals:
            pct = round((g['saved'] / g['target']) * 100, 1) if g['target'] > 0 else 0
            processed_goals.append({**g, "percentage": min(pct, 100.0)})

        return {
            "total": total,
            "count": len(self.expenses),
            "unique_categories": len(unique_cats),
            "budget_limit": self.budget_limit,
            "remaining": remaining,
            "status": status,
            "breakdown": category_percentages,
            "advice": advice,
            "goals": processed_goals
        }
