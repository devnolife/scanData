import os
import uuid
import json
from PIL import Image
import pytesseract
from pytesseract import Output
import numpy as np
import cv2
import re
from flask import Flask, request, redirect, jsonify, url_for, send_from_directory
from flask_cors import CORS 


app = Flask(__name__)
CORS(app)  # Aktifkan CORS untuk aplikasi Flask Anda

app.config['UPLOAD_FOLDER'] = 'static/images'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def save_ocr_result_to_file(text, filename="output.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

def clean_ocr_text(text):
    cleaned_text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
    return cleaned_text

@app.route('/')
def index():
    return 'Scan OCR with Python Flask! by devnolife'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'File tidak ditemukan dalam permintaan!'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'Nama file kosong!'}), 400
    if file and allowed_file(file.filename):
        unique_filename = str(uuid.uuid4()) + '.' + file.filename.rsplit('.', 1)[1].lower()
        filename = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filename)

        img = cv2.imread(filename)
        norm_img = np.zeros((img.shape[0], img.shape[1]))
        image = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
        image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)[1]
        image = cv2.GaussianBlur(image, (1, 1), 0)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        os.environ['TESSDATA_PREFIX'] = '/usr/share/tesseract-ocr/4.00/tessdata/'

        results = pytesseract.image_to_string(image, lang="ind")
        cleaned_results = clean_ocr_text(results)
        cleaned_results = cleaned_results.replace(" ", "")

        # Mencari NIK dengan regex
        nik_match = re.search(r'NIK:(\d{16})', cleaned_results)
        if nik_match:
            nik = nik_match.group(1)
            # Validasi NIK
            if len(nik) == 16:
                response_data = {
                    'message': 'File berhasil diupload!',
                    'filename': unique_filename,
                    'text': cleaned_results,
                    'nik': nik
                }
                return jsonify(response_data), 200

        # Jika "NIK" tidak ditemukan atau NIK tidak sesuai, beri pesan kesalahan
        response_data = {
            'message': 'NIK tidak sesuai atau tidak terdeteksi. Mohon unggah foto ulang dengan NIK yang jelas.',
            'filename': unique_filename,
            'text': cleaned_results
        }
        return jsonify(response_data), 400
    else:
        return jsonify({'message': 'File yang diupload tidak valid!'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


import cv2
import pytesseract
import sys
from ktpocr import KTPOCR

def read(ktp_path):
    img = cv2.imread(ktp_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
    result = pytesseract.image_to_string((threshed), lang="ind")
    final = []
    for word in result.split("\n"):
        if "”—" in word:
            word = word.replace("”—", ":")
        if "NIK" in word:
            nik_char = word.split()
        if "?" in word:
            word = word.replace("?", "7") 
        final.append(word)
    return final

if __name__ == "__main__":  
    try:  
        ktppath = sys.argv[1]    
    except:
        ktppath = 'vianda.jpg'  #default image
    if ktppath:
        ocr = KTPOCR(ktppath)
        word = ocr.to_json()
        print(word)