import time
from datetime import datetime
from send_chunk import send_story

TARGET_HOUR = 16   # 8 AM PST
TARGET_MINUTE = 0

while True:
    now = datetime.utcnow()

    if now.hour == TARGET_HOUR and now.minute == TARGET_MINUTE:
        send_story()

    time.sleep(60)
