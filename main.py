from moviepy.editor import *
import os


def get_image_path(path):
    for subdir, dirs, files in os.walk(path):
        for file in files:
            if file.endswith((".jpg", ".png")):
                return os.path.join(subdir, file)


def get_audio_path(path):
    for subdir, dirs, files in os.walk(path):
        for file in files:
            if file.endswith((".mp3", ".wav")):
                return os.path.join(subdir, file)


def make_video(img_loc, audio_loc):
    audio = AudioFileClip(audio_loc)
    video = ImageClip(img_loc).set_duration(audio.duration)
    video = video.set_audio(audio)
    return video


def remove_used_files(img_loc, audio_loc):
    os.remove(img_loc)
    os.remove(audio_loc)


DATA_PATH = ".\data\\"

image_path = get_image_path(DATA_PATH)
audio_path = get_audio_path(DATA_PATH)

video_clip = make_video(image_path, audio_path)
video_clip.write_videofile(f"video\\video.mp4", fps=60)

remove_used_files(image_path, audio_path)
