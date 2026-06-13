import cv2
import numpy as np
import joblib

# Load trained model
model = joblib.load("gesture_model.pkl")

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Mirror image
    frame = cv2.flip(frame, 1)

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Resize image to match training data
    roi = cv2.resize(gray, (64, 64))

    # Flatten image
    features = roi.flatten().reshape(1, -1)

    # Predict gesture
    prediction = model.predict(features)

    # Display prediction
    cv2.putText(
        frame,
        f"Gesture: {prediction[0]}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Show webcam
    cv2.imshow("Hand Gesture Recognition", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()