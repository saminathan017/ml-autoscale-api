import requests
import json
import numpy as np

data = {
    "data": np.random.rand(28, 28).tolist()
}

res = requests.post("http://127.0.0.1:8000/predict", json=data)
print("Prediction:", res.json())
