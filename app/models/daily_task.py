from sqlalchemy import Column, Integer, String, Text, DateTime, Date, ForeignKey
from datetime import datetime
from app.core.database import Base

class DailyTaskList(Base):
    __tablename__ = "daily_task_lists"

    id = Column(Integer, primary_key=True)
    date = Column(Date, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class DailyTaskItem(Base):
    __tablename__ = "daily_task_items"

    id = Column(Integer, primary_key=True)
    daily_list_id = Column(ForeignKey("daily_task_lists.id"))
    task_id = Column(ForeignKey("tasks.id"))