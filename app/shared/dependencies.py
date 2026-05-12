from app.core.database import SessionLocal
\
# Dependency function to get a database session for FastAPI routes and services.
def get_db():
    """
    Provides a database session for the duration of a request and ensures it is properly closed afterward.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()