# camera_classification.py
import cv2
import numpy as np
import tensorflow as tf
import os

# Load the saved model
model = tf.keras.models.load_model('Model/fruit_classifier_model.h5')

# Load the class labels
class_labels = sorted(os.listdir('fruits_data/test'))  # Same as training folder

# Function to preprocess the camera frame
def preprocess_frame(frame, target_size=(224, 224)):
    img = cv2.resize(frame, target_size)
    img = img.astype('float32') / 255.0  # Normalize
    img = np.expand_dims(img, axis=0)    # Add batch dimension
    return img

# Start webcam
cap = cv2.VideoCapture(0)  # 0 for default camera

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess frame
    preprocessed = preprocess_frame(frame)

    # Predict
    predictions = model.predict(preprocessed)
    predicted_index = np.argmax(predictions)
    confidence = np.max(predictions)
    predicted_label = class_labels[predicted_index]

    # Show prediction on the frame
    label_text = f"{predicted_label} ({confidence * 100:.2f}%)"
    cv2.putText(frame, label_text, (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Fruit Classifier', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
