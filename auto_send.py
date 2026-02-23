import asyncio
from datetime import datetime
import time
from send_chunk import send_story

TARGET_HOUR = 16
TARGET_MINUTE = 0

print("Worker started")

while True:
    try:
        now = datetime.utcnow()

        if now.hour == TARGET_HOUR and now.minute == TARGET_MINUTE:
            print("Sending story...")
            asyncio.run(send_story())
            print("Story sent.")
            time.sleep(60)

        time.sleep(5)

    except Exception as e:
        print("ERROR:", e)
        time.sleep(10)



