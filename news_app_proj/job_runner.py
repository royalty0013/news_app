import os
from pathlib import Path
import logging
import logging.handlers
import sys
import django
import schedule
import time


# append_path = Path(__file__).resolve().parent.parent
# sys.path.append(append_path)
sys.path.append(
    r'C:\Users\hassan.braimah\Documents\projects\Django projects\newsAppEnv\news_app_proj')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_app_proj.settings')
# os.environ["DJANGO_SETTINGS_MODULE"] = "news_app_proj.settings"
django.setup()
from news_app.job import save_latest_item_to_db

FILE_NAME = 'logger.log'
job_logger = logging.getLogger('JobLogger')
job_logger.setLevel(logging.DEBUG)

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(FILE_NAME,
                                               maxBytes=512000,
                                               backupCount=5,
                                               )
job_logger.addHandler(handler)


def run():
    save_latest_item_to_db()


schedule.every(5).minutes.do(run)
while True:
    schedule.run_pending()
    time.sleep(5)


# if __name__ == '__main__':
#     save_latest_item_to_db()
