from .abstract import BaseModel

class User(BaseModel):
    def __init__(self, db, name):
        super().__init__(db)
        self._name = name

    def save(self):
        return self._db.add_user(self._name)