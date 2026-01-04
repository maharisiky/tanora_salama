import os
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from django_apscheduler.jobstores import MemoryJobStore, register_job
from dotenv import load_dotenv

load_dotenv()
scheduler = BackgroundScheduler()
scheduler.add_jobstore(MemoryJobStore(), "default")

@register_job(scheduler, IntervalTrigger(seconds=30), name='call_api_healthy', replace_existing=True)
def call_api_healthy():
    url = f'{os.getenv('APP_BASE_URL')}/api/health_check/'
    try:
        response = requests.get(url)
        print(f"GET {url} status: {response.status_code}")
    except Exception as e:
        print(f"Error calling {url}: {e}")

if __name__ == "__main__":
    print("Starting scheduler...")
    scheduler.start()
    import time
    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("Scheduler stopped.")