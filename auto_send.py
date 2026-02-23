import asyncio
from datetime import datetime
import time
from send_chunk import send_story

target_hour = 7
target_minute = 30

sent_today = False

while True:
    now = datetime.now()

    if now.hour == target_hour and now.minute == target_minute and not sent_today:
        asyncio.run(send_story())
        sent_today = True

    if now.hour == 0 and now.minute == 0:
        sent_today = False

    time.sleep(5)





