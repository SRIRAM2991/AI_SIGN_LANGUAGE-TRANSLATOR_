# vocuabulary.py
# Each gesture tuple: (thumb, index, middle, ring, pinky)
# Motion: "UP", "DOWN", "LEFT", "RIGHT", "STILL"
# Location: "TOP", "BOTTOM", "LEFT", "RIGHT", "CENTER"

VOCABULARY = [
    # Static gestures
    {"gesture": (0,0,0,0,0), "motion": "STILL", "location": "CENTER", "word": "NO"},
    {"gesture": (1,0,0,0,0), "motion": "STILL", "location": "CENTER", "word": "YES"},
    {"gesture": (0,1,0,0,0), "motion": "STILL", "location": "CENTER", "word": "THANK YOU"},
    {"gesture": (1,1,0,0,0), "motion": "STILL", "location": "CENTER", "word": "YOU"},
    {"gesture": (0,1,1,1,1), "motion": "STILL", "location": "CENTER", "word": "HELLO"},
    {"gesture": (1,0,1,1,1), "motion": "STILL", "location": "CENTER", "word": "FRIEND"},
    {"gesture": (1,0,0,0,1), "motion": "STILL", "location": "CENTER", "word": "LIKE"},
    {"gesture": (1,1,1,0,0), "motion": "STILL", "location": "CENTER", "word": "PEACE"},
    {"gesture": (0,0,0,0,1), "motion": "STILL", "location": "CENTER", "word": "WHO"},
    {"gesture": (0,1,0,0,1), "motion": "STILL", "location": "CENTER", "word": "I LOVE YOU"},

    # Motion gestures
    {"gesture": (0,1,1,1,1), "motion": "UP", "location": "CENTER", "word": "COME"},
    {"gesture": (0,1,1,1,1), "motion": "DOWN", "location": "CENTER", "word": ""},
    {"gesture": (0,1,1,1,1), "motion": "LEFT", "location": "CENTER", "word": "LEFT"},
    {"gesture": (0,1,1,1,1), "motion": "RIGHT", "location": "CENTER", "word": "RIGHT"},
    {"gesture": (1,0,1,1,1), "motion": "LEFT", "location": "CENTER", "word": "GOOD"},
    {"gesture": (1,0,1,1,1), "motion": "RIGHT", "location": "CENTER", "word": "BAD"},

    # Location gestures
    {"gesture": (0,1,1,1,1), "motion": "STILL", "location": "TOP", "word": "BYE"},
    {"gesture": (0,1,1,1,1), "motion": "STILL", "location": "BOTTOM", "word": "BAD"},
    {"gesture": (0,1,1,1,1), "motion": "STILL", "location": "LEFT", "word": "GO"},
    {"gesture": (1,1,1,1,1), "motion": "STILL", "location": "RIGHT", "word": "HEY"},
    {"gesture": (1,0,0,0,0), "motion": "STILL", "location": "TOP", "word": "YES_TOP"},
    {"gesture": (1,0,0,0,0), "motion": "STILL", "location": "BOTTOM", "word": "ME"},
    {"gesture": (1,0,0,0,0), "motion": "STILL", "location": "LEFT", "word": "HELP"},
    {"gesture": (1,0,0,0,0), "motion": "STILL", "location": "RIGHT", "word": "PLEASE"},

    # Extra combination gestures
    {"gesture": (1,1,0,0,1), "motion": "UP", "location": "CENTER", "word": "EXTRA_1"},
    {"gesture": (1,1,0,0,1), "motion": "DOWN", "location": "CENTER", "word": "EXTRA_2"},
    {"gesture": (1,0,1,0,1), "motion": "STILL", "location": "CENTER", "word": "EXTRA_3"},
    {"gesture": (0,1,1,0,1), "motion": "STILL", "location": "CENTER", "word": "FAMILY"},
    {"gesture": (1,1,1,0,1), "motion": "STILL", "location": "CENTER", "word": "NAME"},
]
