from pytestqt.qt_compat import qt_api

from PySide6.QtWidgets import QMessageBox

from messageboxex import Window

def test_about_clicked(qtbot, monkeypatch):
    widget = Window()
    qtbot.addWidget(widget)

    monkeypatch.setattr(QMessageBox, "about", lambda *args: None)
    qtbot.mouseClick(widget.btn1, qt_api.QtCore.Qt.MouseButton.LeftButton)
    assert widget.label.text() == "About clicked"

def test_warning_clicked(qtbot, monkeypatch):
    widget = Window()
    qtbot.addWidget(widget)

    assert widget.warning is None
    monkeypatch.setattr(QMessageBox, "warning", lambda *args: None)
    qtbot.mouseClick(widget.btn2, qt_api.QtCore.Qt.MouseButton.LeftButton)
    assert widget.warning

def test_info_clicked(qtbot, monkeypatch):
    widget = Window()
    qtbot.addWidget(widget)

    monkeypatch.setattr(QMessageBox, "information", lambda *args: None)
    qtbot.mouseClick(widget.btn3, qt_api.QtCore.Qt.MouseButton.LeftButton)
    assert widget.label.text() == "Info was clicked"

def test_like_clicked_yes(qtbot, monkeypatch):
    widget = Window()
    qtbot.addWidget(widget)

    assert widget.label.text() == ""
    monkeypatch.setattr(QMessageBox, "question", lambda *args: QMessageBox.Yes)
    qtbot.mouseClick(widget.btn4, qt_api.QtCore.Qt.MouseButton.LeftButton)
    assert widget.label.text() == "I Like Pyside6"

def test_like_clicked_no(qtbot, monkeypatch):
    widget = Window()
    qtbot.addWidget(widget)

    assert widget.label.text() == ""
    monkeypatch.setattr(QMessageBox, "question", lambda *args: QMessageBox.No)
    qtbot.mouseClick(widget.btn4, qt_api.QtCore.Qt.MouseButton.LeftButton)
    assert widget.label.text() == "I Dont Like Pyside6"
