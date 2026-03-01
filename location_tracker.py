def detect_location(lm):
    middle_tip = lm[12]
    x = middle_tip.x
    y = middle_tip.y

    # Vertical zones first (more important)
    if y < 0.35:
        return "TOP"

    if y > 0.75:
        return "BOTTOM"

    # Then horizontal
    if x < 0.25:
        return "LEFT"

    if x > 0.75:
        return "RIGHT"

    return "CENTER"
