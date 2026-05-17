from flask import Flask, render_template, request, redirect
import sys
import os

sys.path.append(os.getcwd())
from ExpenseTracker.manager import ExpenseManager

app = Flask(__name__, template_folder='templates')
manager = ExpenseManager()

@app.route('/')
def home():
    analytics = manager.get_advanced_analytics()
    return render_template('index.html', expenses=manager.expenses, analytics=analytics)

@app.route('/add', methods=['POST'])
def add():
    amount = request.form.get('amount')
    category = request.form.get('category')
    date = request.form.get('date')
    comment = request.form.get('comment', '')
    
    if amount and category and date:
        manager.add_expense(float(amount), category, date, comment)
    return redirect('/')

@app.route('/set-budget', methods=['POST'])
def update_budget():
    limit = request.form.get('limit')
    if limit:
        manager.set_new_budget(float(limit))
    return redirect('/')

# ЖАҢА: Текст және комментарий бойынша ақылды іздеу маршруты
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip()
    analytics = manager.get_advanced_analytics()
    if query:
        filtered = manager.smart_search(query)
        return render_template('index.html', expenses=filtered, analytics=analytics, search_query=query)
    return redirect('/')

# ЖАҢА: Қаржылық мақсат қосу маршруты
@app.route('/add-goal', methods=['POST'])
def add_goal():
    title = request.form.get('title')
    target = request.form.get('target')
    saved = request.form.get('saved')
    
    if title and target and saved:
        manager.add_goal(title, float(target), float(saved))
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
