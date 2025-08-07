# 🚀 Drug Consumption Predictor

**Live Demo:** [**https://huggingface.co/spaces/puunnu/drug-consumption-predictor**](https://huggingface.co/spaces/puunnu/drug-consumption-predictor)

![Live Demo Screenshot](prediksi-ganja.png)


---

### 📝 Ringkasan Proyek

**Drug Consumption Predictor** adalah sebuah aplikasi web berbasis *machine learning* yang bertujuan untuk memprediksi apakah seseorang merupakan pengguna ganja (cannabis) atau bukan. Prediksi ini dibuat berdasarkan serangkaian data demografis (seperti usia dan pendidikan) dan skor dari tes kepribadian responden.

Proyek ini menggunakan model **LightGBM** yang telah dilatih pada dataset *'Drug Consumption (Quantified)'* dari UCI Machine Learning Repository. Sebuah pipeline *end-to-end* dibangun untuk mencakup seluruh proses, mulai dari *preprocessing* data hingga *tuning hyperparameter* untuk memastikan performa yang optimal. Aplikasi ini kemudian di-deploy sebagai layanan web interaktif di Hugging Face Spaces.

---

### ⚙️ Tech Stack & Tools

-   **Machine Learning**: Scikit-learn, LightGBM, Pandas, Joblib
-   **Backend & Frontend**: FastAPI, Uvicorn, HTML, JavaScript
-   **Deployment**: Docker, Hugging Face Spaces
-   **Dataset**: [Drug Consumption (Quantified) - UCI Repository](https://archive.ics.uci.edu/dataset/373/drug-consumption-quantified)

---

### 📂 Struktur Proyek

Struktur proyek ini dirancang untuk memisahkan kode aplikasi dari file-file lainnya, yang merupakan praktik pengembangan yang baik.

```
/
├── app/
│   ├── main.py                 # File utama FastAPI (Backend & Frontend Server)
│   ├── index.html              # Halaman antarmuka pengguna (Frontend)
│   ├── pipeline_konsumsi_narkoba_lightgbm.joblib  # Model pipeline terlatih
│   ├── label_encoder.joblib    # Encoder untuk label target
│   └── requirements.txt        # Daftar dependensi Python
│
├── Dockerfile                  # Instruksi untuk membangun lingkungan aplikasi
├── daftar_fitur_untuk_prediksi.csv          # Contoh file input untuk pengujian
├── drug_consumption_classification_pipeline_gridsearch.ipynb       
└── README.md                   # Dokumentasi proyek (file ini)

```

---

### 🧠 Model & API

#### Detail Model Machine Learning
Model ini adalah sebuah `LGBMClassifier` yang dioptimalkan menggunakan `GridSearchCV`. Prosesnya adalah sebagai berikut:
1.  **Preprocessing**: Variabel target asli yang memiliki 7 kelas penggunaan diubah menjadi 2 kelas biner: `User` (pernah menggunakan) dan `Non-user` (tidak pernah menggunakan). Fitur numerik distandarisasi menggunakan `StandardScaler`.
2.  **Pipeline**: Seluruh langkah *preprocessing* dan pemodelan digabungkan ke dalam sebuah `Pipeline` Scikit-learn untuk mencegah kebocoran data.
3.  **Evaluasi**: Model terbaik dievaluasi pada data uji dan mencapai **weighted F1-Score sebesar 0.78**.
4.  **Fitur Penting**: Analisis menunjukkan bahwa skor kepribadian seperti `nscore` (neuroticism), `cscore` (conscientiousness), dan `ascore` (agreeableness) adalah prediktor yang paling berpengaruh.

#### Detail Aplikasi Web
Aplikasi ini dibangun menggunakan **FastAPI** dan melayani dua hal utama:

* **Frontend (`GET /`)**: Saat pengguna mengunjungi URL utama, server akan menyajikan halaman `index.html` yang interaktif.
* **API Backend (`POST /predict-batch`)**: Halaman frontend akan mengirim file CSV ke endpoint ini. Backend kemudian memproses file menggunakan model yang telah dimuat dan mengembalikan hasil prediksi dalam format JSON untuk ditampilkan kembali di halaman web.

---

### 🚀 Cara Menggunakan Demo

1.  Kunjungi tautan **Live Demo** di atas.
2.  Gunakan file `daftar_fitur_untuk_prediksi.csv` yang ada di repositori ini atau siapkan file CSV Anda sendiri dengan format yang sesuai.
3.  Pada halaman web, klik tombol untuk memilih file, lalu klik "Prediksi".
4.  Hasil prediksi akan muncul di bawah tombol dalam format yang mudah dibaca.

---

### 🙋 Kontak

**Muhammad Naufal Aqil**
-   **Email**: muhammadnaufalaqil20@gmail.com
-   **GitHub**: [Naufal22](https://github.com/Naufal22)
-   **LinkedIn**: [Muhammad Naufal Aqil](https://www.linkedin.com/in/muhammad-naufal-aqil-b6114424a/)
