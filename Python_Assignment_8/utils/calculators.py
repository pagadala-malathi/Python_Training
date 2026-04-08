from functools import reduce

# Total Expense
def calculate_total(expenses):
    amounts = list(map(lambda x: x['amount'], expenses))
    return reduce(lambda a, b: a + b, amounts, 0)

# Filter by category
def filter_by_category(expenses, category):
    return list(filter(lambda x: x['category'] == category, expenses))

# Filter by date (list comprehension)
def filter_by_date(expenses, date):
    return [e for e in expenses if str(e['date']) == date]

# Category-wise spending (dictionary comprehension)
def category_wise(expenses):
    return {
        cat: sum(e['amount'] for e in expenses if e['category'] == cat)
        for cat in set(e['category'] for e in expenses)
    }

# Highest expense using reduce
def highest_expense(expenses):
    return reduce(lambda a, b: a if a['amount'] > b['amount'] else b, expenses)