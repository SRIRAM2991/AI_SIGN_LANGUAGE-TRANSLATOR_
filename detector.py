import cv2
import mediapipe as mp
from config import *

class HandDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = mp.solutions.hands.Hands(
        model_complexity=0,
        max_num_hands=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )
        self.drawer = mp.solutions.drawing_utils

    def detect(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.hands.process(rgb)

    def draw(self, frame, hand_landmarks):
        self.drawer.draw_landmarks(
            frame,
            hand_landmarks,
            self.mp_hands.HAND_CONNECTIONS
        )
