# 创建数据库表（初始化脚本）
from app.core.database import engine, Base
from app.models import user, task, user_task

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__": 
    init_db()

