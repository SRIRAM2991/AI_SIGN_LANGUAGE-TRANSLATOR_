from config import MOTION_THRESHOLD


class MotionTracker:
    def __init__(self):
        self.prev_x = None
        self.prev_y = None

        self.confirmed_motion = "STILL"
        self.motion_lock_frames = 0
        self.lock_duration = 6


    def get_motion(self, lm):
        wrist = lm[0]
        detected_motion = "STILL"

        if self.prev_x is not None:
            dx = wrist.x - self.prev_x
            dy = wrist.y - self.prev_y

            speed = abs(dx) + abs(dy)

            # Ignore violent shaking
            if speed <= 0.25:
                if abs(dx) > MOTION_THRESHOLD:
                    detected_motion = "RIGHT" if dx > 0 else "LEFT"
                elif abs(dy) > MOTION_THRESHOLD:
                    detected_motion = "DOWN" if dy > 0 else "UP"

        # Lock motion for a few frames
        if detected_motion != "STILL":
            self.confirmed_motion = detected_motion
            self.motion_lock_frames = self.lock_duration

        if self.motion_lock_frames > 0:
            self.motion_lock_frames -= 1
        else:
            self.confirmed_motion = "STILL"

        self.prev_x = wrist.x
        self.prev_y = wrist.y

        return self.confirmed_motion
