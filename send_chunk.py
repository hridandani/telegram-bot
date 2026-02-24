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


def send_story():
    bot = Bot(token=BOT_TOKEN)
    stories = get_all_stories()

    # read current story index
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            current_index = int(f.read().strip())
    else:
        current_index = 0

    print("CURRENT INDEX:", current_index)

    story_path = stories[current_index]

    folder_name = os.path.basename(os.path.dirname(story_path))
    chapter_number = folder_name.replace("Chapter_", "")

    filename = os.path.splitext(os.path.basename(story_path))[0]
    parts = filename.split("_", 1)
    if len(parts) > 1:
        filename = parts[1]

    title = filename.replace("_", " ")

    message = f"Here are today's pages:\n\nChapter: {chapter_number}\nPrasang: {title}"

    bot.send_message(chat_id=CHAT_ID, text=message)

    with open(story_path, "rb") as f:
        bot.send_document(chat_id=CHAT_ID, document=f)

    print("Sent:", story_path)

    # increase index
    with open(PROGRESS_FILE, "w") as f:
        f.write(str(current_index + 1))