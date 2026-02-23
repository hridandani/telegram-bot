import os
import requests

BOT_TOKEN = "8580409834:AAE8b_ZpDhSvbrImVI4dbPo5-3rFosHVW9A"
CHAT_ID = -1003503118378

BASE_DIR = "."

# Get overall story index
with open("current_story.txt", "r") as f:
    story_index = int(f.read().strip())

# Get all chapters sorted
chapters = sorted([d for d in os.listdir(BASE_DIR) if d.startswith("Chapter")])

all_files = []

# Collect all PDFs in order
for chapter in chapters:
    chapter_path = os.path.join(BASE_DIR, chapter)
    pdfs = sorted([f for f in os.listdir(chapter_path) if f.endswith(".pdf")])
    for pdf in pdfs:
        all_files.append((chapter, pdf))

# Get the correct story
chapter_name, file = all_files[story_index]

prasang = file.split("_", 1)[1].replace("_", " ").replace(".pdf", "")

caption = f"""Here are today's pages:

{chapter_name}
Prasang: {prasang}"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"

with open(os.path.join(chapter_name, file), "rb") as doc:
    requests.post(
        url,
        data={"chat_id": CHAT_ID, "caption": caption},
        files={"document": doc}
    )

# Increment overall story index
with open("current_story.txt", "w") as f:
    f.write(str(story_index + 1))

print("Sent successfully.")