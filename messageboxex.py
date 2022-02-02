#!/usr/bin/env python
# example from https://codeloop.org/python-tutorial-create-messagebox-with-pyside2/
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QVBoxLayout, QLabel
import sys
from PySide6.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 MessageBox")
        self.setGeometry(300,200,300,200)

        self.setIcon()

        self.create_button()

        self.show()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)


    def create_button(self):
        vbox = QVBoxLayout()

        btn1 = QPushButton("Open About MessageBox")
        btn1.clicked.connect(self.show_about)

        btn2 = QPushButton("Open Warning MessageBox")
        btn2.clicked.connect(self.show_warning)

        btn3 = QPushButton("Open Information MessageBox")
        btn3.clicked.connect(self.show_info)

        self.label = QLabel()

        btn4 = QPushButton("Open Question MessageBox")
        btn4.clicked.connect(self.show_question)


        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        vbox.addWidget(self.label)

        self.setLayout(vbox)


    def show_about(self):
        QMessageBox.about(self, "AboutBox", "This is about application")

    def show_warning(self):
        QMessageBox.warning(self, "Warning", "This is Warning")

    def show_info(self):
        QMessageBox.information(self, "Info", "This is Information")


    def show_question(self):
        reply = QMessageBox.question(self, "Question MessageBox", "Do You Like Pyside2",
                                     QMessageBox.Yes | QMessageBox.No)


        if reply == QMessageBox.Yes:
            self.label.setText("I Like Pyside2")

        elif reply == QMessageBox.No:
            self.label.setText("I Dont Like Pyside2")




myapp = QApplication(sys.argv)
window = Window()
# minor change from example
myapp.exec()
sys.exit()
