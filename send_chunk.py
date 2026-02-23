import asyncio
import os
from telegram import Bot

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = -1003738444350

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROGRESS_FILE = os.path.join(BASE_DIR, "current_story.txt")


def get_all_stories():
    stories = []

    for folder in sorted(os.listdir(BASE_DIR)):
        if folder.startswith("Chapter_"):
            chapter_path = os.path.join(BASE_DIR, folder)

            if os.path.isdir(chapter_path):
                files = sorted(os.listdir(chapter_path))

                for file in files:
                    if file.endswith(".pdf"):
                        stories.append(os.path.join(chapter_path, file))

    return stories


def extract_info(filepath):
    folder_name = os.path.basename(os.path.dirname(filepath))
    chapter_number = folder_name.replace("Chapter_", "")

    filename = os.path.splitext(os.path.basename(filepath))[0]

    parts = filename.split("_", 1)
    if len(parts) > 1:
        filename = parts[1]

    title = filename.replace("_", " ")

    return chapter_number, title


async def send_story():
    bot = Bot(token=BOT_TOKEN)
    stories = get_all_stories()

    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            current_index = int(f.read().strip())
    else:
        current_index = 0

    if current_index >= len(stories):
        print("All stories sent.")
        return

    story_path = stories[current_index]
    chapter_number, title = extract_info(story_path)

    message = f"Here are today's pages:\n\nChapter: {chapter_number}\nPrasang: {title}"
    await bot.send_message(chat_id=CHAT_ID, text=message)

    with open(story_path, "rb") as f:
        await bot.send_document(chat_id=CHAT_ID, document=f)

    print(f"Sent: {story_path}")

    with open(PROGRESS_FILE, "w") as f:
        f.write(str(current_index + 1))


if __name__ == "__main__":
    asyncio.run(send_story())






