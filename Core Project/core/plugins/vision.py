import cv2
import numpy as np
import tensorflow as tf
import os

# Load model
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'fruit_classifier_model.h5')
model = tf.keras.models.load_model(model_path)

# Your classes
class_names = ['apple', 'avacado','avocado', 'banana', 'cherry', 'kiwi','mango', 'orange', 'pineapple', 'strawberry', 'watermelon']

# Global variables
cap = None
vision_active = False
latest_prediction = None
latest_confidence = None

def start_vision_mode():
    global cap, vision_active
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Failed to start vision mode.")
        return "Error: Webcam not accessible."

    vision_active = True
    return "Vision mode activated. Ready for your scan command."

def show_camera_feed():
    """ Continuously show live camera feed with live predictions and bounding box. """
    global cap, vision_active, latest_prediction, latest_confidence

    while vision_active and cap is not None and cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        h, w, _ = frame.shape

        # Define center box for scanning (224x224)
        box_size = 224
        x1 = w // 2 - box_size // 2
        y1 = h // 2 - box_size // 2
        x2 = x1 + box_size
        y2 = y1 + box_size

        roi = frame[y1:y2, x1:x2]

        # Prediction
        img = cv2.resize(roi, (224, 224))
        img = img / 255.0
        img = np.expand_dims(img, axis=0)

        predictions = model.predict(img, verbose=0)

        # Check if prediction shape matches the number of classes
        if predictions.shape[1] != len(class_names):
            print(f"Error: The model output has an unexpected number of classes. Expected: {len(class_names)}, Got: {predictions.shape[1]}")
            continue  # Skip this frame

        confidence = np.max(predictions)
        predicted_class = class_names[np.argmax(predictions)]

        latest_prediction = predicted_class
        latest_confidence = confidence

        # Draw rectangle around the scanning region (ROI)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Label text
        label = f"{predicted_class} ({confidence*100:.2f}%)"
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Display live feed with the bounding box
        cv2.imshow('Vermeil Vision Mode', frame)

        # Close window if 'q' is pressed manually
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    if cap is not None:
        cap.release()
    cv2.destroyAllWindows()

def scan_current_frame():
    """ When user says 'scan this', speak latest prediction. """
    global latest_prediction, latest_confidence

    if latest_prediction is None or latest_confidence is None:
        return "No object detected yet."

    # return f"This looks like {latest_prediction} with {latest_confidence*100:.2f}% confidence."
    return f"This looks like {latest_prediction}"

def close_vision_mode():
    """ Properly close the camera and stop vision feed. """
    global cap, vision_active
    vision_active = False

    if cap is not None:
        cap.release()
        cap = None

    cv2.destroyAllWindows()
    return "Vision mode deactivated."

def process_vision_commands(command):
    """ Decide what to do based on command: scan or close vision """
    command = command.lower()
    if "scan this" in command:
        return scan_current_frame()
    elif "close vision" in command:
        return close_vision_mode()
    else:
        return "Unknown vision command."
