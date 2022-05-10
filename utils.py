from PyQt5.QtWidgets import QDesktopWidget


def center(widget):
    qtRectangle = widget.frameGeometry()
    centerPoint = QDesktopWidget().availableGeometry().center()
    qtRectangle.moveCenter(centerPoint)
    widget.move(qtRectangle.topLeft())


def center_relative(old_widget, new_widget):
    qtRectangle = new_widget.frameGeometry()
    centerPoint = old_widget.frameGeometry().center()
    qtRectangle.moveCenter(centerPoint)
    new_widget.move(qtRectangle.topLeft())
