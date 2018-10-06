import os
from sys import argv
from goog import transcribe_gcs

directory = argv[1]


def auto_run(directory):

    files = os.listdir(directory)
    for file in files:
        os.rename(os.path.join(directory, file), os.path.join(directory, file.replace(' ', '_')))

    for file in os.listdir(directory):    
        if file.endswith(".mp4"):
            file_path = os.path.join(directory, file)
            transcribe_gcs(file_path)
            print(file_path)
            cmd2='ffmpeg -i /home/aravinth/Downloads/subtitles.srt /home/aravinth/Downloads/subtitles.ass'
            os.system(cmd2)
            cmd1='ffmpeg -i '+file_path+' -vf ass=/home/aravinth/Downloads/subtitles.ass /home/aravinth/Downloads/mysubtitledmovie.mp4'
            os.system(cmd1)
        else:
            continue

auto_run(directory)
