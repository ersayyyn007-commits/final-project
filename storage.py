import json
import os

class Storage:
    def __init__(self, data_file="ExpenseTracker/expenses.json", budget_file="ExpenseTracker/budget.json", goals_file="ExpenseTracker/goals.json"):
        self.data_file = data_file
        self.budget_file = budget_file
        self.goals_file = goals_file

    def load_data(self) -> list:
        if not os.path.exists(self.data_file): return []
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file: return json.load(file)
        except: return []

    def save_data(self, data: list):
        with open(self.data_file, 'w', encoding='utf-8') as file: json.dump(data, file, indent=4, ensure_ascii=False)

    def load_budget(self) -> float:
        if not os.path.exists(self.budget_file): return 50000.0
        try:
            with open(self.budget_file, 'r', encoding='utf-8') as file: return json.load(file).get("limit", 50000.0)
        except: return 50000.0

    def save_budget(self, limit: float):
        with open(self.budget_file, 'w', encoding='utf-8') as file: json.dump({"limit": limit}, file, indent=4)

    # ЖАҢА: Қаржылық мақсаттарды жүктеу және сақтау
    def load_goals(self) -> list:
        if not os.path.exists(self.goals_file): return []
        try:
            with open(self.goals_file, 'r', encoding='utf-8') as file: return json.load(file)
        except: return []

    def save_goals(self, goals: list):
        with open(self.goals_file, 'w', encoding='utf-8') as file: json.dump(goals, file, indent=4, ensure_ascii=False)
