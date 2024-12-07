import os

import yt_dlp

ffmpeg_path = r"C:\ffmpeg-master-latest-win64-gpl-shared\bin"  # Replace with your FFmpeg path
os.environ["PATH"] = ffmpeg_path + os.pathsep + os.environ["PATH"]
BASE_PATH = "G:\\downloads"


def download_audio(url, folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder created at {folder_path}")
    else:
        print("Folder already exists.")

    folder_path = BASE_PATH + "\\" + folder_path
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
        info = ydl.extract_info(url, download=False)
        print(info)
        ydl.download([url])


# Example usage
download_audio(
    "https://music.youtube.com/playlist?list=RDCLAK5uy_n-I3VEF7u92CpUknwwVvWy9iLuGq1P9I4&playnext=1&si=JZz-ylrLYMwm2-c6",
    "Haryanvi Songs"
)
