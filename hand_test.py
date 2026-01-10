import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

# Open webcam
cap = cv2.VideoCapture(0)
prev_gesture = ""
gesture_count = 0
STABLE_FRAMES = 8
locked_gesture = ""
sentence = []
last_added_gesture = ""
clear_mode = False
while True:
    success, frame = cap.read()
    if not success:
        break

    # Flip for natural interaction
    frame = cv2.flip(frame, 1)

    # Convert to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

# Exit clear mode only when hand is removed

    if clear_mode and not result.multi_hand_landmarks:
        clear_mode = False


    gesture = "No Hand"

    if result.multi_hand_landmarks:
        hand_landmarks = result.multi_hand_landmarks[0]
        lm = hand_landmarks.landmark

        # Landmark shortcuts
        thumb_tip = lm[4]
        thumb_ip = lm[3]

        index_tip = lm[8]
        index_pip = lm[6]

        middle_tip = lm[12]
        middle_pip = lm[10]

        ring_tip = lm[16]
        ring_pip = lm[14]

        pinky_tip = lm[20]
        pinky_pip = lm[18]

        # Gesture rules
        if (index_tip.y < index_pip.y and
            middle_tip.y < middle_pip.y and
            ring_tip.y < ring_pip.y and
            pinky_tip.y < pinky_pip.y):
            gesture = "HELLO"

        # FOR FRIEND
        elif (index_tip.y > index_pip.y and        
              middle_tip.y < middle_pip.y and      
              ring_tip.y < ring_pip.y and          
              pinky_tip.y < pinky_pip.y):          
              gesture = "FRIEND" 

        # FOR I LOVE YOU
        elif (thumb_tip.y < lm[3].y and 
              index_tip.y < index_pip.y and 
              middle_tip.y > middle_pip.y and 
              ring_tip.y > ring_pip.y and 
              pinky_tip.y < pinky_pip.y):
              gesture = "I LOVE YOU"
       
        # FOR PLEASE
        elif (index_tip.y > index_pip.y and
              middle_tip.y > middle_pip.y and
              ring_tip.y > ring_pip.y and
              pinky_tip.y > pinky_pip.y and
              thumb_tip.y > thumb_ip.y):
              gesture = "PLEASE"

        # FOR SORRY
        elif (index_tip.y > index_pip.y and 
              middle_tip.y > middle_pip.y and 
              ring_tip.y > ring_pip.y and 
              pinky_tip.y > pinky_pip.y and 
              thumb_tip.y > index_pip.y):
              gesture = "SORRY" 

        # FOR STOP
        elif (index_tip.y > index_pip.y and
              middle_tip.y > middle_pip.y and
              ring_tip.y > ring_pip.y and
              pinky_tip.y > pinky_pip.y):
            gesture = "STOP"

        # FOR HELP    
        elif (index_tip.y > index_pip.y and 
               middle_tip.y > middle_pip.y and 
               ring_tip.y > ring_pip.y and 
              pinky_tip.y > pinky_pip.y and 
              thumb_tip.y < thumb_ip.y and      
              thumb_tip.y < index_pip.y):    
              gesture = "HELP"  

        # FOR NO
        elif (index_tip.y > index_pip.y and 
              middle_tip.y > middle_pip.y and 
              ring_tip.y > ring_pip.y):
              gesture = "NO"    

        # FOR YES
        elif thumb_tip.y < thumb_ip.y:
            gesture = "YES"

        # Draw hand skeleton
        mp_draw.draw_landmarks(
            frame,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS
        )

    # Display gesture
    # ---------- STEP 3: Gesture Stabilization ----------

    if gesture == prev_gesture:
        gesture_count += 1
    else:
        gesture_count = 0
        prev_gesture = gesture

    if gesture_count >= STABLE_FRAMES and gesture != "No Hand":
        locked_gesture = gesture

    # Display locked gesture
    cv2.putText(frame, f"Gesture: {locked_gesture}",
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.2,
                (0, 255, 0),
                2)
    
    # ---------- STEP 4: Sentence Formation ----------

    if locked_gesture and locked_gesture != last_added_gesture:
        sentence.append(locked_gesture)
        last_added_gesture = locked_gesture

    status = "Hand Detected" if result.multi_hand_landmarks else "No Hand"

    cv2.putText(frame, f"Status: {status}",
            (30, 140),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (200, 200, 200),
            2)
    

# Limit sentence length
    if len(sentence) > 8:
        sentence = sentence[-8:]


    cv2.putText(frame, "Sentence: " + " ".join(sentence),
            (30, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (255, 255, 0),
            2)

    cv2.imshow("Sign Language Recognition - Step 3", frame)

    
    key = cv2.waitKey(10) & 0xFF

    if key == 27:  # ESC
        break

    if key == ord('c') or key == ord('C'):
       sentence.clear()
       last_added_gesture = ""
       locked_gesture = ""
       prev_gesture = ""
       gesture_count = 0
       clear_mode = True   # 👈 BLOCK GESTURE ADDING


cap.release()
cv2.destroyAllWindows()
