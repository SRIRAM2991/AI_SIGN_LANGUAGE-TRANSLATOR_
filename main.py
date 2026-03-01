import cv2
import pyttsx3

# ------------------ TEXT TO SPEECH SETUP ------------------
def speak_sentence(sentence_list):
    if sentence_list:
        text = " ".join(sentence_list)

        engine = pyttsx3.init()   # reinitialize every time
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)

        engine.say(text)
        engine.runAndWait()
        engine.stop()
# ----------------------------------------------------------

from detector import HandDetector
from gestures_rules import detect_static_gesture, detect_location
from motion_tracker import MotionTracker
from sentence_build import SentenceBuilder
from config import *
from word_engine import WordEngine
from vocuabulary import VOCABULARY

# Initialize modules
detector = HandDetector()
motion_tracker = MotionTracker()
builder = SentenceBuilder(STABLE_FRAMES, MAX_SENTENCE_LENGTH)
engine = WordEngine()

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    result = detector.detect(frame)

    gesture_tuple = None
    motion = "STILL"
    location = ""

    # Only process if hand is detected
    if result.multi_hand_landmarks:
        hand_landmarks = result.multi_hand_landmarks[0]
        lm = hand_landmarks.landmark

        gesture_tuple = detect_static_gesture(lm)
        motion = motion_tracker.get_motion(lm)
        location = detect_location(lm)

        detector.draw(frame, hand_landmarks)

    # Get word using WordEngine
    word = engine.interpret(gesture_tuple, motion, location) if gesture_tuple else None

    # Update sentence builder
    if word:
        locked, sentence = builder.update(word)
    else:
        locked, sentence = builder.update(None)

    # Display on screen
    cv2.putText(frame, f"Word: {word}", (30,60),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.putText(frame, "Sentence: " + " ".join(sentence), (30,160),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,0), 2)
    cv2.putText(frame, "Press C = Clear | S = Speak | ESC = Exit",
                (30, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200,200,200), 1)

    cv2.imshow("AI Sign Language Translator", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == 27:  # ESC
        break

    if key == ord('c'):  # Press C to clear
        builder.clear()

    if key == ord('s'):  # Press S to speak
        speak_sentence(sentence)

cap.release()
cv2.destroyAllWindows()