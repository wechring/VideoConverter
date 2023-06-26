from IPython.core.display import Video
import html
import os
import re
import moviepy.video.io.ImageSequenceClip
image_folder='/content/Untitled Folder'
fps=1

image_files = [os.path.join(image_folder,img)
               for img in sorted(os.listdir(image_folder))
               if img.endswith(".jpg")]
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=5)
clip.write_videofile('myvideo.mp4')
