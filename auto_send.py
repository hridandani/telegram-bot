import asyncio
from datetime import datetime
import time
from send_chunk import send_story

# Railway runs in UTC
TARGET_HOUR = 18   # 7:30 AM EST = 12:30 UTC
TARGET_MINUTE = 15

sent_today = False

while True:
    now = datetime.utcnow()

    if now.hour == TARGET_HOUR and now.minute == TARGET_MINUTE and not sent_today:
        asyncio.run(send_story())
        sent_today = True

    if now.hour == 0 and now.minute == 0:
        sent_today = False

    time.sleep(60)




