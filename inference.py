# inference.py

import tensorflow as tf
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np

# Load the trained model
model = tf.keras.models.load_model("models/model.keras")

# Define the input schema
class PredictRequest(BaseModel):
    data: list  # Accepts a list of 28x28 floats or multiple such samples

# Create FastAPI app
app = FastAPI(title="ML Inference API")

@app.post("/predict")
async def predict(request: PredictRequest):
    try:
        # Convert to NumPy array
        input_data = np.array(request.data)

        # Normalize if needed (e.g., if original values are 0-255)
        input_data = input_data / 255.0

        # Ensure proper shape for single image: (1, 28, 28)
        if input_data.ndim == 2:
            input_data = np.expand_dims(input_data, axis=0)

        # If model expects (batch, 28, 28, 1), reshape:
        if input_data.ndim == 3:
            input_data = np.expand_dims(input_data, axis=-1)

        predictions = model.predict(input_data)
        predicted_classes = np.argmax(predictions, axis=1).tolist()

        return {"predictions": predicted_classes}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
