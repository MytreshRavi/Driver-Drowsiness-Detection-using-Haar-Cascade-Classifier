
Project Title: Drowsiness Detection Using Eye Aspect Ratio (EAR) via Webcam
# Drowsiness Detection System

## Project Description
This project is a **Drowsiness Detection System** that uses facial landmark detection to monitor the user's eye aspect ratio (EAR) and detect drowsiness. If drowsiness is detected:
1. A "DROWSINESS ALERT!" message is displayed on the screen.
2. An alarm sound (`alarm-original.wav`) is played to alert the user.

## Features
- **Facial Landmark Detection:** Uses `dlib`'s pre-trained `shape_predictor_68_face_landmarks.dat` model.
- **Eye Aspect Ratio (EAR):** Calculates EAR to detect if the user's eyes are closed for a prolonged period.
- **Real-Time Video Stream:** Processes frames from the webcam in real-time.
- **Audio Alert:** Plays an alarm sound whenever drowsiness is detected.

## Dependencies
- Python 3.10
- Libraries:
- `dlib`
- `opencv`
- `numpy`
- `scipy`
- `imutils`
- `pygame`

## Troubleshooting
- If you encounter issues with `dlib` installation, ensure that you have installed the precompiled `.whl` file as instructed.
- If the alarm sound does not play, verify that the `pygame` library is installed and the `.wav` file is accessible.
- Ensure that the `shape_predictor_68_face_landmarks.dat` file is in the correct location.

## Setup Instructions
### 1. Install Anaconda
- Download and install Anaconda from [https://www.anaconda.com/](https://www.anaconda.com/).

### 2. Create a Conda Environment
- Open the terminal or Anaconda Prompt and run the following commands:
  ```bash
  conda create -n myenv python=3.10
  conda activate myenv
  ```

### 3. Install Required Libraries
(https://github.com/datamagic2020/Install-dlib.git) Try getting from here
- Navigate to the `Dlib_Windows_Python3.x-main` folder:
  ```bash
  cd Dlib_Windows_Python3.x-main
  python -m pip install dlib-19.22.99-cp310-cp310-win_amd64.whl
  conda install -c conda-forge dlib opencv numpy scipy imutils pygame
  ```

### 4. Navigate to the Project Folder
- Go back to the main project folder:
  ```bash
  cd ..
  ```

### 5. Run the Application
- Use the following command to run the project:
  ```bash
  python project.py --shape-predictor shape_predictor_68_face_landmarks.dat --alarm alarm-original.wav
  ```
This includes the necessary steps for creating a Conda environment with Python 3.10 on systems that have Python 3.11.12 installed.

