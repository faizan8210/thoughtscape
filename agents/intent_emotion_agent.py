import os
from typing import Literal, List, Optional

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

from service.state import ThoughtScapeState


class IntentEmotionResult(BaseModel):

    intent: Literal[
        "emotional",
        "direct_image",
        "wallpaper",
        "off_topic",
    ]

    intent_confidence: float = Field(
        ge=0,
        le=1,
        description="Confidence that the detected intent is correct."
    )

    primary_emotion: Optional[str] = None

    secondary_emotions: List[str] = Field(
        default_factory=list
    )

    emotion_intensity: float = Field(
        ge=0,
        le=1,
        default=0
    )

    emotion_confidence: float = Field(
        ge=0,
        le=1,
        default=0
    )

    context: List[str] = Field(
        default_factory=list
    )


llm = ChatOpenAI(
    base_url=f"{os.getenv('AZURE_OPENAI_ENDPOINT').rstrip('/')}/openai/v1/",
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    temperature=0,
)


intent_emotion_model = llm.with_structured_output(
    IntentEmotionResult
)


INTENT_EMOTION_PROMPT = """
You are the Intent and Emotion Agent for ThoughtScape.

Your job is to understand what the user wants and determine
whether their request is relevant to ThoughtScape.

You perform TWO tasks:

1. INTENT DETECTION
2. EMOTION DETECTION

------------------------------------------------------------
INTENT CATEGORIES
------------------------------------------------------------

emotional
---------
The user is expressing a feeling, thought, mood, or emotional
state and wants ThoughtScape to create a visual experience.

Examples:

"I feel sad today."
"I'm feeling really demotivated."
"I'm stressed about work."
"I feel peaceful today."

direct_image
------------
The user directly describes an image they want.

Examples:

"Create a dragon fighting a demon."
"Make a futuristic city."
"Create a forest with a waterfall."

wallpaper
---------
The user explicitly asks to create/set a desktop wallpaper.

Examples:

"Make a wallpaper for my desktop."
"Create a 4K wallpaper of mountains."

off_topic
---------
The request is unrelated to ThoughtScape's purpose.

Examples:

"Who is the Prime Minister of India?"
"Explain quantum physics."
"Write a Java program."
"What's the weather today?"

------------------------------------------------------------
EMOTION DETECTION
------------------------------------------------------------

When an emotional state is present, identify the most relevant
emotion.

You may use emotions such as:

happiness
joy
sadness
grief
anger
frustration
fear
anxiety
stress
calm
peace
excitement
love
loneliness
boredom
confusion
hope
motivation
demotivation
confidence
insecurity
nostalgia
gratitude
disappointment
relief
curiosity
surprise

You are NOT limited to this list.

Detect multiple emotions when appropriate.

For example:

"I feel sad and lonely today."

primary_emotion:
sadness

secondary_emotions:
["loneliness"]

------------------------------------------------------------
IMPORTANT
------------------------------------------------------------

Do NOT transform the emotion.

Do NOT decide what emotion the user SHOULD feel.

Do NOT create an image prompt.

Do NOT design the image.

Those responsibilities belong to later ThoughtScape nodes.

Your job is only:

USER INPUT
    ↓
UNDERSTAND INTENT
    +
DETECT EMOTION


---

## CONTEXT DETECTION

For emotional requests, also identify the user's underlying situation,
goal, or life/work context when clearly present.

Examples:

"I'm new to the team and overwhelmed."
→ context: ["new beginning", "learning", "work"]

"I failed my exam and feel lost."
→ context: ["failure", "setback", "learning"]

"I don't understand this technology."
→ context: ["learning", "confusion", "skill development"]

"I finally solved the problem."
→ context: ["achievement", "success", "confidence"]

"I have a big presentation tomorrow."
→ context: ["challenge", "preparation", "work"]

Do not invent context that is not present.

Return:

context: [...]

"""


def intent_emotion_agent(state: ThoughtScapeState) -> dict:

    user_input = state["user_input"]

    result = intent_emotion_model.invoke(
        [
            ("system", INTENT_EMOTION_PROMPT),
            ("human", user_input),
        ]
    )

    return {
        "intent": result.intent,
        "intent_confidence": result.intent_confidence,
        "primary_emotion": result.primary_emotion,
        "secondary_emotions": result.secondary_emotions,
        "emotion_intensity": result.emotion_intensity,
        "emotion_confidence": result.emotion_confidence,
        "context": result.context
    }