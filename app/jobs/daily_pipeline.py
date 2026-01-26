# Daily automated pipeline will be implemented here
from datetime import date
import logging
from typing import Optional
from app.core.database import SessionLocal

from app.services.news_ingestion import ingest_news
from app.services.daily_selector import select_daily_news
from app.services.task_generator import generate_task_for_news
from app.services.daily_tasks import create_daily_task_list

logger = logging.getLogger(__name__)

def run_daily_pipeline(
    target_date: Optional[date] = None,  # 支持回溯/补跑
    force: bool = False  # 支持测试（忽略缓存）
) -> dict:
    """
    Run full daily workflow:
    - news ingestion
    - importance ranking
    - task generation
    - daily task list creation
    """

    if target_date is None:
        target_date = date.today()

    result = {
        "date": target_date.isoformat(), # YYYY-MM-DD
        "news_ingested": 0,
        "news_selected": 0,
        "tasks_generated": 0,
        "daily_list_created": False,
        "daily_list_id": None,
        "errors": [],
    }

    db = SessionLocal()

    try:
        # 1. news ingestion
        try:
            # result["news_ingested"] = ingest_news(force=force)
            result["news_ingested"] = ingest_news()
        except Exception as e:
            logger.exception("News ingestion failed")
            result["errors"].append(f"ingest_news: {e}")

        # 2.importance ranking & daily selection
        try:
            daily_news = select_daily_news(db, top_n=5)
            result["news_selected"] = len(daily_news)
            # result["daily_list_created"] = len(daily_news) > 0
        except Exception as e:
            logger.exception("Daily news selection failed")
            result["errors"].append(f"select_daily_news: {e}")
            daily_news = []

        # 3. task generation
        tasks = []
        for news in daily_news:
            try:
                task = generate_task_for_news(db, news)
                if task:
                    tasks.append(task)
                    result["tasks_generated"] += 1
            except Exception as e:
                logger.exception(f"Task generation failed for news ID {news.id}")
                result["errors"].append(f"generate_task_for_news (news ID {news.id}): {e}")

        # daily list creation
        if tasks:
            try:
                daily_list = create_daily_task_list(db, target_date, tasks)
                result["daily_list_created"] = True
                result["daily_list_id"] = daily_list.id
            except Exception as e:
                logger.exception("Daily task list creation failed")
                result["errors"].append(f"create_daily_task_list: {e}")

    finally:
        db.close()

    return result

