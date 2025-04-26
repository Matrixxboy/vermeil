import tensorflow as tf

# Load the model
model_path = 'fruit_classifier_model.h5'
model = tf.keras.models.load_model(model_path)

# Print the model summary to check the output layer
model.summary()

# Create a dummy input image (same shape as expected by the model)
import numpy as np
dummy_image = np.random.rand(1, 224, 224, 3)  # Assuming the model expects 224x224 RGB images

# Make a prediction with the model
predictions = model.predict(dummy_image)

# Print the predicted class probabilities
print(f"Prediction probabilities: {predictions}")

# Print the shape of the predictions to see how many classes it predicts
print(f"Predictions shape: {predictions.shape}")

# If the model predicts multiple classes, it will show the confidence for each class
# You can print the most probable class and its confidence
predicted_class = np.argmax(predictions)
print(f"Predicted class index: {predicted_class}")
