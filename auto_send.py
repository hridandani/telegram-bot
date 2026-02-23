import asyncio
from datetime import datetime
import time
from send_chunk import send_story

# 11:09 PM PST = 07:09 UTC
TARGET_HOUR = 7
TARGET_MINUTE = 10

while True:
    now = datetime.utcnow()

    if now.hour == TARGET_HOUR and now.minute == TARGET_MINUTE:
        asyncio.run(send_story())
        time.sleep(60)  # prevents multiple sends in same minute

    time.sleep(5)




