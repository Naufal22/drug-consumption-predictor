from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib

#Load model dan encoder
model = joblib.load("pipeline_konsumsi_narkoba_lightgbm.joblib")
label_encoder = joblib.load("label_encoder.joblib")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict-batch")
async def predict_batch(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    
    #Validasi kolom
    excepted_columns = [
        "age", "gender", "education", "country", "ethnicity",
        "nscore", "escore", "oscore", "ascore", "cscore",
        "impuslive", "ss"
    ]
    if not all(col in df.columns for col in excepted_columns):
        return {"eror": "Kolom input tidak sesuai."}

    pred = model.predict(df)
    prob = model.predict_proba(df)[:,1]
    label = label_encoder.inverse_transform(pred)

    result = [
        {"prediction": l, "probability":round(float(p),4)}
        for l,p in zip(label, prob)
    ]

    return {
        "predictions": result,
        "total": len(result),
        "positives": sum(1 for r in label if r == "User"),
        "negatives": sum(1 for r in label if r == "Non-user")
    }