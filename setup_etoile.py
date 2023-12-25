import os
from pathlib import Path

working_dir = Path.cwd()

data_input_dir = working_dir / "Data Input"
data_processed_dir = working_dir / "Data Processed"

if not data_input_dir.exists():
    os.mkdir(data_input_dir)

if not data_processed_dir.exists():
    os.mkdir(data_processed_dir)

resources_dir_text = "Resources_Path.txt"

with open(resources_dir_text, 'a') as writer:
    writer.close()

entry_list = []

with open(resources_dir_text, 'r') as reader:
    entry_list.append(reader.read())
    reader.close()

if entry_list[0]:
    resources_dir = Path(entry_list[0])
    print(f"Resources Directory: {resources_dir}")

    if not resources_dir.exists():
        os.mkdir(resources_dir)

    photo_related_dir = resources_dir / "Photo Related Files"
    video_related_dir = resources_dir / "Video Related Files"

    if not photo_related_dir.exists():
        os.mkdir(photo_related_dir)
    if not video_related_dir.exists():
        os.mkdir(video_related_dir)

else:
    print(f"No Directory")

