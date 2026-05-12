from abc import ABC, abstractmethod


class BookRepository(ABC):

    @abstractmethod
    def create(self, db, book_data):
        raise NotImplementedError

    @abstractmethod
    def get_all(self, db, skip: int = 0, limit: int = 10, search: str = None):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, db, book_id: int):
        raise NotImplementedError

    @abstractmethod
    def delete(self, db, book):
        raise NotImplementedError
