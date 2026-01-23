from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models.news import News

from typing import List
from app.services.ranking import rank_news

def get_candidate_news(
        db: Session,
        hours: int=120
):
    """
    获取最近 hours 小时内发布的新闻作为候选
    """
    now = datetime.utcnow()
    since = now - timedelta(hours=hours)

    candidates = (
        db.query(News).filter(News.published_at >= since).all()
        # db.query(News).filter((News.published_at >= since) | (News.published_at.is_(None) & (News.created_at >= since)))
    )

    return candidates

def select_daily_news(
        db: Session,
        top_n: int = 5
) -> List[News]:
    """
    生成今日top-N新闻
    """
    candidates = get_candidate_news(db)

    if not candidates:
        return []
    
    top_news = rank_news(candidates, top_n=top_n)
    return top_news

# TODO: 每日选择的新闻应该与过去不同