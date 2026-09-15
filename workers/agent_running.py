from service.graph import thoughtscape_graph


def security_check(status, result):

    if not result.get("is_safe", False):
        status.setText(
            "Sorry, I can't help with this request."
        )
        return False

    return True


def prompt(status, user_input):

    result = thoughtscape_graph.invoke(
        {
            "user_input": user_input
        }
    )

    print(
        "annnnnn------------------------->>",
        result
    )

   
    if not security_check(status, result):
        return None


    image_prompt = result.get("image_prompt")

    if not image_prompt:
        status.setText(
            "Could not create an image prompt."
        )
        return None

  
    return result


def agent_running(
    transcript_box,
    status,
    generate_button
):

    user_input = transcript_box.toPlainText().strip()

    if not user_input:

        status.setText(
            "Please speak something first."
        )

        return None

    status.setText(
        "ThoughtScape is thinking..."
    )

    generate_button.setEnabled(False)

    try:

        result = prompt(
            status,
            user_input
        )

        return result

    except Exception as e:

        print("AGENT ERROR:")
        print(repr(e))

        status.setText(
            "Something went wrong. Check the terminal."
        )

        return None