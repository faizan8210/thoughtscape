# from ui.sidebar import build_sidebar 
# from PySide6.QtWidgets import (
#     QHBoxLayout,
#     QWidget,
# )
# from ui.main_page import build_main_page

# def build_app_layout():
#     root = QWidget()

#     layout = QHBoxLayout(root)
#     layout.setContentsMargins(0, 0, 0, 0)

#     sidebar = build_sidebar()
#     main_page, mic_button, status, transcript_box , generate_button = build_main_page()

#     layout.addWidget(sidebar)
#     layout.addWidget(main_page, 1)

#     return root, mic_button, status, transcript_box , generate_button



from PySide6.QtWidgets import QHBoxLayout, QWidget

from ui.sidebar import build_sidebar
from ui.main_page import build_main_page


def build_app_layout():

    root = QWidget()

    layout = QHBoxLayout(root)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(0)

    sidebar = build_sidebar()

    (
        main_page,
        mic_button,
        status,
        transcript_box,
        generate_button,
    ) = build_main_page()

    layout.addWidget(sidebar)
    layout.addWidget(main_page, 1)

    return (
        root,
        mic_button,
        status,
        transcript_box,
        generate_button,
    )