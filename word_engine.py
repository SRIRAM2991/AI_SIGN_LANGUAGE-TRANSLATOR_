from vocuabulary import VOCABULARY

class WordEngine:
    def __init__(self):
        self.last_word = None

    def interpret(self, gesture_tuple, motion, location):
        # 1. First, look for a PERFECT match (Gesture + Motion + Location)
        for item in VOCABULARY:
            if item["gesture"] == gesture_tuple and item["motion"] == motion and item["location"] == location:
                return item["word"]

        # 2. If no perfect match, look for just the GESTURE + STILL
        # This fixes the issue where your hand is slightly out of 'CENTER'
        for item in VOCABULARY:
            if item["gesture"] == gesture_tuple and item["motion"] == "STILL":
                return item["word"]

        return None