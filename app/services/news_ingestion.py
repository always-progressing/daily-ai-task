# import feedparser
# from datetime import datetime
# from sqlalchemy.orm import Session
# from app.models.news import News

# RSS_SOURCES = [
#     {
#         "name": "OpenAI",
#         "url": "https://openai.com/blog/rss/"
#     },
#     {
#         "name": "Google AI",
#         "url": "https://ai.googleblog.com/feeds/posts/default"
#     }
# ]

# def ingest_news(db: Session):
#     for source in RSS_SOURCES:
#         feed = feedparser.parse(source["url"])

#         for entry in feed.entries: 
#             url = entry.get("link") 
#             if not url: 
#                 continue
#             # 检查新闻是否已存在
#             exists = db.query(News).filter(News.url == url).first()
#             if exists:
#                 continue

#             published = entry.get("published_parsed")
#             published_at = (
#                 datetime(*published[:6]) if published else None
#             )

#             news = News(
#                 title=entry.get("title", ""),
#                 summary=entry.get("summary", ""),
#                 source=source["name"],
#                 url=url,
#                 published_at=published_at
#             )

#             db.add(news)
#     db.commit()

import feedparser
from datetime import datetime
from app.core.database import SessionLocal
from app.models.news import News

# FEEDS = [
#     "https://openai.com/blog/rss.xml",
#     "https://arxiv.org/rss/cs.AI",
# ]

FEEDS = [
    {
        "name": "OpenAI",
        "url": "https://openai.com/blog/rss.xml",
        "type": "official",
    },
    {
        "name": "Anthropic",
        "url": "https://www.anthropic.com/rss.xml",
        "type": "official",
    },
    {
        "name": "arXiv cs.AI",
        "url": "https://arxiv.org/rss/cs.AI",
        "type": "paper",
    },
    {
        "name": "Hugging Face",
        "url": "https://huggingface.co/blog/feed.xml",
        "type": "community",
    },
]


def ingest_news() -> int:
    db = SessionLocal()
    inserted = 0

    for feed_cfg in FEEDS:
        print(f"Fetching feed: {feed_cfg['url']}")
        parsed_feed = feedparser.parse(feed_cfg["url"])

        print(f"Feed title: {parsed_feed.feed.get('title')}")
        print(f"Entries found: {len(parsed_feed.entries)}")

        for entry in parsed_feed.entries:
            title = entry.get("title")
            url = entry.get("link")

            if not title or not url:
                print("Skipping entry without title or url")
                continue

            # 去重（非常重要）
            exists = db.query(News).filter(News.url == url).first()
            if exists:
                continue

            published = None
            if "published_parsed" in entry and entry.published_parsed:
                published = datetime(*entry.published_parsed[:6])

            news = News(
                title=title,
                summary=entry.get("summary", "")[:2000],
                url=url,
                published_at=published,
                source_name=feed_cfg["name"],
                source_type=feed_cfg["type"],
            )

            db.add(news)
            inserted += 1

    db.commit()
    db.close()

    return inserted
