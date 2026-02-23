import asyncio
from datetime import datetime
import time
from send_chunk import send_story

TARGET_HOUR = 10   # put your PST hour here
TARGET_MINUTE = 28 # put your PST minute here

sent_today = False

while True:
    now = datetime.now()  # uses server time (UTC on Railway)

    if now.hour == TARGET_HOUR and now.minute == TARGET_MINUTE and not sent_today:
        asyncio.run(send_story())
        sent_today = True

    if now.hour == 0 and now.minute == 0:
        sent_today = False

    time.sleep(30)




