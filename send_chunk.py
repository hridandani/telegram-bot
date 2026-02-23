import asyncio
import os
import psycopg2
from telegram import Bot

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = -1003503118378
DATABASE_URL = os.environ["DATABASE_URL"]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_connection():
    return psycopg2.connect(DATABASE_URL)


def setup_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS story_progress (
            id SERIAL PRIMARY KEY,
            story_index INTEGER NOT NULL
        );
    """)

    cur.execute("SELECT COUNT(*) FROM story_progress;")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO story_progress (story_index) VALUES (0);")

    conn.commit()
    cur.close()
    conn.close()


def get_story_index():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT story_index FROM story_progress LIMIT 1;")
    index = cur.fetchone()[0]
    cur.close()
    conn.close()
    return index


def update_story_index(new_index):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE story_progress SET story_index = %s;", (new_index,))
    conn.commit()
    cur.close()
    conn.close()


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
    setup_db()

    bot = Bot(token=BOT_TOKEN)
    stories = get_all_stories()

    current_index = get_story_index()
    print("CURRENT INDEX:", current_index)

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

    update_story_index(current_index + 1)


if __name__ == "__main__":
    asyncio.run(send_story())
