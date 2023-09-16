# Aplikasi Scan OCR dengan Flask

Aplikasi ini adalah contoh penggunaan Flask untuk melakukan OCR (Optical Character Recognition) pada gambar yang diunggah. Aplikasi ini khususnya dirancang untuk mendeteksi dan mengekstrak Nomor Induk Kependudukan (NIK) dari teks yang dideteksi dalam gambar.

## Instalasi

1. Pastikan Anda telah menginstal Python. Anda dapat mengunduh Python dari [situs resmi Python](https://www.python.org/downloads/) dan mengikuti panduan instalasinya.

2. Instal paket-paket Python yang diperlukan dengan menjalankan perintah berikut di terminal:

pip install flask opencv-python-headless pytesseract pillow


Pastikan Anda memiliki [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) yang terinstal di sistem Anda. Anda dapat menginstalnya melalui manajer paket sistem (misalnya, `apt-get` di Ubuntu) atau mengunduhnya dari [situs resmi Tesseract OCR](https://github.com/tesseract-ocr/tesseract).

3. Clone repositori ini atau unduh kode sumbernya ke komputer Anda.

4. Buka terminal, navigasikan ke direktori proyek, dan jalankan aplikasi Flask dengan perintah:

python server.py


Aplikasi akan berjalan di `http://localhost:5000`.

## Penggunaan

1. Akses aplikasi melalui browser Anda dengan membuka alamat `http://localhost:5000`.

2. Klik tombol "Pilih File" untuk mengunggah gambar yang berisi teks yang akan dideteksi.

3. Aplikasi akan melakukan OCR pada gambar dan mencoba mengekstrak NIK dari teks yang dideteksi.

4. Jika NIK berhasil diekstrak dan sesuai dengan format yang diharapkan (16 digit angka), informasi akan ditampilkan sebagai respons JSON.

5. Jika NIK tidak terdeteksi atau tidak sesuai, pesan kesalahan akan ditampilkan.

## Kontribusi

Anda dapat berkontribusi pada proyek ini dengan mengirimkan isu (issue) atau permintaan tarik (pull request) melalui GitHub.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat berkas [LICENSE](LICENSE) untuk informasi lebih lanjut.
