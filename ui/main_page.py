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
from ui.style_loader import load_style

def build_main_page():

    page = QWidget()

    page.setStyleSheet(load_style("main.qss"))

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

   
    transcript_box.setReadOnly(True)

   
    transcript_box.setFixedHeight(150)

  



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