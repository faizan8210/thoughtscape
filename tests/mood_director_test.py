from agents.mood_director import mood_director


def test_mood_director(test_case):
    print("\n" + "=" * 60)
    print("INPUT")
    print("=" * 60)

    print("Emotion:", test_case["primary_emotion"])
    print("Secondary:", test_case["secondary_emotions"])
    print("Intensity:", test_case["emotion_intensity"])
    print("Confidence:", test_case["emotion_confidence"])

    state = {
        "primary_emotion": test_case["primary_emotion"],
        "secondary_emotions": test_case["secondary_emotions"],
        "emotion_intensity": test_case["emotion_intensity"],
        "emotion_confidence": test_case["emotion_confidence"],
    }

    result = mood_director(state)

    print("\n" + "-" * 60)
    print("MOOD DIRECTOR RESULT")
    print("-" * 60)

    print("Action:", result["mood_action"])
    print("Target emotion:", result["target_emotion"])
    print("Supporting emotions:", result["supporting_emotions"])
    print("Visual mood:", result["visual_mood"])
    print("Reason:", result["transformation_reason"])

    print("=" * 60)


test_cases = [
    {
        "primary_emotion": "sadness",
        "secondary_emotions": ["loneliness"],
        "emotion_intensity": 0.8,
        "emotion_confidence": 0.95,
    },

    {
        "primary_emotion": "demotivation",
        "secondary_emotions": ["tiredness", "frustration"],
        "emotion_intensity": 0.85,
        "emotion_confidence": 0.94,
    },

    {
        "primary_emotion": "stress",
        "secondary_emotions": ["overwhelm"],
        "emotion_intensity": 0.7,
        "emotion_confidence": 0.91,
    },

    {
        "primary_emotion": "anxiety",
        "secondary_emotions": ["worry"],
        "emotion_intensity": 0.75,
        "emotion_confidence": 0.93,
    },

    {
        "primary_emotion": "anger",
        "secondary_emotions": ["frustration"],
        "emotion_intensity": 0.8,
        "emotion_confidence": 0.92,
    },

    {
        "primary_emotion": "happiness",
        "secondary_emotions": ["joy"],
        "emotion_intensity": 0.9,
        "emotion_confidence": 0.98,
    },

    {
        "primary_emotion": "excitement",
        "secondary_emotions": ["enthusiasm"],
        "emotion_intensity": 0.85,
        "emotion_confidence": 0.96,
    },

    {
        "primary_emotion": "calm",
        "secondary_emotions": ["peace"],
        "emotion_intensity": 0.7,
        "emotion_confidence": 0.95,
    },
]


for test_case in test_cases:
    test_mood_director(test_case)