from sqlalchemy import Column, BigInteger, String, Text

from core.db.database import Base


class Todo(Base):
    __tablename__ = 'todos'

    id = Column(BigInteger, primary_key=True, index=True)
    title = Column(String(128), index=True)
    text = Column(Text)
