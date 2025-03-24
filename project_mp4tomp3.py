from pydub import AudioSegment
import os

file_path = "C:/Users/Dell/Desktop/MorePython/bappaDa"  # Update this with the correct path

if os.path.exists(file_path):
    video = AudioSegment.from_file(file_path, "mp4")
    video.export("output.mp3", format="mp3")
    print("Conversion successful!")
else:
    print(f"File {file_path} not found.")
