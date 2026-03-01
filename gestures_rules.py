# gestures_rules.py
def detect_static_gesture(lm):
    """
    Returns tuple of fingers (thumb, index, middle, ring, pinky) as 0=down, 1=up
    lm: mediapipe hand landmarks
    """
    thumb = 1 if lm[4].x < lm[3].x else 0   # adjust for hand orientation
    index = 1 if lm[8].y < lm[6].y else 0
    middle = 1 if lm[12].y < lm[10].y else 0
    ring = 1 if lm[16].y < lm[14].y else 0
    pinky = 1 if lm[20].y < lm[18].y else 0

    return (thumb, index, middle, ring, pinky)


def detect_location(lm):
    wrist = lm[0]
    x, y = wrist.x, wrist.y

    if y < 0.2:
        return "TOP"
    elif y > 0.8:
        return "BOTTOM"
    elif x < 0.2:
        return "LEFT"
    elif x > 0.8:
        return "RIGHT"
    else:
        return "CENTER"
