from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./focus_tracker.db"

# Intialise the database engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args = {"check_same_thread": False},

)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # session maker is a factory for creating new Session objects and is configured with the database engine, autocomiitt=False means that changes to the database will not be automatically committed, and autoflush=False means that changes will not be automatically flushed to the database.

base = declarative_base() # base class for our database models, it provides a foundation for defining the structure of our database tables and the relationships between them.

# define database
def get_db():
    db = SessionLocal() # creates a new database session using the SessionLocal factory
    try:
        yield db # yields the database session to be used in the application, allowing for efficient management of database connections and transactions.
    finally:
        db.close() # ensures that the database session is properly closed after use, preventing resource leaks and ensuring that connections are returned to the connection pool.

