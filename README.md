# 🚀 Drug Consumption Predictor

**Live Demo:** [**https://drug-consumption-predictor.onrender.com/**](https://drug-consumption-predictor.onrender.com/) hosted on Render.com

![Live Demo Screenshot](https://i.imgur.com/your-screenshot-url.png) 
*Catatan: Ganti URL gambar di atas dengan screenshot aplikasi web Anda setelah di-deploy.*

---

### 📝 Ringkasan Proyek

[cite_start]**Drug Consumption Predictor** adalah sebuah aplikasi web berbasis *machine learning* yang bertujuan untuk memprediksi apakah seseorang merupakan pengguna ganja (cannabis) atau bukan. [cite: 4] [cite_start]Prediksi ini dibuat berdasarkan serangkaian data demografis (seperti usia dan pendidikan) dan skor dari tes kepribadian responden. [cite: 5]

[cite_start]Proyek ini menggunakan model **LightGBM** yang telah dilatih pada dataset *'Drug Consumption (Quantified)'* dari UCI Machine Learning Repository. [cite: 6, 7] [cite_start]Pipeline *end-to-end* dibangun untuk mencakup seluruh proses, mulai dari *preprocessing* data hingga *tuning hyperparameter* untuk memastikan performa yang optimal dan proses yang efisien. [cite: 357, 358]

---

### ⚙️ Tech Stack & Tools

-   [cite_start]**Machine Learning**: Scikit-learn, LightGBM, Pandas [cite: 27, 30, 21]
-   **Backend API**: FastAPI, Uvicorn
-   **Frontend**: HTML, JavaScript (Fetch API)
-   **Deployment**: Render.com
-   **Dataset**: [Drug Consumption (Quantified) - UCI Repository](https://archive.ics.uci.edu/dataset/373/drug-consumption-quantified)

---

### 📂 Struktur Proyek

Struktur folder proyek ini dirancang agar sederhana dan mudah dikelola:

```
drug-consumption-predictor/
│
├── 🚀 main.py                 # File utama FastAPI (backend, API endpoint)
├── 🧠 pipeline_konsumsi_narkoba_lightgbm.joblib  # Model pipeline (preprocessor + model)
├── 🏷️ label_encoder.joblib    # Encoder untuk label target
├── 📄 requirements.txt         # Daftar dependensi Python
├── 🌐 index.html              # Halaman antarmuka pengguna (frontend)
├── 📊 example_input.csv       # Contoh file input untuk pengujian
└── 📖 README.md               # Dokumentasi proyek (file ini)
```

---

### 🧠 Model & API

#### Detail Model Machine Learning
[cite_start]Model ini adalah sebuah `LGBMClassifier` yang dioptimalkan menggunakan `GridSearchCV` untuk menemukan kombinasi *hyperparameter* terbaik. [cite: 13, 224] Prosesnya adalah sebagai berikut:
1.  [cite_start]**Preprocessing**: Variabel target asli yang memiliki 7 kelas penggunaan diubah menjadi 2 kelas biner: `User` (pernah menggunakan) dan `Non-user` (tidak pernah menggunakan). [cite: 71, 122] [cite_start]Fitur numerik distandarisasi menggunakan `StandardScaler`. [cite: 11, 215]
2.  [cite_start]**Pipeline**: Seluruh langkah *preprocessing* dan pemodelan digabungkan ke dalam sebuah `Pipeline` Scikit-learn untuk mencegah kebocoran data dan menyederhanakan proses. [cite: 11, 213, 358]
3.  [cite_start]**Evaluasi**: Model terbaik dievaluasi pada data uji dan mencapai **weighted F1-Score sebesar 0.78**. [cite: 269]
4.  [cite_start]**Fitur Penting**: Analisis menunjukkan bahwa skor kepribadian seperti `nscore` (neuroticism), `cscore` (conscientiousness), dan `ascore` (agreeableness) adalah prediktor yang paling berpengaruh. [cite: 298, 300, 302]

#### Detail API
Backend dibangun menggunakan **FastAPI** dan menyediakan satu *endpoint* utama:

-   **Endpoint**: `/predict/`
-   **Metode**: `POST`
-   **Input**: Menerima unggahan file `.csv`. File input harus memiliki kolom yang sama dengan data pelatihan, seperti `age`, `gender`, `education`, `nscore`, dll.
-   **Output**: Mengembalikan respons **JSON** yang berisi hasil prediksi untuk setiap baris dalam CSV, lengkap dengan label (`User`/`Non-user`) dan probabilitas prediksi.

---

### 🚀 Cara Menggunakan Demo

1.  Kunjungi tautan **Live Demo** di atas.
2.  Gunakan file `example_input.csv` yang ada di repositori ini atau siapkan file CSV Anda sendiri dengan format yang sesuai.
3.  Klik tombol "Choose File", pilih file CSV Anda, lalu klik "Predict".
4.  Hasil prediksi akan muncul di bawah tombol dalam format JSON.

---

### 🙋 Kontak

**Muhammad Naufal Aqil**
-   **Email**: muhammadnaufalaqil20@gmail.com
-   **GitHub**: [Naufal22](https://github.com/Naufal22)
-   **LinkedIn**: [Muhammad Naufal Aqil](https://www.linkedin.com/in/muhammad-naufal-aqil-b6114424a/)