# inference.py

import tensorflow as tf
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np

# Load the trained model
model = tf.keras.models.load_model("models/model.keras")

# Define the input schema
class PredictRequest(BaseModel):
    data: list  # Expects a list of 28x28 pixel values (flattened or nested)

# Create FastAPI app
app = FastAPI(title="ML Inference API")

@app.post("/predict")
async def predict(request: PredictRequest):
    try:
        # Ensure input is a NumPy array and reshaped correctly
        input_data = np.array(request.data)
        
        # Handle if user sends just one image (single 28x28)
        if input_data.ndim == 2:
            input_data = np.expand_dims(input_data, axis=0)

        predictions = model.predict(input_data)
        predicted_classes = np.argmax(predictions, axis=1).tolist()

        return {"predictions": predicted_classes}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
