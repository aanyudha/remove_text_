import cv2
import os
from imageio import get_writer

# Path ke video input dan output folder untuk menyimpan frame
base_dir = r'C:/python/remove_text_/'  # Base directory for the video
input_video_path = 'input_video.mp4'
output_frames_folder = 'detected_text_frames'

# Membuat folder untuk menyimpan frame jika belum ada
if not os.path.exists(output_frames_folder):
    os.makedirs(output_frames_folder)

# Membaca video
cap = cv2.VideoCapture(input_video_path)

# Mendapatkan properti video
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = int(cap.get(cv2.CAP_PROP_FOURCC))

# Loop melalui setiap gambar di direktori
frame_number = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_filename = os.path.join(output_frames_folder, f'frame_{frame_number:04d}.png')
    frame_number += 1
    
# Membuat video dari frame
output_video_path = os.path.join(base_dir, 'vid_joined_hsbg.mp4')
with get_writer(output_video_path, fps=fps) as writer:
    for i in range(frame_number):
        frame_filename = os.path.join(output_frames_folder, f'frame_{i:04d}.png')
        frame = cv2.imread(frame_filename)
        writer.append_data(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

print(f'Video selesai dibuat! Video disimpan di {output_video_path}')