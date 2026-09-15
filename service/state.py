from typing import TypedDict , Optional ,List


class ThoughtScapeState(TypedDict, total=False):
    user_input: str

    # Security Agent
    is_safe: bool
    security_category: str
    security_reason: str
    security_route: str

    # Intent + Emotion Agent
    intent: str
    intent_confidence: float
    primary_emotion: Optional[str]
    secondary_emotions: List[str]
    emotion_intensity: float
    emotion_confidence: float
    context: List[str]

    # Mood Director
    mood_action: str
    target_emotion: str
    supporting_emotions: List[str]
    visual_mood: str
    transformation_reason: str
    use_quote: bool
    quote_theme: str
    growth_requested: bool
    growth_goal: str
    action_steps: List[str]
    
   #Visual Prompt Agent
   
    image_prompt: str