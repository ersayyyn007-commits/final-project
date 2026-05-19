import os
from flask import Flask, render_template, request, redirect
from expense import Expense
from manager import ExpenseManager
from storage import Storage

app = Flask(__name__)

# Мәліметтер қорын жүктеу және тазалау
#Storage.clear_data()
manager = ExpenseManager()

@app.route('/')
def index():
    expenses = manager.get_all_expenses()
    analytics = manager.get_advanced_analytics()
    
    # --- КАТЕГОРИЯЛАРДЫ ПАЙЫЗБЕН ЕСЕПТЕУ (ҚАУІПСІЗ BACKEND ЛОГИКА) ---
    cat_weights = {}
    if expenses:
        total_volume = 0.0
        # Әр категорияның сомасын жинаймыз
        for exp in expenses:
            val = abs(float(exp.amount))
            cat_weights[exp.category] = cat_weights.get(exp.category, 0.0) + val
            total_volume += val
        
        # Пайызға айналдырамыз
        if total_volume > 0:
            for cat in cat_weights:
                cat_weights[cat] = round((cat_weights[cat] / total_volume) * 100, 1)
    # ---------------------------------------------------------------

    return render_template('index.html', expenses=expenses, analytics=analytics, cat_weights=cat_weights, search_query=None)

@app.route('/add', methods=['POST'])
def add_transaction():
    try:
        tx_type = request.form.get('tx_type', 'Expense')
        raw_amount = float(request.form.get('amount', 0))
        category = request.form.get('category', 'Other')
        date = request.form.get('date')
        comment = request.form.get('comment', '')

        if tx_type == 'Expense':
            amount = -abs(raw_amount)
        else:
            amount = abs(raw_amount)

        manager.add_expense(amount, category, date, comment)
        
    except Exception as e:
        print(f"Flask backend error during /add: {e}")
        
    return redirect('/')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip()
    if not query:
        return redirect('/')
    
    expenses = manager.get_all_expenses()
    analytics = manager.get_advanced_analytics()
    
    filtered = [
        e for e in expenses 
        if query.lower() in getattr(e, 'category', '').lower() or query.lower() in getattr(e, 'comment', '').lower()
    ]
    
    return render_template('index.html', expenses=filtered, analytics=analytics, cat_weights={}, search_query=query)

@app.route('/set-budget', methods=['POST'])
def set_budget():
    limit = float(request.form.get('limit', 0))
    manager.set_budget_limit(limit)
    return redirect('/')

@app.route('/add-goal', methods=['POST'])
def add_goal():
    title = request.form.get('title')
    target = float(request.form.get('target', 0))
    saved = float(request.form.get('saved', 0))
    manager.add_saving_goal(title, target, saved)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
