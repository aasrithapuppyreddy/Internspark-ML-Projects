from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("model.pkl")

@app.get("/")
def home():
    return {"message": "API is working"}

@app.post("/predict")
def predict(data: list):
    prediction = model.predict([data])
    return {"prediction": int(prediction[0])}