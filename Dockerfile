# Menggunakan base image Python versi 3.9
FROM python:3.9

# Menetapkan direktori kerja di dalam container
WORKDIR /app

# Menyalin semua file proyek ke dalam container, termasuk venv
COPY . .  

# Menentukan port yang akan digunakan dalam container
EXPOSE 5000

# Menjalankan aplikasi Flask dengan virtual environment yang sudah ada
CMD ["sh", "-c", ". venv/bin/activate && python app.py"]
