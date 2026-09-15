# from PySide6.QtCore import Qt
# from PySide6.QtWidgets import (
#     QHBoxLayout,
#     QLabel,
#     QPushButton,
#     QTextEdit,
#     QVBoxLayout,
#     QWidget,
# )


# def build_main_page():
#     page = QWidget()

#     layout = QVBoxLayout(page)
#     layout.setContentsMargins(50, 40, 50, 40)
#     layout.setSpacing(20)
#     buttons_layout = QHBoxLayout()

#     eyebrow = QLabel("CREATE A THOUGHTSCAPE")

#     heading = QLabel("What is moving through you?")
#     heading.setStyleSheet("font-size: 30px; font-weight: bold;")

#     mic_button = QPushButton("Start speaking")
#     mic_button.setMinimumHeight(60)

#     generate_button = QPushButton("Generate and set wallpaper")
#     generate_button.setMinimumHeight(60)

#     buttons_layout.addWidget(mic_button)
#     buttons_layout.addWidget(generate_button)

  
#     status = QLabel("Tap the microphone to begin")
#     status.setAlignment(Qt.AlignmentFlag.AlignCenter)

#     transcript_label = QLabel("LIVE TRANSCRIPT")

#     transcript_box = QTextEdit()
#     transcript_box.setPlaceholderText(
#         "Your speech will appear here while you are talking..."
#     )
#     transcript_box.setReadOnly(True)
#     transcript_box.setMinimumHeight(220)

#     layout.addWidget(eyebrow)
#     layout.addWidget(heading)
#     layout.addSpacing(20)
#     layout.addLayout(buttons_layout)  
#     layout.addWidget(mic_button)
#     layout.addWidget(status)
#     layout.addSpacing(10)
#     layout.addWidget(transcript_label)
#     layout.addWidget(transcript_box)

#     return page, mic_button, status, transcript_box , generate_button


from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


