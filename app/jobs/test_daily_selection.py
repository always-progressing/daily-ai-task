from app.core.database import SessionLocal
from app.services.daily_selector import select_daily_news

def main():
    db = SessionLocal()

    news_list = select_daily_news(db, top_n=5)

    print(f"Select {len(news_list)} news.")
    for i, news in enumerate(news_list):
        print(f"{i+1}. [{news.source_name}]{news.title} (Published at: {news.published_at})")

    db.close()

if __name__== "__main__":
    main()
