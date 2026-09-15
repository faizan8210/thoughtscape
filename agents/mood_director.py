import os
from typing import Literal, List

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

from service.state import ThoughtScapeState

from dotenv import load_dotenv

load_dotenv()



class MoodDirectorResult(BaseModel):

    mood_action: Literal[
        "transform",
        "preserve",
    ]

    target_emotion: str

    supporting_emotions: List[str] = Field(
        default_factory=list
    )

    visual_direction: str

    use_quote: bool = False

    quote_theme: str = ""
    growth_requested: bool = False
    growth_goal: str = ""
    action_steps: List[str] = Field(default_factory=list)



llm = ChatOpenAI(
    base_url=f"{os.getenv('AZURE_OPENAI_ENDPOINT').rstrip('/')}/openai/v1/",
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    temperature=0,
)


mood_director_model = llm.with_structured_output(
    MoodDirectorResult
)


MOOD_DIRECTOR_PROMPT = """
You are the Mood Director for ThoughtScape.

Your responsibility is to decide how ThoughtScape should
emotionally respond to the user's emotion and situation.

You DO NOT generate an image.

You DO NOT write an image-generation prompt.

You ONLY decide the emotional and visual direction.

---

## CORE PRINCIPLE

ThoughtScape should not simply reproduce negative emotions.

For difficult emotions, transform the experience toward
a constructive emotional state.

The transformation must consider both:

1. The user's emotion
2. The user's context

Do not blindly transform every negative emotion into happiness.

The result should feel natural and meaningful.

---

## EMOTION + CONTEXT EXAMPLES

overwhelm + new beginning
→ calm confidence

overwhelm + learning
→ calm confidence + progress

stress + work challenge
→ clarity + control

failure + learning
→ resilience

feeling lost + career
→ hope + direction

demotivation + difficult task
→ motivation + determination

anxiety + new responsibility
→ confidence + stability

fear + challenge
→ courage

loneliness
→ connection + belonging

---

## POSITIVE EMOTIONS

Positive emotions should generally be preserved
or amplified.

happiness → happiness
joy → joy
excitement → excitement
pride → achievement
confidence → confidence
gratitude → gratitude
calm → calm
hope → hope

---

## VISUAL DIRECTION

For difficult emotions, create a visual story of
transformation rather than literally visualizing
the negative emotion.

Prefer concepts such as:

- journeys
- paths
- mountains
- sunrise
- open horizons
- progress
- exploration
- growth
- achievement
- light
- futuristic environments
- meaningful environments related to the context

Avoid automatically using:

- stones
- sand
- meditation
- therapy
- empty minimalist scenes
- generic abstract shapes

unless specifically appropriate.

---

## MOTIVATIONAL QUOTE

Sometimes the visual experience should include
a motivational quote.

Set:

use_quote: true

when the user expresses things such as:

- failure
- feeling lost
- strong demotivation
- major uncertainty
- difficult learning
- overcoming a challenge
- starting a difficult journey

Otherwise:

use_quote: false

When use_quote is true, provide:

quote_theme

The quote_theme describes the message of the quote.

Do NOT write the actual quote here.

Example:

quote_theme:
"Failure is temporary and does not define the future."

---

## OUTPUT

Return:

mood_action
target_emotion
supporting_emotions
visual_direction
use_quote
quote_theme

## PERSONAL GROWTH PLAN

Determine whether the user wants to improve, learn, develop,
or become better at something.

Set growth_requested=true ONLY when the user expresses a
clear desire for personal or professional improvement.

Examples:

"I need to improve my communication."
"I want to become better at speaking in meetings."
"I want to learn this technology."
"I need to become more confident."
"I want to improve my leadership skills."

For normal emotional statements, set growth_requested=false.

Examples:

"I'm feeling sad today."
"I'm really stressed."
"I had a difficult day."
"I'm excited about my new job."

When growth_requested=true:

1. Identify the main improvement goal.

2. Create exactly 3 or 4 simple action steps.

3. Make the actions practical and achievable for an employee.

4. Keep each action short.

Example:

User:
"I need to improve my communication.
I'm not confident speaking in meetings."

Return:

growth_requested:
true

growth_goal:
"Improve communication confidence"

action_steps:
[
    "Practice speaking for 10 minutes daily",
    "Share one idea in every meeting",
    "Ask one question confidently",
    "Reflect on progress weekly"
]

Another example:

User:
"I want to become better at presentations."

Return:

growth_requested:
true

growth_goal:
"Improve presentation skills"

action_steps:
[
    "Practice one presentation each week",
    "Record yourself speaking",
    "Focus on clear explanations",
    "Ask for feedback"
]

If growth_requested=false:

growth_goal:
""

action_steps:
[]

Do not create a growth plan just because the user has a
negative emotion.

A growth plan requires an explicit desire to improve.


"""



def mood_director(state: ThoughtScapeState) -> dict:

    result = mood_director_model.invoke(
        [
            ("system", MOOD_DIRECTOR_PROMPT),
            (
                "human",
                f"""
Primary emotion:
{state.get("primary_emotion")}

Secondary emotions:
{state.get("secondary_emotions", [])}

Context:
{state.get("context", [])}

Emotion intensity:
{state.get("emotion_intensity", 0)}

Emotion confidence:
{state.get("emotion_confidence", 0)}
"""
            ),
        ]
    )

    return {
        
        "mood_action": result.mood_action,
        "target_emotion": result.target_emotion,
        "supporting_emotions": result.supporting_emotions,
        "visual_direction": result.visual_direction,
        "use_quote": result.use_quote,
        "quote_theme": result.quote_theme,
        "growth_requested": result.growth_requested,
        "growth_goal": result.growth_goal,
        "action_steps": result.action_steps,

    }