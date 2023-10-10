from .Base import Base
from typing import Optional
class Token(Base):
    access_token: str
    token_type: str

class TokenData(Base):
    email: Optional[str] = None