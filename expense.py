class Expense:
    def __init__(self, amount: float, category: str, date: str, comment: str = ""):
        self.amount = amount
        self.category = category.strip().capitalize()
        self.date = date
        self.comment = comment.strip() if comment else "No comment"

    def to_dict(self) -> dict:
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "comment": self.comment
        }
