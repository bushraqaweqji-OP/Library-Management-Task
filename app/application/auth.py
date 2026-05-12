from app.domain.auth.services import login_user


def authenticate_user(db, email: str, password: str):
    return login_user(db, email, password)
