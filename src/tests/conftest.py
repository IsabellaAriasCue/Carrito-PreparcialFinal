import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from testcontainers.postgres import PostgresContainer

from src.database.models import Base
@pytest.fixture(scope="session")
def postgres_container():
    with PostgresContainer("postgres:16") as postgres:
        yield postgres


@pytest.fixture(scope="session")
def engine(postgres_container):

    engine = create_engine(
        postgres_container.get_connection_url()
    )

    Base.metadata.create_all(engine)

    yield engine

    engine.dispose()

@pytest.fixture
def db_session(engine):

    connection = engine.connect()

    transaction = connection.begin()

    SessionLocal = sessionmaker(
        bind=connection
    )

    session = SessionLocal()

    yield session

    session.close()

    transaction.rollback()

    connection.close()
