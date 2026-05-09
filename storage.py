import json
import os

class Storage:
    # Папка аты мен файл атын дұрыс көрсету маңызды
    def __init__(self, filename="ExpenseTracker/expenses.json"):
        self.filename = filename

    def load_data(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except:
            return []

    def save_data(self, data):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)