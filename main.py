import sys
import os

# Модульдерді табу үшін негізгі жолды қосамыз
sys.path.append(os.getcwd())

from ExpenseTracker.manager import ExpenseManager

def main():
    manager = ExpenseManager()
    
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Жаңа шығын қосу")
        print("2. Шығындарды көру")
        print("3. Шығу")
        
        choice = input("\nТаңдауыңызды енгізіңіз: ")
        
        if choice == '1':
            try:
                amount = float(input("Сомасы (мысалы, 5000): "))
                category = input("Категория (Тамақ, Көлік, т.б.): ")
                date = input("Күні (КК.АА.ЖЖЖЖ): ")
                manager.add_expense(amount, category, date)
            except ValueError:
                print("❌ Қате: Соманы санмен енгізіңіз!")
        elif choice == '2':
            manager.show_expenses()
        elif choice == '3':
            print("Сау болыңыз! 👋")
            break
        else:
            print("❌ Қате таңдау, қайта көріңіз.")

if __name__ == "__main__":
    main()