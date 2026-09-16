from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
)
from ui.style_loader import load_style

def build_sidebar():

    sidebar = QFrame()
    sidebar.setFixedWidth(250)

    sidebar.setStyleSheet(load_style("sidebar.qss"))

    layout = QVBoxLayout(sidebar)
    layout.setContentsMargins(20, 30, 20, 20)
    layout.setSpacing(8)

    title = QLabel("Thoughtscape")
    title.setObjectName("title")

    subtitle = QLabel("INNER SPACE, VISUALIZED")
    subtitle.setObjectName("subtitle")

    create_button = QPushButton("✦  Create")
    create_button.setObjectName("active")

    layout.addWidget(title)
    layout.addWidget(subtitle)

    layout.addSpacing(38)
    layout.addWidget(create_button)
    layout.addStretch()
    return sidebar