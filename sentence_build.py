class SentenceBuilder:
    def __init__(self, stable_frames, max_length):
        self.prev = ""
        self.count = 0
        self.locked = ""
        self.sentence = []
        self.last_added = ""
        self.stable_frames = stable_frames
        self.max_length = max_length

    def update(self, gesture):
        if gesture == self.prev:
            self.count += 1
        else:
            self.count = 0
            self.prev = gesture

        if self.count >= self.stable_frames:
            self.locked = gesture

        if self.locked and self.locked != self.last_added:
            self.sentence.append(self.locked)
            self.last_added = self.locked

        if len(self.sentence) > self.max_length:
            self.sentence = self.sentence[-self.max_length:]

        return self.locked, self.sentence
    
    def clear(self):
     self.sentence.clear()