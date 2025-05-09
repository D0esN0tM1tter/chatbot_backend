from sqlalchemy.orm import Session
from app.models.user import User
from fastapi import Depends
from app.database.database import get_db
from typing import Optional, List



class UserRepository:

    def __init__(self, session: Session=Depends(get_db)):
        self.session = session

    def create(self, user: User) -> User:
        # Using the session directly, no need for `with` block
        self.session.add(user)
        self.session.commit()  # Commit the transaction
        return user

    def find_by_id(self, id: int) -> Optional[User]:
        return self.session.query(User).filter(User.id == id).first()

    def find_all(self) -> List[User]:
        return self.session.query(User).all()

    def delete_by_id(self, id: int) -> Optional[User]:
        user = self.find_by_id(id)
        if user:
            self.session.delete(user)
            self.session.commit()  # Commit the transaction
        return user
