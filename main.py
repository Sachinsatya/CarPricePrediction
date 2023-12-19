from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Load the trained model
model = joblib.load('model/car_price_model.pkl')

# Define request model
class CarFeatures(BaseModel):
    Year: int
    Present_Price: float
    Kms_Driven: int
    Fuel_Type: str
    Seller_Type: str
    Transmission: str
    Owner: int

# Endpoint to make predictions
@app.post("/predict")
def predict_price(car: CarFeatures):
    features = [car.Year, car.Present_Price, car.Kms_Driven, car.Fuel_Type, car.Seller_Type, car.Transmission, car.Owner]
    prediction = model.predict([features])[0]
    return {"predicted_price": prediction}
