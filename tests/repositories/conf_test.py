import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database.base import Base

TEST_DB_URL = "sqlite:///:memory:"
test_engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=test_engine, autoflush=False, autocommit=False)

@pytest.fixture(scope="session")
def db_session():
    # Setup: create tables and session
    Base.metadata.create_all(bind=test_engine)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        # Teardown: drop all tables
        Base.metadata.drop_all(bind=test_engine)


def test_create_user(db_session):
    repo = UserRepository(db_session)
    user = User("test", "test")
    created_user = repo.create(user)
    assert created_user.name == "test"
