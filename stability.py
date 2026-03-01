class StabilityFilter:
    def __init__(self, required_frames=8):
        self.required_frames = required_frames
        self.last_value = None
        self.counter = 0
        self.stable_value = None

    def update(self, new_value):

        # If nothing detected → reset softly
        if new_value is None:
            self.counter = 0
            self.last_value = None
            return self.stable_value

        # If same as previous frame
        if new_value == self.last_value:
            self.counter += 1
        else:
            self.counter = 1   # start counting from 1
            self.last_value = new_value

        # Lock only when stable enough
        if self.counter >= self.required_frames:
            if self.stable_value != new_value:
                self.stable_value = new_value
                return self.stable_value

        return None