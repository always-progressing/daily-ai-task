from sqlalchemy import Column, Date, Integer, String, DateTime, Text
from datetime import datetime
from app.core.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text, nullable=True)
    source_news_id = Column(String, index=True)
    date = Column(Date, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)