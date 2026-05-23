from apscheduler.schedulers.background import BackgroundScheduler # type: ignore
from app.services.sales_pipeline import generate_daily_sales_report

scheduler = BackgroundScheduler()

scheduler.add_job(
    generate_daily_sales_report,
    'cron',
    hour=7
)

scheduler.start()