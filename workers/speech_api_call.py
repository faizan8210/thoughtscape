
from service.speechtotext import start_speech, stop_speech

speech_state = {"listening": False}

def speech_api_call(mic_button ,status , transcript_box):


        if not speech_state["listening"]:

            start_speech()

            speech_state["listening"] = True

            mic_button.setText("Stop speaking")
            status.setText("Listening...")

        else:

            text = stop_speech()

            speech_state["listening"] = False

            mic_button.setText("Start speaking")
            status.setText("Stopped")

            transcript_box.setPlainText(text)