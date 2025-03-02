# Gunakan Python versi slim untuk mengurangi ukuran image
FROM python:3.9-slim

# Set direktori kerja di dalam container
WORKDIR /app

# Copy file dari project ke container
COPY . /app

# Install dependencies (pastikan requirements.txt ada)
RUN pip install --no-cache-dir -r requirements-live.txt

# Menentukan port yang akan digunakan dalam container
EXPOSE 5000

# Jalankan aplikasi
CMD ["python", "app.py"]
