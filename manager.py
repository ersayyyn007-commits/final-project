import os
from expense import Expense
from storage import Storage

class ExpenseManager:
    def __init__(self):
        # Бастапқы деректерді жүктейміз немесе бос тізім жасаймыз
        self.expenses = Storage.load_expenses()
        self.budget_limit = Storage.load_budget_limit()
        self.saving_goals = Storage.load_saving_goals()

    def add_expense(self, amount, category, date, comment):
        print("[CORE LOG] Running internal operation: 'add_expense'")
        # Жаңа транзакция объектісін жасау
        new_expense = Expense(amount, category, date, comment)
        self.expenses.append(new_expense)
        # Файлға сақтау
        Storage.save_expenses(self.expenses)
        return new_expense

    def get_all_expenses(self):
        return self.expenses

    def set_budget_limit(self, limit):
        self.budget_limit = limit
        Storage.save_budget_limit(limit)

    def add_saving_goal(self, title, target, saved=0.0):
        goal = {
            "title": title,
            "target": target,
            "saved": saved,
            "percentage": round((saved / target) * 100, 1) if target > 0 else 0.0
        }
        self.saving_goals.append(goal)
        Storage.save_saving_goals(self.saving_goals)

    def get_advanced_analytics(self):
        print("[CORE LOG] Running internal operation: 'get_advanced_analytics'")
        
        total_expenses = 0.0
        total_income = 0.0

        # Шығыстар мен кірістерді бөлек есептейміз
        for exp in self.expenses:
            amt = float(exp.amount)
            if amt < 0:
                total_expenses += abs(amt)
            else:
                total_income += amt

        # Қалдық баланс (Кіріс + Шығыс, өйткені шығыс теріс таңбамен тұр)
        remaining_balance = total_income - total_expenses

        # Ақылды кеңес (AI Insight) жүйесі
        advice = "Сіздің қаржылық жүйеңіз тұрақты қалыпта. Транзакциялар сәтті өңделуде."
        if self.budget_limit > 0:
            usage_pct = (total_expenses / self.budget_limit) * 100
            if usage_pct >= 100:
                advice = f"🚨 Назар аударыңыз! Белгіленген лимиттен асып кеттіңіз ({round(usage_pct, 1)}%). Шығындарды шұғыл шектеңіз!"
            elif usage_pct >= 80:
                advice = f"⚠️ Ескерту: Бюджет лимитінің {round(usage_pct, 1)}% жұмсалды. Шығындарды бақылауда ұстаңыз."
            else:
                advice = f"✅ Тамаша! Бюджет лимитінің тек {round(usage_pct, 1)}% жұмсалды. Қаржылық жоспарыңыз өте жақсы."
        elif total_expenses > 0 and total_income == 0:
            advice = "💡 Кеңес: Қазір тек шығындар тіркеліп жатыр. Балансты теңгерімде ұстау үшін кірістерді (Credit) енгізуді ұмытпаңыз."

        # Мақсаттардың пайызын қайта тексеру
        updated_goals = []
        for goal in self.saving_goals:
            target = float(goal.get('target', 1))
            saved = float(goal.get('saved', 0))
            goal['percentage'] = round((saved / target) * 100, 1) if target > 0 else 0.0
            updated_goals.append(goal)

        return {
            "total": round(total_expenses, 2),
            "income": round(total_income, 2),
            "remaining": round(remaining_balance, 2),
            "budget_limit": round(self.budget_limit, 2),
            "advice": advice,
            "goals": updated_goals
        }
