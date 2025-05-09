from app.models.user import User
from app.repositories.user_repository import UserRepository


def test_create_user(db_session):
    repo = UserRepository(db_session)
    user = User(name="test", email="test@example.com")
    created_user = repo.create(user)
    assert created_user.name == "test"
    assert created_user.email == "test@example.com"
    assert created_user.id is not None 


def test_find_user_by_id(db_session):
    repo = UserRepository(db_session)
    user = User(name="test", email="test@example.com")
    created_user = repo.create(user)
    found_user = repo.find_by_id(created_user.id)
    assert found_user is not None
    assert found_user.id == created_user.id
    assert found_user.name == "test"
    assert found_user.email == "test@example.com"


def test_find_all_users(db_session):
    repo = UserRepository(db_session)
    user1 = User(name="test1", email="test1@example.com")
    user2 = User(name="test2", email="test2@example.com")
    repo.create(user1)
    repo.create(user2)
    
    users = repo.find_all()
    assert len(users) == 2
    assert any(user.name == "test1" for user in users)
    assert any(user.name == "test2" for user in users)

def test_delete_user_by_id(db_session):
    repo = UserRepository(db_session)
    user = User(name="test", email="test@example.com")
    created_user = repo.create(user)
    
    # Check if user is created and exists
    found_user = repo.find_by_id(created_user.id)
    assert found_user is not None

    deleted_user = repo.delete_by_id(created_user.id)
    
    # Verify the user is deleted
    assert deleted_user is not None
    assert deleted_user.id == created_user.id
    assert repo.find_by_id(created_user.id) is  None  
