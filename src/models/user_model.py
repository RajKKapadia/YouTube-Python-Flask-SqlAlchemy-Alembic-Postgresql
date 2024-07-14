from datetime import datetime, timezone
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
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc))
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
    username: Mapped[str] = mapped_column(String(128))

    def __repr__(self) -> str:
        """print(user)
        id -> email
        """
        return f'{self.id} -> {self.email}.'

    def _to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'created_at': self.created_at,
            'is_deleted': self.is_deleted,
            'username': self.username
        }
