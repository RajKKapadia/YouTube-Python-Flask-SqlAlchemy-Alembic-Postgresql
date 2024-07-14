from datetime import datatime, timezone
import uuid

from sqlalchemy import String, Boolean, DateTime, UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase


class UserBase(DeclarativeBase):
    pass


class User(UserBase):
    __tablename__ = 'user'

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    email: Mapped[str] = mapped_column(String(128), unique=True)
    password: Mapped[str] = mapped_column(String(128))
    created_at: Mapped[datatime] = mapped_column(
        DateTime, default=datatime.now(timezone.utc))
    """
    name
    is_verified
    """

    def __repr__(self) -> str:
        """print(user)
        id -> email
        """
        return f'{self.id} -> {self.email}.'

    def _to_dict(self):
        {
            'id': self.id,
            'email': self.email,
            'created_at': self.created_at
        }
