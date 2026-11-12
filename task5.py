import schedule
import time
from datetime import datetime


def job() -> None:
    hour = datetime.now().hour
    h12 = hour % 12 or 12
    for _ in range(h12):
        print("Ку")


schedule.every().hour.at(":00").do(job)
# schedule.every().minute.at(":00").do(job) #test


if __name__ == "__main__":
    print("Планировщик запущен.")
    while True:
        schedule.run_pending()
        time.sleep(1)