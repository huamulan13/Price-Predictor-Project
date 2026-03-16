from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="E-Commerce Price Predictor API")

try:
    model = joblib.load("app/model.pkl")
except:
    model = None
    print("Warning: model.pkl belum ditemukan!")

class ProductSpecs(BaseModel):
    brand: str
    ram: int
    storage: int
    condition_score: float

@app.get("/")
def home():
    return {"message": "Welcome to Price Predictor API!"}

@app.post("/predict")
def predict_price(data: ProductSpecs):
    if model is None:
        return {"error": "Model tidak tersedia. Hubungi Data Scientist-mu!"}

    df_input = pd.DataFrame([data.dict()])

    prediction = model.predict(df_input)
    
    return {
        "status": "success",
        "predicted_price": round(float(prediction[0]), 2)
    }