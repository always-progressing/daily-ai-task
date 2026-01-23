from sqlalchemy.orm import Session
from app.models.news import News
from app.models.task import Task
from app.services.llm_client import call_llm
from app.prompts.task_promt import render_task_prompt

def generate_task_for_news(db: Session, news: News) -> Task:
    # cache check
    existing = db.query(Task).filter(Task.news_id == news.id).first()
    if existing:
        return existing
    
    # render prompt
    prompt = render_task_prompt(news)

    # call LLM
    task_yaml = call_llm(prompt)
    
    # create Task (MVP 不强制解析 YAML)
    task = Task(
        news_id=news.id,
        title="",
        goal="",
        estimated_time="",
        steps="",
        task_yaml=task_yaml,
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task

