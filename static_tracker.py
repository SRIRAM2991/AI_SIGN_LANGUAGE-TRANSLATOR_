def detect_static(lm):
    
    index_tip = lm[8]
    index_pip = lm[6]
    middle_tip = lm[12]
    middle_pip = lm[10]
    ring_tip = lm[16]
    ring_pip = lm[14]
    pinky_tip = lm[20]
    pinky_pip = lm[18]

    open_fingers = (
        index_tip.y < index_pip.y and
        middle_tip.y < middle_pip.y and
        ring_tip.y < ring_pip.y and
        pinky_tip.y < pinky_pip.y
    )

    closed_fingers = (
        index_tip.y > index_pip.y and
        middle_tip.y > middle_pip.y and
        ring_tip.y > ring_pip.y and
        pinky_tip.y > pinky_pip.y
    )

    if open_fingers:
        return "OPEN"

    if closed_fingers:
        return "FIST"

    return "UNKNOWN"
