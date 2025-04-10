# models/train_model.py

import tensorflow as tf
from tensorflow.keras import layers, models

# 1. Load MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# 2. Normalize pixel values to 0–1
x_train, x_test = x_train / 255.0, x_test / 255.0

# 3. Build the model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),      # Flatten 2D to 1D
    layers.Dense(128, activation='relu'),      # Hidden layer
    layers.Dropout(0.2),                        # Prevent overfitting
    layers.Dense(10, activation='softmax')     # Output: 10 digits
])

# 4. Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 5. Train the model
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# 6. Save the trained model
model.save('models/model.keras')
print("✅ Model saved as models/model.keras")
