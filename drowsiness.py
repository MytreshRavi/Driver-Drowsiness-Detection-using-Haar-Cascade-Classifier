from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread
import numpy as np
import imutils
import time
import dlib
import cv2
import pygame

# -------- CONFIG --------
SHAPE_PREDICTOR = "shape_predictor_68_face_landmarks.dat"
ALARM_PATH = "alarm.mp3"
WEBCAM = 0

EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 48


def sound_alarm(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)


def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)


def run_drowsiness_detection():
    print("[INFO] Loading face detector...")
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(SHAPE_PREDICTOR)

    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

    COUNTER = 0
    ALARM_ON = False

    print("[INFO] Starting camera...")
    vs = VideoStream(src=WEBCAM).start()
    time.sleep(1.0)

    start_time = time.time()

    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=450)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        rects = detector(gray, 0)

        for rect in rects:
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]

            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)
            ear = (leftEAR + rightEAR) / 2.0

            if ear < EYE_AR_THRESH:
                COUNTER += 1

                if COUNTER >= EYE_AR_CONSEC_FRAMES:
                    if not ALARM_ON:
                        ALARM_ON = True
                        t = Thread(target=sound_alarm, args=(ALARM_PATH,))
                        t.daemon = True
                        t.start()

                    vs.stop()
                    return "Drowsy"

            else:
                COUNTER = 0
                ALARM_ON = False

                if time.time() - start_time > 5:
                    vs.stop()
                    return "Awake"
