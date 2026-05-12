from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    """Pydantic model for user login request."""
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    """Pydantic model for JWT token response."""
    access_token: str
    token_type: str