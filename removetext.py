#Remove text on video with inpaint telea by #hsbg
import cv2
import os
import numpy as np

# Path ke folder dengan frame yang memiliki teks dan folder output untuk menyimpan hasil
detected_text_frames_folder = 'detected_text_frames'
output_cleaned_frames_folder = 'cleaned_text_frames'

# Membuat folder untuk menyimpan frame tanpa teks jika belum ada
if not os.path.exists(output_cleaned_frames_folder):
    os.makedirs(output_cleaned_frames_folder)

# Fungsi untuk menghilangkan latar belakang dan teks dari gambar
def remove_background_and_text(frame):
    # Konversi gambar ke grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Menggunakan adaptive threshold untuk memisahkan teks dari latar belakang
    background_mask = cv2.adaptiveThreshold(gray_frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY, 11, 2)

    # Invers mask untuk mendapatkan area teks
    inverse_background_mask = cv2.bitwise_not(background_mask)

    # Terapkan inpainting untuk menghilangkan teks
    cleaned_frame = cv2.inpaint(frame, inverse_background_mask, inpaintRadius=7, flags=cv2.INPAINT_TELEA)

    return cleaned_frame

# Memproses setiap frame di folder detected_text_frames
for frame_filename in sorted(os.listdir(detected_text_frames_folder)):
    frame_path = os.path.join(detected_text_frames_folder, frame_filename)
    frame = cv2.imread(frame_path)

    # Menghilangkan latar belakang dan teks dari frame
    cleaned_frame = remove_background_and_text(frame)

    # Simpan frame yang telah dibersihkan di folder baru
    output_path = os.path.join(output_cleaned_frames_folder, frame_filename)
    cv2.imwrite(output_path, cleaned_frame)

    print(f'Teks dihilangkan dari {frame_filename} dan disimpan di {output_cleaned_frames_folder}')

print(f'Proses selesai! Frame yang telah dibersihkan disimpan di folder {output_cleaned_frames_folder}')