# --------------------------------------------------------------------------
# 1. IMPORTS - Mengimpor semua library yang dibutuhkan
# --------------------------------------------------------------------------
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib
from pathlib import Path

# --------------------------------------------------------------------------
# 2. INISIALISASI & MEMUAT MODEL
# Menggunakan pathlib untuk memastikan path ke file model selalu benar.
# --------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve(strict=True).parent

try:
    model = joblib.load(Path(BASE_DIR, "pipeline_konsumsi_narkoba_lightgbm.joblib"))
    label_encoder = joblib.load(Path(BASE_DIR, "label_encoder.joblib"))
except FileNotFoundError:
    raise RuntimeError("Model/Encoder file not found. Pastikan file .joblib ada di direktori yang sama dengan main.py")

# Inisialisasi aplikasi FastAPI
app = FastAPI(title="Drug Consumption Prediction API")

# Middleware untuk mengizinkan Cross-Origin Resource Sharing (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------------------------------
# 3. ENDPOINT UNTUK FRONTEND
# --------------------------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
    """Menyajikan halaman frontend index.html."""
    html_path = BASE_DIR / "index.html"
    try:
        return HTMLResponse(content=html_path.read_text())
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File index.html tidak ditemukan. Pastikan file ada di dalam folder 'app'.")


# --------------------------------------------------------------------------
# 4. ENDPOINT UNTUK API PREDIKSI 
# --------------------------------------------------------------------------
@app.post("/predict-batch")
async def predict_batch(file: UploadFile = File(...)):
    """Menerima file CSV, melakukan prediksi, dan mengembalikan hasil."""
    
    # Cek apakah file yang diunggah adalah CSV
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Format file tidak valid. Harap unggah file .csv")

    try:
        df = pd.read_csv(file.file)
    except Exception:
        raise HTTPException(status_code=400, detail="Gagal memproses file. Pastikan formatnya adalah CSV yang valid.")

    # Validasi kolom input
    expected_columns = [
        "age", "gender", "education", "country", "ethnicity",
        "nscore", "escore", "oscore", "ascore", "cscore",
        "impuslive", "ss"
    ]
    missing_cols = set(expected_columns) - set(df.columns)
    if missing_cols:
        raise HTTPException(
            status_code=422, # Unprocessable Entity
            detail={
                "error": "Kolom input pada file CSV tidak sesuai.",
                "missing_columns": list(missing_cols),
                "expected_columns": expected_columns
            }
        )
    
    try:
        # Lakukan prediksi
        pred = model.predict(df[expected_columns])
        prob = model.predict_proba(df[expected_columns])
        label = label_encoder.inverse_transform(pred)

        # Ambil probabilitas untuk kelas "User"
        user_class_index = list(label_encoder.classes_).index('User')
        user_prob = prob[:, user_class_index]

        result = [
            {"prediction": l, "probability": round(float(p), 4)}
            for l, p in zip(label, user_prob)
        ]

        return {
            "predictions": result,
            "total_rows": len(result),
            "user_count": sum(1 for r in label if r == "User"),
            "non_user_count": sum(1 for r in label if r == "Non-user")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Terjadi error internal saat prediksi: {e}")
