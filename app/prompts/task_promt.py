from pathlib import Path

PROMPT_PATH = Path(__file__).parent / "task_prompt_v1.txt"

# Render the task prompt with news details
def render_task_prompt(news) -> str:
    template = PROMPT_PATH.read_text(encoding="utf-8")
    return template.format(
        title=news.title,
        summary=news.summary,
        source=news.source_name,
    )