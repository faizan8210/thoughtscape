import sys
import threading

from PySide6.QtWidgets import QApplication, QMainWindow

from ui.app_layout import build_app_layout
from workers.image_api_call import image_api_call
from service.set_wallpaper import set_wallpaper
from workers.speech_api_call import speech_api_call
from workers.agent_running import agent_running
from PySide6.QtGui import QIcon

def main():

    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("Thoughtscape")
    window.setWindowIcon(QIcon("assets/thoughtscape.png"))
    window.resize(1000, 650)

    layout, mic_button, status, transcript_box, generate_button = build_app_layout()

    def api_call():

        
        generate_button.setEnabled(False)

        status.setText("Understanding your thought...")

        
        def process():

            try:

              
                result = agent_running(transcript_box,status,generate_button)

                print("result:")
                print(result)

    
                if not result:
                    return

               
                final_prompt = result.get("image_prompt")

                if not final_prompt:
                    raise ValueError(
                        "No image prompt returned by agent."
                    )

                print("\nIMAGE PROMPT:")
                print(final_prompt)

             
                status.setText(
                    "Creating your ThoughtScape..."
                )

        
                image_path = image_api_call(final_prompt)

                print("\n Image created:")
                print(image_path)

               
                set_wallpaper(image_path)

                print("\nWallpaper updated successfully.")

                status.setText(
                    "Wallpaper updated successfully."
                )

            except Exception as e:

                print("\nERROR:")
                print(repr(e))

                status.setText(
                    f"Error: {str(e)}"
                )

            finally:
                generate_button.setEnabled(True)

        #  thread
        threading.Thread(
            target=process,
            daemon=True
        ).start()

    mic_button.clicked.connect(
        lambda: speech_api_call(
            mic_button,
            status,
            transcript_box
        )
    )


    generate_button.clicked.connect(api_call)

   
    window.setCentralWidget(layout)


    window.show()


    sys.exit(app.exec())


if __name__ == "__main__":
    main()
