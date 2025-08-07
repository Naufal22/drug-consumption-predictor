# Menggunakan image Python dasar yang ringan
FROM python:3.11-slim

# Menetapkan direktori kerja di dalam container
WORKDIR /code

RUN apt-get update && apt-get install -y libgomp1 && rm -rf /var/lib/apt/lists/*

# Menyalin file requirements terlebih dahulu untuk efisiensi caching
COPY ./app/requirements.txt /code/requirements.txt

# Menginstal semua library yang dibutuhkan
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Menyalin seluruh folder aplikasi Anda ke dalam container
COPY ./app /code/app

# Perintah untuk menjalankan aplikasi FastAPI saat container dimulai
# Hugging Face Spaces menggunakan port 7860 secara default
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
