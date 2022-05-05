from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from confirmar_programacion_ui import Ui_Dialog


class ConfirmarProgramacion(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def set_name_dni(self, name, dni):
        body = self.body.text()
        body = body.replace("<NOMBRE>", name)
        body = body.replace("<DNI>", dni)
        self.body.setText(body)