import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QRadioButton, QWidget


class MainWindow(QMainWindow):
    D_WIDTH = 1280
    D_HEIGHT = 720
    MODELS = ['yolov5s', 'yolov5m', 'yolov5l', 'yolov5x', 'custom']
    PATHS = ['github', 'local']

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("YOLO GUI")
        self.setFixedSize(self.D_WIDTH, self.D_HEIGHT)
        # label for holds image
        self.img_label = QLabel(self)
        # setting up border
        self.img_label.setStyleSheet("background-color: darkgray;")
        self.img_label.resize(self.D_WIDTH, self.D_HEIGHT)
        self._init_settings_ui()

    def _init_settings_ui(self):
        s_width = self.D_WIDTH // 4
        s_height = self.D_HEIGHT // 2
        s_start_pos = (self.D_WIDTH // 2 - s_width // 2, self.D_HEIGHT // 2 - s_height // 2)

        settings_layout = QGridLayout()
        settings_layout.setSpacing(5)

        path_label = QLabel()
        path_label.setText('Select yolo folder or remote path:')
        path_label.setFont(QFont('Arial', 16))
        settings_layout.addWidget(path_label, 0, 0)

        for index, path_name in enumerate(self.PATHS):
            layout_count = settings_layout.count()
            r_btn = QRadioButton(path_name)
            if index == 0:
                r_btn.setChecked(True)
            settings_layout.addWidget(r_btn, index + layout_count, 0)
            if path_name == 'local':
                path_btn = QPushButton('path')
                settings_layout.addWidget(path_btn, index + layout_count, 1)
            elif path_name == 'github':
                path_line = QLineEdit('ultralytics/yolov5')
                settings_layout.addWidget(path_line, index + layout_count, 1)

        model_label = QLabel()
        model_label.setText('Select model:')
        model_label.setFont(QFont('Arial', 16))

        layout_count = settings_layout.count()
        settings_layout.addWidget(model_label, layout_count, 0)

        for index, r_btn_name in enumerate(self.MODELS):
            layout_count = settings_layout.count()
            r_btn = QRadioButton(r_btn_name)
            if index == 0:
                r_btn.setChecked(True)
            settings_layout.addWidget(r_btn, index + layout_count, 0)
            if r_btn_name == 'custom':
                weight_btn = QPushButton('weights')
                settings_layout.addWidget(weight_btn, index + layout_count, 1)

        settings_layout.addWidget(QPushButton('Start'), settings_layout.count() + 3, 0, 1, settings_layout.columnCount()) # + 3 ?????
        widget = QWidget()
        widget.setStyleSheet("background-color: white;")
        widget.setFixedSize(s_width, s_height)
        widget.setLayout(settings_layout)
        widget.move(*s_start_pos)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
