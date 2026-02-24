import time
from datetime import datetime
from send_chunk import send_story

TARGET_HOUR = 16   # 8 AM PST (UTC)
TARGET_MINUTE = 0

print("Worker started")

while True:
    now = datetime.utcnow()
    print("Current UTC:", now.hour, now.minute)

    if now.hour == TARGET_HOUR and now.minute == TARGET_MINUTE:
        print("TIME MATCHED — SENDING")
        send_story()

    time.sleep(60)
