from sqlalchemy.orm import Session 
from app.models.user import User 
from app.repositories.user_repository import UserRepository
from fastapi import Depends
from typing import Optional, List


class UserCrudService : 

    def __init__(self , repository : UserRepository = Depends(UserRepository)):
        self.repository = repository
        

    def create(self, user : User) -> User: 
        print("Creating user")
        return self.repository.create(user=user)
        

    def find_by_id(self, id : int) -> Optional[User]: 
        return self.repository.find_by_id(id=id)
         

    def find_all(self) -> List[User] : 
        return self.repository.find_all()
        

    def delete_by_id(self, id : int)->Optional[User] : 
        return self.repository.delete_by_id(id=id)
        