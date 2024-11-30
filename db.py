from datetime import datetime

import pytz
from sqlalchemy import DateTime, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Tugas(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    nama: Mapped[str] = mapped_column(String(30))
    detail: Mapped[str] = mapped_column(String(100))
    deadline: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(pytz.timezone("Asia/Jakarta"))
    )
