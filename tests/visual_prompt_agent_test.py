from agents.visual_prompt_agent import visual_prompt_agent


def test_visual_prompt(user_input, intent, primary_emotion,
                       mood_action, target_emotion, visual_mood):

    state = {
        "user_input": user_input,

        "intent": intent,

        "primary_emotion": primary_emotion,
        "secondary_emotions": [],
        "emotion_intensity": 0.8,
        "emotion_confidence": 0.95,

        "mood_action": mood_action,
        "target_emotion": target_emotion,
        "supporting_emotions": [],
        "visual_mood": visual_mood,
    }

    result = visual_prompt_agent(state)

    print("=" * 70)
    print("INPUT:")
    print(user_input)

    print("\nIMAGE PROMPT:")
    print(result["image_prompt"])

    print("=" * 70)


# ============================================================
# Test 1 - Emotional transformation
# ============================================================

test_visual_prompt(
    user_input="I feel really demotivated today.",
    intent="emotional",
    primary_emotion="demotivation",
    mood_action="transform",
    target_emotion="motivation",
    visual_mood="uplifting",
)


# ============================================================
# Test 2 - Happy emotion
# ============================================================

test_visual_prompt(
    user_input="I am feeling very happy today.",
    intent="emotional",
    primary_emotion="happiness",
    mood_action="preserve",
    target_emotion="happiness",
    visual_mood="joyful",
)


# ============================================================
# Test 3 - Calm emotion
# ============================================================

test_visual_prompt(
    user_input="I want something peaceful and relaxing.",
    intent="emotional",
    primary_emotion="stress",
    mood_action="transform",
    target_emotion="calm",
    visual_mood="peaceful",
)


# ============================================================
# Test 4 - Direct image request
# ============================================================

test_visual_prompt(
    user_input="Create a dragon fighting a demon in a dark fantasy world.",
    intent="direct_image",
    primary_emotion="",
    mood_action="preserve",
    target_emotion="",
    visual_mood="epic",
)