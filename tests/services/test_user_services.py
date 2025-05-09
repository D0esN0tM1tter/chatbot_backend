from app.models.user import User
from app.services.user_crud_services import UserCrudService
from app.repositories.user_repository import UserRepository

def test_create_user(mocker):

    # create an object which simulates the behavior of the repository
    mock_repo = mocker.MagicMock(spec=UserRepository)
    user_service = UserCrudService(mock_repo)
    user = User(id = 1 , name="test", email="test@example.com")
    
    # Mock the repository's create method to return the user
    mock_repo.create.return_value = user
    
    created_user = user_service.create(user)
    
    mock_repo.create.assert_called_once_with(user=user)  # Ensure the create method was called once
    assert created_user.name == "test"
    assert created_user.email == "test@example.com"
    assert created_user.id is not None  

def test_find_user_by_id(mocker):
    # Arrange
    mock_repo = mocker.MagicMock(spec=UserRepository)
    user_service = UserCrudService(mock_repo)
    user = User(name="test", email="test@example.com", id=1)
    
    # Mock the repository's find_by_id method to return the user
    mock_repo.find_by_id.return_value = user
    
    # Act
    found_user = user_service.find_by_id(1)
    
    # Assert
    mock_repo.find_by_id.assert_called_once_with(id=1)
    assert found_user is not None
    assert found_user.id == 1
    assert found_user.name == "test"
    assert found_user.email == "test@example.com"

def test_find_all_users(mocker):
    # Arrange
    mock_repo = mocker.MagicMock(spec=UserRepository)
    user_service = UserCrudService(mock_repo)
    user1 = User(name="test1", email="test1@example.com", id=1)
    user2 = User(name="test2", email="test2@example.com", id=2)
    
    # Mock the repository's find_all method to return a list of users
    mock_repo.find_all.return_value = [user1, user2]
    
    # Act
    users = user_service.find_all()
    
    # Assert
    mock_repo.find_all.assert_called_once()
    assert len(users) == 2
    assert users[0].name == "test1"
    assert users[1].name == "test2"

def test_delete_user_by_id(mocker):
    # Arrange
    mock_repo = mocker.MagicMock(spec=UserRepository)
    user_service = UserCrudService(mock_repo)
    user = User(name="test", email="test@example.com", id=1)
    
    # Mock the repository's delete_by_id method to return the user
    mock_repo.delete_by_id.return_value = user
    
    # Act
    deleted_user = user_service.delete_by_id(id=1)
    
    # Assert
    mock_repo.delete_by_id.assert_called_once_with(id=1)
    assert deleted_user is not None
    assert deleted_user.id == 1
    assert deleted_user.name == "test"
