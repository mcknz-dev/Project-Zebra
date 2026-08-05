from datetime import datetime

from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Receipt(Base):
    __tablename__ = "receipts"

    id: Mapped[int] = mapped_column(primary_key=True)

    storage_path: Mapped[str] = mapped_column(String(500))

    merchant: Mapped[str] = mapped_column(String(255))

    total: Mapped[float] = mapped_column(Float)

    currency: Mapped[str] = mapped_column(String(10))

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)