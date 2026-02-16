from datetime import datetime
from sqlalchemy.orm import Session
from app.models.user_task import UserTask

def mark_task_completed(
    db: Session,
    user_id: int,
    task_id: int,
) -> UserTask:
    """
    标记任务为已完成，并记录完成时间
    """
    record = (
        db.query(UserTask)
        .filter_by(user_id=user_id, task_id=task_id)
        .first()
    )
    if not record:
        record = UserTask(
            user_id = user_id,
            task_id = task_id,
            completed = True,
            # completed_at = datetime.utcnow(),
        )
        db.add(record)
    
    record.completed = True
    record.completed_at = datetime.utcnow()
    db.commit()
    return record