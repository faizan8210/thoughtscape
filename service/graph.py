from langgraph.graph import StateGraph, START, END

from service.state import ThoughtScapeState
from agents.security_agent import security_agent
from agents.intent_emotion_agent import intent_emotion_agent
from agents.mood_director import mood_director
from agents.visual_prompt_agent import visual_prompt_agent



def decline_node(state: ThoughtScapeState) -> dict:

    return {
        "response": "Sorry, I can't help with that.",
        "security_route": "decline",
    }


def security_router(state: ThoughtScapeState):

    if state.get("is_safe") is True:
        return "intent_emotion"

    return "decline"



def intent_router(state: ThoughtScapeState):

    intent = state.get("intent")

    if intent == "emotional":
        return "mood_director"

    if intent == "direct_image":
        return "visual_prompt"

    if intent == "wallpaper":
        return "visual_prompt"

    return "decline"



def build_graph():

    graph = StateGraph(ThoughtScapeState)


  
  
   

    # Node 1
    graph.add_node(
        "security_agent",
        security_agent
    )

    # Node 2
    graph.add_node(
        "intent_emotion",
        intent_emotion_agent
    )

    # Node 3
    graph.add_node(
        "mood_director",
        mood_director
    )

    # Node 4
    graph.add_node(
        "visual_prompt",
        visual_prompt_agent
    )

    # Decline node
    graph.add_node(
        "decline",
        decline_node
    )




    # start → Security
    graph.add_edge(
        START,
        "security_agent"
    )


   
    # Security → Intent or  Decline
   

    graph.add_conditional_edges(
        "security_agent",
        security_router,
        {
            "intent_emotion": "intent_emotion",
            "decline": "decline",
        },
    )


  
    # Intent → Mood Director or Visual Prompt or decline
  

    graph.add_conditional_edges(
        "intent_emotion",
        intent_router,
        {
            "mood_director": "mood_director",
            "visual_prompt": "visual_prompt",
            "decline": "decline",
        },
    )



    # Mood Director → Visual Prompt
 

    graph.add_edge(
        "mood_director",
        "visual_prompt"
    )



    # Visual Prompt → END
 

    graph.add_edge(
        "visual_prompt",
        END
    )


    # Decline → END
   

    graph.add_edge(
        "decline",
        END
    )


    return graph.compile()


thoughtscape_graph = build_graph()