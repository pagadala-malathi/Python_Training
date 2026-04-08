from abc import ABC, abstractmethod

class BaseModel(ABC):
    def __init__(self, db):
        self._db = db   # encapsulation

    @abstractmethod
    def save(self):
        pass