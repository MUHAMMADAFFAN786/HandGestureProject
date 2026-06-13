import os
import cv2
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

dataset_path = "dataset/leapGestRecog"

X = []
y = []

for person in os.listdir(dataset_path):

    person_path = os.path.join(dataset_path, person)

    if os.path.isdir(person_path):

        for gesture in os.listdir(person_path):

            gesture_path = os.path.join(person_path, gesture)

            if os.path.isdir(gesture_path):

                for image_name in os.listdir(gesture_path):

                    image_path = os.path.join(gesture_path, image_name)

                    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

                    if image is not None:

                        image = cv2.resize(image, (64, 64))

                        X.append(image.flatten())
                        y.append(gesture)

X = np.array(X)
y = np.array(y)

print("Dataset Loaded:", X.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

joblib.dump(model, "gesture_model.pkl")

print("Model Saved Successfully")