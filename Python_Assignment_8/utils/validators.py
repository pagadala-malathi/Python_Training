from datetime import datetime

def validate_expense_data(user_id, amount, category, description, date):
    """Validate expense data"""
    errors = []
    
    if not user_id:
        errors.append("User ID is required")
    
    if amount <= 0:
        errors.append("Amount must be positive")
    
    if not category or len(category.strip()) == 0:
        errors.append("Category is required")
    
    if len(category) > 50:
        errors.append("Category must be less than 50 characters")
    
    if description and len(description) > 100:
        errors.append("Description must be less than 100 characters")
    
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        errors.append("Date must be in YYYY-MM-DD format")
    
    if errors:
        return None
    
    return {
        'user_id': user_id,
        'amount': float(amount),
        'category': category.strip(),
        'description': description.strip() if description else "",
        'date': date
    }

def validate_user_data(name, email):
    """Validate user data"""
    errors = []
    
    if not name or len(name.strip()) == 0:
        errors.append("Name is required")
    elif len(name) > 50:
        errors.append("Name must be less than 50 characters")
    
    if email:
        if '@' not in email or '.' not in email:
            errors.append("Valid email is required")
        elif len(email) > 100:
            errors.append("Email must be less than 100 characters")
    
    if errors:
        return None
    
    return {
        'name': name.strip(),
        'email': email.strip() if email else None
    }