from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.core.database import Base

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    summary = Column(Text)
    url = Column(String, unique=True, index=True)
    published_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)

    source_name = Column(String(100))
    source_type = Column(String(50))