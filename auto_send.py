import time
from datetime import datetime
from send_chunk import send_story

TARGET_HOUR = 12  # 8 AM PST = 16 UTC
TARGET_MINUTE = 30

print("Worker running...")

while True:
    now = datetime.utcnow()

    if now.hour == TARGET_HOUR and now.minute == TARGET_MINUTE:
        try:
            print("Sending story...")
            send_story()
            print("Done.")
            time.sleep(60)
        except Exception as e:
            print("Error:", e)

    time.sleep(5)


