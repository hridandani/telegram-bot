import asyncio
from datetime import datetime
import time
from send_chunk import send_story

TARGET_HOUR = 18   # 10:15 PST
TARGET_MINUTE = 31

while True:
    now = datetime.now()

    if now.hour == TARGET_HOUR and now.minute == TARGET_MINUTE:
        asyncio.run(send_story())
        time.sleep(60)  # wait 1 minute so it doesn't spam

    time.sleep(5)




