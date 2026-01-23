from sqlalchemy import Column, Date, Integer, String, DateTime, Text, ForeignKey
from datetime import datetime
from app.core.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    # one-to-one key to News(cache)
    news_id = Column(Integer, ForeignKey("news.id"), unique=True, index=True)

    # title = Column(String)
    # description = Column(Text, nullable=True)
    # source_news_id = Column(String, index=True)
    # date = Column(Date, index=True)
    # created_at = Column(DateTime, default=datetime.utcnow)

    # structured fields (future use)
    title = Column(String(200))
    goal = Column(Text)
    estimated_time = Column(String(50))
    steps = Column(Text)  # JSON/YAML string

    # raw LLM output (debug / replay)
    task_yaml = Column(Text, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)