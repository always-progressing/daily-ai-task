from app.core.database import SessionLocal
from app.models.news import News
from app.services.ranking import rank_news

db = SessionLocal()

news = db.query(News).all()
top = rank_news(news, top_n=5)

for n in top:
    print(f"Title: {n.title}\n URL: {n.url}\n")

