import asyncio
from telegram import Bot

BOT_TOKEN = "8580409834:AAFG2FNTN_ir5bAy3XoD_VDNFk4Bx18AVGc"
CHAT_ID = -1003503118378  # main 40-person group

message = """Jai Swaminarayan Everyone  

We have created a new group dedicated to deeper reflection and understanding of our gurus' Jivan Charitra.   

In this group, thoughtful questions will be sent once a week based on the pages that were sent. Feel free to ask questions and have discussions with each other in this group. 

The purpose of this group is for us to do manan so we can better understand and imbibe the values that our gurus have displayed throughout their life.   

Please join using the link below: 
https://t.me/+8rMz0rce78FjZTJh
"""

async def main():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message)

asyncio.run(main())