# from PySide6.QtWidgets import (
#     QFrame,
#     QLabel,
#     QPushButton,
#     QVBoxLayout,
   
# )

# def build_sidebar():
#     sidebar = QFrame()
#     sidebar.setFixedWidth(220)

#     layout = QVBoxLayout(sidebar)
#     layout.setContentsMargins(20, 30, 20, 20)
#     layout.setSpacing(15)

#     title = QLabel("Thoughtscape")
#     title.setStyleSheet("font-size: 24px; font-weight: bold;")

#     subtitle = QLabel("INNER SPACE, VISUALIZED")
#     settings_button = QPushButton("Settings")

#     layout.addWidget(title)
#     layout.addWidget(subtitle)
#     layout.addSpacing(30)
#     layout.addStretch()
#     layout.addWidget(settings_button)

#     return sidebar




from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
)


def build_sidebar():

    sidebar = QFrame()
    sidebar.setFixedWidth(250)

    sidebar.setStyleSheet("""
        QFrame {
            background-color: #151824;
            border-right: 1px solid #292d3d;
        }

        QLabel#title {
            color: #f4f1ff;
            font-size: 26px;
            font-weight: 700;
        }

        QLabel#subtitle {
            color: #a99fc5;
            font-size: 12px;
            font-weight: 600;
            letter-spacing: 1px;
        }

        QPushButton {
            background-color: transparent;
            color: #c9c4dc;
            border: none;
            border-radius: 10px;
            padding: 12px 14px;
            text-align: left;
            font-size: 15px;
        }

        QPushButton:hover {
            background-color: #25233d;
            color: #ffffff;
        }

        QPushButton#active {
            background-color: #302c50;
            color: #ffffff;
        }
    """)

    layout = QVBoxLayout(sidebar)
    layout.setContentsMargins(20, 30, 20, 20)
    layout.setSpacing(8)

    title = QLabel("Thoughtscape")
    title.setObjectName("title")

    subtitle = QLabel("INNER SPACE, VISUALIZED")
    subtitle.setObjectName("subtitle")

    create_button = QPushButton("✦  Create")
    create_button.setObjectName("active")

    # recent_button = QPushButton("◷  Recent spaces")

    # settings_button = QPushButton("⚙  Settings")

    layout.addWidget(title)
    layout.addWidget(subtitle)

    layout.addSpacing(38)

    layout.addWidget(create_button)
    # layout.addWidget(recent_button)

    layout.addStretch()

    # layout.addWidget(settings_button)

    return sidebar