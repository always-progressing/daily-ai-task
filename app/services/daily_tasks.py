from datetime import date
from sqlalchemy.orm import Session
from app.models.daily_task import DailyTaskList, DailyTaskItem

def create_daily_task_list(
        db: Session,
        target_date: date,
        tasks: list
) -> DailyTaskList:
    """
    创建/复用某天的清单
    """
    existing = (
        db.query(DailyTaskList)
        .filter(DailyTaskList.date == target_date)
        .first()
    )
    if existing:
        return existing
    
    daily_list = DailyTaskList(date=target_date)
    db.add(daily_list)
    db.flush()  # 获取 daily_list.id

    for task in tasks:
        item = DailyTaskItem(
            daily_list_id=daily_list.id,
            task_id=task.id,
        )
        db.add(item)

    db.commit()
    return daily_list

