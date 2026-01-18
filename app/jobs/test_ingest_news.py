from app.core.database import SessionLocal
from app.services.news_ingestion import ingest_news

# db = SessionLocal()
count = ingest_news()

print(f"News ingestion test finished. {count} articles processed.")