import asyncio
from datetime import datetime
import time
from send_chunk import send_story

TARGET_HOUR = 19   # change for your test
TARGET_MINUTE = 1

while True:
    now = datetime.utcnow()

    if now.hour == TARGET_HOUR and now.minute == TARGET_MINUTE:
        asyncio.run(send_story())
        time.sleep(60)  # prevent multiple sends in same minute

    time.sleep(5)




