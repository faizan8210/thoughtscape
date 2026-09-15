from dotenv import load_dotenv

load_dotenv()

from service.graph import thoughtscape_graph


def test_graph(user_input):

    print("\n" + "=" * 80)
    print("THOUGHTSCAPE GRAPH TEST")
    print("=" * 80)

    print("\nUSER INPUT:")
    print(user_input)

    print("\nRunning LangGraph...")
    print("-" * 80)

    try:

        result = thoughtscape_graph.invoke(
            {
                "user_input": user_input
            }
        )

        print("\n" + "=" * 80)
        print("GRAPH FINISHED")
        print("=" * 80)

        print("\nFINAL STATE:")
        print(result)

        print("\n" + "-" * 80)

        print("SECURITY:")
        print("is_safe:", result.get("is_safe"))
        print("category:", result.get("security_category"))

        print("\nINTENT:")
        print(result.get("intent"))

        print("\nPRIMARY EMOTION:")
        print(result.get("primary_emotion"))

        print("\nEMOTION INTENSITY:")
        print(result.get("emotion_intensity"))

        print("\nMOOD ACTION:")
        print(result.get("mood_action"))

        print("\nTARGET EMOTION:")
        print(result.get("target_emotion"))

        print("\nVISUAL MOOD:")
        print(result.get("visual_mood"))

        print("\nIMAGE PROMPT:")
        print(result.get("image_prompt"))

        print("\nRESPONSE:")
        print(result.get("response"))

        print("\n" + "=" * 80)

    except Exception as e:

        print("\n" + "=" * 80)
        print("GRAPH ERROR")
        print("=" * 80)

        print(type(e).__name__)
        print(e)


test_graph(
   "Who is the Prime Minister of India?"
)