from .abstract import BaseModel

class Expense(BaseModel):
    def __init__(self, db, user_id, amount, category, description, date):
        super().__init__(db)
        self._user_id = user_id
        self._amount = amount
        self._category = category
        self._description = description
        self._date = date

    def save(self):   # overriding
        query = """
        INSERT INTO expenses (user_id, amount, category, description, date)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (self._user_id, self._amount, self._category, self._description, self._date)
        return self._db.execute_query(query, values)