def build_main_page():

    page = QWidget()

    page.setStyleSheet("""
        QWidget {
            background-color: #0d0f16;
            color: #f4f1ff;
            font-family: "Segoe UI";
        }

      

        QLabel#eyebrow {
            background: transparent;
            color: #aaa1c8;
            font-size: 13px;
            font-weight: 700;
        }

        QLabel#heading {
            background: transparent;
            color: #f5f2ff;
            font-size: 32px;
            font-weight: 700;
        }

        QLabel#input_label {
            background: transparent;
            color: #c5bed8;
            font-size: 14px;
            font-weight: 600;
        }

        QLabel#helper {
            background: transparent;
            color: #8f899f;
            font-size: 13px;
        }

        QLabel#status {
            background: transparent;
            color: #a98cff;
            font-size: 13px;
        }

        QLabel#landscape_title {
            background: transparent;
            color: #eeeaff;
            font-size: 13px;
            font-weight: 700;
        }


        QFrame#input_card {
            background-color: #171a25;
            border: 1px solid #292d3c;
            border-radius: 18px;
        }

        QTextEdit {
            background-color: #0e1018;
            color: #eeeaff;
            border: 1px solid #8d65ff;
            border-radius: 12px;
            padding: 14px;
            font-size: 16px;
        }

        QTextEdit:focus {
            border: 1px solid #a27aff;
        }

        QPushButton#mic_button {
            background-color: #2b2846;
            color: #e8e1ff;
            border: 1px solid #403966;
            border-radius: 10px;
            padding: 10px 18px;
            font-size: 14px;
            font-weight: 600;
        }

        QPushButton#mic_button:hover {
            background-color: #353052;
        }

        QPushButton#generate_button {
            background-color: #9b72ff;
            color: #120d20;
            border: none;
            border-radius: 11px;
            padding: 10px 22px;
            font-size: 14px;
            font-weight: 700;
        }

        QPushButton#generate_button:hover {
            background-color: #ad8aff;
        }

        QPushButton#generate_button:disabled {
            background-color: #51486d;
            color: #aaa4b7;
        }

        QFrame#landscape_card {
            background-color: #1b2440;
            border: none;
            border-radius: 18px;
        }

        QLabel#landscape_title {
            color: #eeeaff;
            font-size: 13px;
            font-weight: 700;
        }
    """)

    layout = QVBoxLayout(page)

    layout.setContentsMargins(
        48,
        36,
        48,
        30,
    )

    layout.setSpacing(0)

    # ---------------------------------
    # Header
    # ---------------------------------

    eyebrow = QLabel("CREATE A THOUGHTSCAPE")
    eyebrow.setObjectName("eyebrow")

    heading = QLabel("What is moving through you?")
    heading.setObjectName("heading")

    layout.addWidget(eyebrow)

    layout.addSpacing(10)

    layout.addWidget(heading)

    layout.addSpacing(24)

    # ---------------------------------
    # Input Card
    # ---------------------------------

    input_card = QFrame()
    input_card.setObjectName("input_card")

    card_layout = QVBoxLayout(input_card)

    card_layout.setContentsMargins(
        24,
        20,
        24,
        20,
    )

    card_layout.setSpacing(10)

    input_label = QLabel(
        "A thought, feeling, or moment"
    )

    input_label.setObjectName("input_label")

    transcript_box = QTextEdit()

    transcript_box.setPlaceholderText(
        "Share what's on your mind..."
    )

    # IMPORTANT:
    # Keep this because your speech code uses it.
    transcript_box.setReadOnly(True)

    # Fixed height prevents the text box
    # from pushing the other controls away.
    transcript_box.setFixedHeight(150)

    # helper = QLabel(
    #     "A few honest words are enough."
    # )

    # helper.setObjectName("helper")

    # ---------------------------------
    # Buttons
    # ---------------------------------

    buttons_layout = QHBoxLayout()

    buttons_layout.setSpacing(12)

    mic_button = QPushButton(
        "Start speaking"
    )

    mic_button.setObjectName(
        "mic_button"
    )

    mic_button.setFixedHeight(46)

    generate_button = QPushButton(
        "Shape my space  →"
    )

    generate_button.setObjectName(
        "generate_button"
    )

    generate_button.setFixedHeight(46)

    buttons_layout.addWidget(mic_button)

    buttons_layout.addStretch()

    buttons_layout.addWidget(
        generate_button
    )

    # ---------------------------------
    # Add card contents
    # ---------------------------------

    card_layout.addWidget(input_label)

    card_layout.addWidget(transcript_box)

    # card_layout.addWidget(helper)

    card_layout.addSpacing(6)

    card_layout.addLayout(
        buttons_layout
    )

    layout.addWidget(input_card)

    # ---------------------------------
    # Status
    # ---------------------------------

    status = QLabel(
        "Tap the microphone to begin"
    )

    status.setObjectName("status")

    status.setAlignment(
        Qt.AlignmentFlag.AlignCenter
    )

    layout.addSpacing(12)

    layout.addWidget(status)

    # ---------------------------------
    # Current Landscape
    # ---------------------------------

    layout.addSpacing(20)

    landscape_card = QFrame()

    landscape_card.setObjectName(
        "landscape_card"
    )

    landscape_layout = QVBoxLayout(
        landscape_card
    )

    landscape_layout.setContentsMargins(
        24,
        20,
        24,
        20,
    )

    landscape_title = QLabel(
        "YOUR CURRENT LANDSCAPE"
    )

    landscape_title.setObjectName(
        "landscape_title"
    )

    landscape_layout.addWidget(
        landscape_title
    )

    landscape_layout.addStretch()

    # Smaller because it is currently empty.
    landscape_card.setFixedHeight(150)

    layout.addWidget(
        landscape_card
    )

    return (
        page,
        mic_button,
        status,
        transcript_box,
        generate_button,
    )