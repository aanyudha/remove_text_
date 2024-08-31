pip install opencv-python-headless pytesseract


import cv2
import os
import pytesseract

# Path ke folder frame dan output folder untuk menyimpan frame dengan deteksi teks
output_frames_folder = 'output_frames'
detected_text_frames_folder = 'detected_text_frames'

# Membuat folder untuk menyimpan frame dengan deteksi teks jika belum ada
if not os.path.exists(detected_text_frames_folder):
    os.makedirs(detected_text_frames_folder)

# Konfigurasi Tesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # Ganti dengan path ke tesseract di sistem Anda

# Membaca setiap frame dan mendeteksi tulisan
for frame_filename in sorted(os.listdir(output_frames_folder)):
    frame_path = os.path.join(output_frames_folder, frame_filename)
    frame = cv2.imread(frame_path)
    
    # Konversi frame ke grayscale untuk OCR
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Menggunakan Tesseract OCR untuk mendeteksi teks pada frame
    detected_text = pytesseract.image_to_string(gray_frame)

    # Jika teks terdeteksi, simpan frame ke folder yang berbeda
    if detected_text.strip():
        output_path = os.path.join(detected_text_frames_folder, frame_filename)
        cv2.imwrite(output_path, frame)
        print(f'Teks terdeteksi pada {frame_filename}:')
        print(detected_text)
    else:
        print(f'Tidak ada teks terdeteksi pada {frame_filename}.')

print(f'Proses selesai! Frame dengan teks disimpan di folder {detected_text_frames_folder}')cek