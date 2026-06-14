# Hand Gesture Recognition System

## SkillCraft Technology Internship - Task 1

### Project Overview

This project is a **real-time Hand Gesture Recognition System** developed as part of **Task 1** during my internship at **SkillCraft Technology**. The system uses **Machine Learning** and **Computer Vision** techniques to identify and classify different hand gestures through a webcam feed.

The goal of this project is to enable intuitive **human-computer interaction** using gesture-based control systems.

---

## Features

* Real-time hand gesture recognition using a webcam
* Machine Learning based gesture classification
* Custom-trained gesture recognition model
* User-friendly implementation
* Supports multiple predefined hand gestures

---

## Technologies Used

* Python
* OpenCV
* NumPy
* Scikit-learn
* Joblib
* Git & GitHub

---

## Project Structure

```
HandGestureProject/
│
├── train.py
├── predict.py
├── gesture_model.pkl
├── README.md
└── dataset/
```

---

## Dataset

The project uses the **LeapGestRecog** dataset for training and testing the machine learning model.

Recognized gestures include:

* Palm
* L
* Fist
* Fist Moved
* Thumb
* Index
* OK
* Palm Moved
* C
* Down

---

## Installation

### Clone the repository

```bash
git clone https://github.com/MUHAMMADAFFAN786/HandGestureProject.git
```

### Navigate to the project directory

```bash
cd HandGestureProject
```

### Install required libraries

```bash
pip install opencv-python numpy scikit-learn joblib
```

---

## Training the Model

Run the following command to train the model:

```bash
python train.py
```

After successful training, the model file `gesture_model.pkl` will be generated.

---

## Running the Project

To start real-time gesture recognition:

```bash
python predict.py
```

Press **Q** to close the webcam window.

---

## Learning Outcomes

Through this project, I gained hands-on experience in:

* Machine Learning model development
* Computer Vision applications
* Real-time image processing
* Python programming
* Git and GitHub version control

---

## Internship Information

**Internship Provider:** SkillCraft Technology

**Task:** Task 1 – Hand Gesture Recognition System

---

## Author

**Muhammad Affan**

GitHub: https://github.com/MUHAMMADAFFAN786

LinkedIn: [www.linkedin.com/in/muhammad-affan-49a127368](http://www.linkedin.com/in/muhammad-affan-49a127368)

---

## Acknowledgements

I would like to thank **SkillCraft Technology** for providing this valuable opportunity to enhance my practical skills in Machine Learning and Computer Vision.
