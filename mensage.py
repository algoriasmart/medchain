from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from mensage_ui import Ui_widget


class Mensage(QWidget, Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.button.clicked.connect(lambda: self.close())

    def set_text(self, text):
        self.body.setText(text)
