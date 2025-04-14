# Use official Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency file first
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# 🔥 Install stress tool to simulate CPU load for autoscaling
RUN apt-get update && apt-get install -y stress

# Copy all app code into container
COPY . .

# Expose the API port
EXPOSE 8000

# Run FastAPI server
CMD ["uvicorn", "inference:app", "--host", "0.0.0.0", "--port", "8000"]
