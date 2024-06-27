"""
  Now is easy to implement the database repository. The DBRepository
  should implement the Repository (Storage) interface and the methods defined
  in the abstract class Storage.

  The methods to implement are:
    - get_all
    - get
    - save
    - update
    - delete
    - reload (which can be empty)
"""

from src.models.base import Base
from src.persistence.repository import Repository
from src import db


class DBRepository(Repository):
    """Dummy DB repository"""

    def __init__(self) -> None:
        """Initialize the DB repository with a session"""
        self.session = db.session

    def get_all(self, model_name: str) -> list:
        """Retrieve all objects of a given model"""
        model_class = self._get_model_class(model_name)
        return self.session.query(model_class).all()

    def get(self, model_name: str, obj_id: str) -> Base | None:
        """Retrieve an object by its ID"""
        model_class = self._get_model_class(model_name)
        return self.session.query(model_class).get(obj_id)

    def reload(self) -> None:
        """Reload the objects from the database"""
        self.session.expire_all()

    def save(self, obj: Base) -> None:
        """Save a new object to the database"""
        self.session.add(obj)
        self.session.commit()

    def update(self, obj: Base) -> Base | None:
        """Update an existing object"""
        self.session.commit()
        return obj

    def delete(self, obj: Base) -> bool:
        """Delete an object from the database"""
        self.session.delete(obj)
        self.session.commit()
        return True

