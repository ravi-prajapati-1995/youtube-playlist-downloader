import os
from email.utils import format_datetime

import yt_dlp

ffmpeg_path = r"C:\ffmpeg-master-latest-win64-gpl-shared\bin"  # Replace with your FFmpeg path
os.environ["PATH"] = ffmpeg_path + os.pathsep + os.environ["PATH"]
BASE_PATH = "G:\\downloads"


def download_audio(url, folder_name):
    folder_path = BASE_PATH + "\\" + folder_name
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder created at {folder_path}")
    else:
        print("Folder already exists.")

    options = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320"
        }],
        "outtmpl": f"{folder_path}\\%(title)s.%(ext)s",
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        try:
            # Extract video or playlist info
            info_dict = ydl.extract_info(url, download=True)

            # If it's a playlist, iterate through entries
            if "entries" in info_dict:
                for entry in info_dict["entries"]:
                    if not entry:  # Handle cases where an entry is None
                        print("Skipping an unavailable video (Entry is None).")
                        continue

                    try:
                        file_path = ydl.prepare_filename(entry)  # Get the file path for the current video

                        # Check if the file already exists, and skip if it does
                        if os.path.exists(file_path):
                            print(f"Skipping {entry['title']} (File already exists).")
                            continue  # Skip this file and continue to the next one

                        print(f"Downloading {entry['title']}...")
                    except yt_dlp.DownloadError as e:
                        print(f"Skipping {entry.get('title', 'Unknown Title')} due to an error: {e}")
                        continue  # Skip to the next video

            else:  # Handle single video download
                try:
                    file_path = ydl.prepare_filename(info_dict)  # Get the file path for the video

                    # Check if the file already exists, and skip if it does
                    if os.path.exists(file_path):
                        print(f"Skipping {info_dict['title']} (File already exists).")
                        return  # Skip if the file exists

                    print(f"Downloading {info_dict['title']}...")
                except yt_dlp.DownloadError as e:
                    print(f"Skipping {info_dict.get('title', 'Unknown Title')} due to an error: {e}")

        except yt_dlp.DownloadError as e:
            print(f"Failed to process URL due to an error: {e}")


playlist_or_song_url = "https://music.youtube.com/playlist?list=PLmfcCDSUSykbCreWECyLwGcQoHrQGlSfS"
folder_name = "Punjabi Hit2"
# Example usage
download_audio(
    playlist_or_song_url,
    folder_name
)
