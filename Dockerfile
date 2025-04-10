# Use official Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency file first
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy all app code into container
COPY . .

# Expose the API port
EXPOSE 8000

# Run FastAPI server
CMD ["uvicorn", "inference:app", "--host", "0.0.0.0", "--port", "8000"]
