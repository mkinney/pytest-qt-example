#!/usr/bin/env python
# coding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QFormLayout

class HelloWidget(QWidget):
    def __init__(self):
        # Window
        super(HelloWidget, self).__init__()
        self.resize(200, 150)
        self.setWindowTitle("PySide6 Demo")

        # QLabel
        self.greet_label = QLabel(self)
        self.greet_label.setText("Hello World!")

        # QPushButton
        self.button_greet = QPushButton("Go")
        self.button_greet.clicked.connect(self.greet)

        # create layout
        form_layout = QFormLayout()
        form_layout.addRow(self.tr("Label"), self.greet_label)
        form_layout.addRow(self.tr("Say hi"), self.button_greet)
        self.setLayout(form_layout)

    def greet(self):
        """Say hello"""
        self.greet_label.setText("Hello!")


if __name__ == "__main__":
    app = QApplication([])
    window = HelloWidget()
    window.show()
    sys.exit(app.exec())
