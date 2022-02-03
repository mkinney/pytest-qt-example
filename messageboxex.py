#!/usr/bin/env python
""" example from https://codeloop.org/python-tutorial-create-messagebox-with-pyside2/
    demonstrating various dialog boxes
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QVBoxLayout, QLabel
from PySide6.QtGui import QIcon

class Window(QWidget):
    """custom Window class derived from QWidget"""

    def __init__(self):
        """constructor"""
        super().__init__()

        self.setWindowTitle("Pyside6 MessageBox")
        self.setGeometry(300,200,300,200)

        self.set_icon()

        vbox = QVBoxLayout()

        self.btn1 = QPushButton("Open About MessageBox")
        self.btn1.clicked.connect(self.show_about)

        self.btn2 = QPushButton("Open Warning MessageBox")
        self.btn2.clicked.connect(self.show_warning)

        self.btn3 = QPushButton("Open Information MessageBox")
        self.btn3.clicked.connect(self.show_info)

        self.label = QLabel()

        self.btn4 = QPushButton("Open Question MessageBox")
        self.btn4.clicked.connect(self.show_question)

        self.quit_button = QPushButton("Quit")
        self.quit_button.clicked.connect(self.quit_action)

        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.btn3)
        vbox.addWidget(self.btn4)
        vbox.addWidget(self.label)
        vbox.addWidget(self.quit_button)

        self.warning = None

        self.setLayout(vbox)

        self.show()

    def quit_action(self):
        """Quit the application from a button"""
        QApplication.quit()

    def set_icon(self):
        """Se the icon"""
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def show_about(self):
        """Show about dialog"""
        QMessageBox.about(self, "AboutBox", "This is about application")
        # can test based off of some attribute like the text of the label
        self.label.setText("About clicked")

    def show_warning(self):
        """Show warning dialog"""
        QMessageBox.warning(self, "Warning", "This is Warning")
        # can test based off of some attribute or a member
        self.warning = True

    def show_info(self):
        """Show info dialog"""
        QMessageBox.information(self, "Info", "This is Information")
        self.label.setText("Info was clicked")

    def show_question(self):
        """Show y/n dialog"""
        reply = QMessageBox.question(self, "Question MessageBox", "Do You Like Pyside6",
                                     QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.label.setText("I Like Pyside6")

        elif reply == QMessageBox.No:
            self.label.setText("I Dont Like Pyside6")


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    # pylint: disable=unused-variable
    window = Window()
    myapp.exec()
    sys.exit()
