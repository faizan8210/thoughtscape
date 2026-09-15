import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv


load_dotenv()


recognizer = None
final_text = []


def start_speech():
    global recognizer
    global final_text

    speech_key = os.getenv("AZURE_SPEECH_KEY")
    speech_region = os.getenv("AZURE_SPEECH_REGION")

    if not speech_key:
        raise ValueError("AZURE_SPEECH_KEY is not set.")

    if not speech_region:
        raise ValueError("AZURE_SPEECH_REGION is not set.")

    speech_config = speechsdk.SpeechConfig(
        subscription=speech_key,
        region=speech_region
    )

    speech_config.speech_recognition_language = "en-US"

    audio_config = speechsdk.audio.AudioConfig(
        use_default_microphone=True
    )

    recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        audio_config=audio_config
    )

    final_text = []

    def recognizing_handler(event):
        print("Partial:", event.result.text)

    def recognized_handler(event):
        if event.result.reason == speechsdk.ResultReason.RecognizedSpeech:
            text = event.result.text

            if text:
                final_text.append(text)
                print("Final:", text)

    def canceled_handler(event):
        print("Recognition canceled.")

        if event.cancellation_details:
            print(
                "Reason:",
                event.cancellation_details.reason
            )

            if event.cancellation_details.error_details:
                print(
                    "Error:",
                    event.cancellation_details.error_details
                )

    recognizer.recognizing.connect(recognizing_handler)
    recognizer.recognized.connect(recognized_handler)
    recognizer.canceled.connect(canceled_handler)

    print("Listening...")

    recognizer.start_continuous_recognition()


def stop_speech():
    global recognizer
    global final_text

    if recognizer is None:
        return ""

    recognizer.stop_continuous_recognition()

    text = " ".join(final_text)

    print("Stopped.")
    print("Final text:", text)

    recognizer = None

    return text