import logging
from apscheduler.schedulers.blocking import BlockingScheduler
from app.services.daily_pipeline import run_daily_pipeline
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def scheduled_job():
    logger.info("Starting daily pipeline job at %s", datetime.now())
    result = run_daily_pipeline()
    logger.info("Daily pipeline job completed. Daily List ID: %s, Tasks Generated: %d, Daily List Created: %s",
                result["daily_list_id"],
                result["tasks_generated"],
                result["daily_list_created"])
    
def main():
    # # 测试用
    # scheduler_test = BlockingScheduler(timezone="UTC")
    # scheduler_test.add_job(run_daily_pipeline, trigger="date")
    # scheduler_test.start()

    # 正式用
    scheduler = BlockingScheduler(timezone="UTC")
    # Schedule the job to run daily at 8:00 UTC
    scheduler.add_job(
        scheduled_job,
        trigger="cron",
        hour=8,
        minute=0,
    )
    logger.info("Scheduler started. Daily pipeline job will run at 8:00 UTC daily.")
    # scheduler.start()

if __name__ == "__main__":
    main()

