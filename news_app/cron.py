from .job import save_latest_item_to_db


def cron_job():
    save_latest_item_to_db()
