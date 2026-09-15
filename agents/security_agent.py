import os

from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from typing import Literal

from service.state import ThoughtScapeState


class SecurityResult(BaseModel):
    is_safe: bool

    category: Literal[
        "safe",
        "self_harm",
        "harm_to_others",
        "sexual_or_nudity",
        "other_unsafe",
    ]

    reason: str



llm = ChatOpenAI(
    base_url=f"{os.getenv('AZURE_OPENAI_ENDPOINT').rstrip('/')}/openai/v1/",
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    temperature=0,
)



security_model = llm.with_structured_output(SecurityResult)


SECURITY_PROMPT = """
You are the Security Agent for ThoughtScape.

Your ONLY responsibility is to determine whether the user's
input is safe to continue through the ThoughtScape pipeline.

Classify the input into exactly one category:

safe
self_harm
harm_to_others
sexual_or_nudity
other_unsafe

SAFE:
Normal conversation, emotions, thoughts, and creative image
requests that are not unsafe.

Examples:
"I feel sad today."
"I feel demotivated."
"Create a mountain wallpaper."
"Create a dragon fighting a demon."

SELF_HARM:
Requests or expressions involving suicide or self-harm.

HARM_TO_OTHERS:
Requests involving seriously harming or killing another person.

SEXUAL_OR_NUDITY:
Requests for sexual, sexually explicit, pornographic,
or nude content.

OTHER_UNSAFE:
Other content that should not proceed through ThoughtScape.

IMPORTANT:
- Do not analyze emotions.
- Do not create image prompts.
- Do not generate images.
- Do not transform emotions.
- You are only the security gate.


"""


def security_agent(state: ThoughtScapeState) -> dict:

    user_input = state["user_input"]

    try:
        result = security_model.invoke(
            [
                ("system", SECURITY_PROMPT),
                ("human", user_input),
            ]
        )

        return {
            "is_safe": result.is_safe,
            "security_category": result.category,
            "security_reason": result.reason,
            "security_route": (
                "continue"
                if result.is_safe
                else "decline"
            ),
        }

    except Exception as e:

        error_message = str(e)
     

        if "content_filter" in error_message:
            return {
                "is_safe": False,
                "security_category": "other_unsafe",
                "security_reason": (
                    "The request was blocked by the Azure "
                    "content safety filter."
                ),
                "security_route": "decline",
            }

        raise
   