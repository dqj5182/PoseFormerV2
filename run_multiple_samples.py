import subprocess
from os import listdir

video_dir = '/home/danieljung0121/OnlineAL_CloIT/data/CLOIT/cropped_images_new'
video_names = [f for f in listdir(video_dir)]

import re
def atoi(text):
    return int(text) if text.isdigit() else text
def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]

video_names.sort(key=natural_keys)

for each_video_name in video_names:
    subprocess.call(["python", "demo/vis.py", "--video", each_video_name])