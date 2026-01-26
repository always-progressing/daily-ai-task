# CLI / scheduler 入口
from app.jobs.daily_pipeline import run_daily_pipeline
result = run_daily_pipeline()

print(result["daily_list_id"])
print(result["tasks_generated"])
print(result["daily_list_created"])
