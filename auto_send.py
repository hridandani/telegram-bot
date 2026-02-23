import asyncio
from datetime import datetime
import time
from send_chunk import send_story

# Railway runs in UTC
# 8:00 AM PST = 16:00 UTC (during standard time)
TARGET_HOUR = 16
TARGET_MINUTE = 0

while True:
    now = datetime.utcnow()

    if now.hour == TARGET_HOUR and now.minute == TARGET_MINUTE:
        asyncio.run(send_story())
        time.sleep(60)  # prevent double send

    time.sleep(5)



