from datetime import datetime
from urllib.parse import urlparse
from app.models.news import News
from typing import List

# SOURCE_WEIGHT = {
#     "openai.com": 5,
#     "deepmind.com": 5,
#     "anthropic.com": 5,
#     "google.com": 4,
#     "microsoft.com": 3,
#     # "arxiv.org": 3,
#     "github.com": 3,
#     "medium.com": 2,
#     "towardsdatascience.com": 2,
#     "reddit.com": 2,

# }

SOURCE_TYPE_WEIGHT = {
    "official": 5,
    "paper": 4,
    "community": 2,
    "blog": 2,
}


KEYWORDS = {
    # "artificial intelligence": 3,
    "machine learning": 2,
    "deep learning": 2,
    "neural network": 2,
    "nlp": 2,
    "natural language processing": 2,
    "computer vision": 2,
    "reinforcement learning": 2,
    "transformer": 3,
    "big data": 2,
    "data science": 2,
    "gpt": 3,
    "llm": 3,
    "agent": 3,
    "rag": 3,
    "open source": 2,
    "benchmark": 2,
    "release": 2,
    "paper": 1,

}

def score_news(news: News) -> int:
    score = 0

    # source score
    # domain = urlparse(news.url).netloc.replace("www.","")
    score += SOURCE_TYPE_WEIGHT.get(news.source_type, 1)

    # keyword score
    text = f"{news.title} {news.summary}".lower()
    for kw, kw_score in KEYWORDS.items():
        if kw in text:
            score += kw_score

    # freshness score
    now = datetime.utcnow()
    if news.published_at:
        hours = (now - news.published_at).total_seconds() / 3600
        if hours < 6:
            score += 3
        elif hours < 24:
            score += 2
        elif hours < 72:
            score += 1

    # content length penalty
    if news.summary and len(news.summary) < 100:
        score -= 1

    return max(score, 0)

def rank_news(news_list: List[News], top_n: int = 5) -> List[News]:
    scored = [(news, score_news(news)) for news in news_list]
    scored.sort(key=lambda x: x[1], reverse=True)
    return [news for news, score in scored[:top_n]]

