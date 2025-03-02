# Menggunakan base image Python versi 3.9
FROM python:3.9

# Menetapkan direktori kerja di dalam container
WORKDIR /app

# Menyalin semua file dari direktori proyek ke dalam container
COPY . .

# Mengaktifkan virtual environment dan menginstal dependencies
RUN . venv/bin/activate 

# Menentukan port yang akan digunakan di dalam container
EXPOSE 5000

# Menjalankan aplikasi Flask saat container dijalankan
CMD ["sh", "-c", ". venv/bin/activate && python app.py"]
