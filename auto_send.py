import time
import asyncio
from datetime import datetime
from send_chunk import send_story

TARGET_HOUR = 4
TARGET_MINUTE = 40

while True:
    now = datetime.utcnow()
    print("Current UTC:", now.hour, now.minute)

    if now.hour == TARGET_HOUR and now.minute == TARGET_MINUTE:
        print("TIME MATCHED — SENDING")
        asyncio.run(send_story())

    time.sleep(60)