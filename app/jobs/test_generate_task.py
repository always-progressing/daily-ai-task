from app.core.database import SessionLocal
from app.services.daily_selector import select_daily_news
from app.services.task_generator import generate_task_for_news

def main():
    db = SessionLocal()

    news_list = select_daily_news(db, top_n=5)
    news = news_list[4]
    print(news.title)

    task1 = generate_task_for_news(db, news)
    task2 = generate_task_for_news(db, news)

    print("Task ID:", task1.id)
    # print("Task content:", task1.content)
    print("Task YAML:", task1.task_yaml)
    print("Cached:", task1.id == task2.id)

    db.close()

if __name__ == "__main__":
    main()
